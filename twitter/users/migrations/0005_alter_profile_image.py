# Generated by Django 3.2.13 on 2022-06-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='logo.png', upload_to='profile-pics/'),
        ),
    ]