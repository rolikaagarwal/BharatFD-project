# Generated by Django 5.0.7 on 2025-01-31 12:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("faqs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="answer",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
