# Generated by Django 4.1.3 on 2022-11-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=500)),
                ('pincode', models.CharField(max_length=10)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('long', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
