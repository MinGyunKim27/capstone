# Generated by Django 5.0.3 on 2024-04-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facemeet', '0003_meeting_transcription_participant_engagement_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_id',
            field=models.CharField(default='e9aa581159b04f6c90921eec014c88cc', max_length=100),
        ),
    ]
