# Generated by Django 2.2.4 on 2019-09-03 18:21

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0077_blogpage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpagecategory',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
