# Generated by Django 5.0.7 on 2024-07-28 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_headermenu_setting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='company_claims',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='company_number',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='motivate_text',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='motivate_url',
        ),
    ]
