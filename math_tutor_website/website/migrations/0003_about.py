# Generated by Django 4.2.1 on 2023-07-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_studyingprograms_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название раздела')),
                ('about', models.CharField(db_index=True, max_length=255, verbose_name='Название раздела')),
            ],
        ),
    ]
