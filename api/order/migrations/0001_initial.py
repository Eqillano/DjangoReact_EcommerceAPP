# Generated by Django 3.0.8 on 2020-09-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_names', models.CharField(max_length=500)),
                ('total_products', models.CharField(default=0, max_length=500)),
                ('transaction_id', models.CharField(default=0, max_length=500)),
                ('total_amount', models.CharField(default=0, max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
    ]
