# Generated by Django 5.0.3 on 2024-04-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facemeet', '0006_meeting_participants_alter_expressionscore_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_id',
            field=models.CharField(default='4dc30e1bbe154609a8a235cfba72b19a', max_length=100),
        ),
    ]
