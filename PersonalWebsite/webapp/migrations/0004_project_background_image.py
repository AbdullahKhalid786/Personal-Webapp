# Generated by Django 5.1.1 on 2024-10-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_blogpost_text_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='project_backgrounds/'),
        ),
    ]
