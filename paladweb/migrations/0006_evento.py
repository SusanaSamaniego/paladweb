# Generated by Django 4.2.2 on 2023-06-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paladweb', '0005_remove_profile_user_remove_tienda_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]