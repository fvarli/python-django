# Generated by Django 3.0.6 on 2020-05-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_settings_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='github',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]