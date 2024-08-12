# Generated by Django 5.0.7 on 2024-08-09 12:00

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_sitesettings_motivate_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('heading', models.TextField(help_text='This text displays in a large size into the footer')),
                ('text', models.TextField(help_text='Enter the main text it fits into the footer (like license or copyright content)')),
                ('setting', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer', to='base.sitesettings')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
