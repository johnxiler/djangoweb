# Generated by Django 4.1.3 on 2022-12-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_language', models.CharField(max_length=2)),
                ('target_language', models.CharField(max_length=2)),
                ('source_text', models.TextField()),
                ('translated_text', models.TextField(blank=True)),
            ],
        ),
    ]
