# Generated by Django 5.0.7 on 2024-07-28 09:58

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_number', models.CharField(default='09123456789', help_text='Enter your company phone number', max_length=15)),
                ('motivate_text', models.CharField(default='09123456789', help_text='Something to make user motivated like : Get A Cash Offer Today', max_length=250)),
                ('motivate_url', models.URLField(default='Enter motivation url', help_text='When user cliked on motivate text, where shall he go? enter the url.')),
                ('company_name', models.CharField(default='09123456789', help_text="Enter name of your company (it'll displayed below the logo)", max_length=200)),
                ('company_claims', models.CharField(default='09123456789', help_text='Enter your company claims', max_length=300)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeaderMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('setting', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='header_menu', to='base.sitesettings')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
