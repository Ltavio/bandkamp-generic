# Generated by Django 4.0.7 on 2022-12-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'email': 'This field must be unique.'}, max_length=254, unique=True),
        ),
    ]
