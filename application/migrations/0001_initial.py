# Generated by Django 4.2.2 on 2023-06-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(max_length=20, null=True)),
                ('passport_photo', models.ImageField(upload_to=None)),
                ('application_country', models.CharField(max_length=50)),
                ('nigeria_embassy', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Emmail Address')),
                ('date_of_entry', models.DateField(null=True)),
                ('visa_type', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
