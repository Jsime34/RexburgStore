# Generated by Django 5.2.1 on 2025-06-17 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0005_message_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginpage.listing'),
        ),
    ]
