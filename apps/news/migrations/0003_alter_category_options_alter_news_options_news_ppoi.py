# Generated by Django 4.1.1 on 2022-09-09 01:11

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_published_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-published_at'], 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Primary Point of Interest'),
        ),
    ]
