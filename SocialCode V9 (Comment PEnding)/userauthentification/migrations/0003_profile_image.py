# Generated by Django 4.1.2 on 2022-12-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentification', '0002_profile_bio_profile_created_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pciture'),
        ),
    ]
