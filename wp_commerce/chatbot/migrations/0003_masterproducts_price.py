# Generated by Django 4.0.5 on 2022-09-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_masterproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterproducts',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
