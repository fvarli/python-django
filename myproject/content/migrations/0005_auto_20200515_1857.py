# Generated by Django 3.0.6 on 2020-05-15 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20200515_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Category'),
        ),
    ]
