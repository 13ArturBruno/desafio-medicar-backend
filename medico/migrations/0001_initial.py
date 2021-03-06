# Generated by Django 3.2.13 on 2022-05-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('crm', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
