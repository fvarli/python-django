from django.contrib import admin

# Register your models here.
from content.models import Category, Content, Images, Comment
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'get_image_tag']
    list_filter = ['status']
    readonly_fields = ('get_image_tag',)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'detail', 'get_image_tag', 'status']
    readonly_fields = ('get_image_tag',)
    list_filter = ['status', 'category']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'get_image_tag']
    readonly_fields = ('get_image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_contents_count', 'related_contents_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Content,
                'category',
                'contents_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Content,
                 'category',
                 'contents_count',
                 cumulative=False)
        return qs

    def related_contents_count(self, instance):
        return instance.contents_count
    related_contents_count.short_description = 'Related contents (for this specific category)'

    def related_contents_cumulative_count(self, instance):
        return instance.contents_cumulative_count
    related_contents_cumulative_count.short_description = 'Related contents (in tree)'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'content', 'user', 'email', 'rate', 'status']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)
