# Generated by Django 3.1.4 on 2020-12-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suitability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto', models.CharField(max_length=50)),
                ('disability', models.CharField(max_length=50)),
                ('home', models.CharField(max_length=50)),
                ('life', models.CharField(max_length=50)),
                ('renters', models.CharField(max_length=50)),
            ],
        ),
    ]
