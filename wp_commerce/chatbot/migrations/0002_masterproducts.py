# Generated by Django 4.0.5 on 2022-09-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=100)),
                ('product_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]