# Generated by Django 2.2.10 on 2020-03-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozfest', '0012_auto_20200302_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_destination',
            field=models.CharField(blank=True, help_text='The URL for the page that the CTA button in the primary nav bar should redirect to.E.g., /proposals, https://example.com/external-link', max_length=2048),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_de',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_en',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_es',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_fr',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_nl',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_pl',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mozfesthomepage',
            name='cta_button_label_pt',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
    ]
