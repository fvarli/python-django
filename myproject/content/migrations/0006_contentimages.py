# Generated by Django 3.0.6 on 2020-05-17 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20200515_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Content')),
            ],
        ),
    ]
