# Generated by Django 5.0.2 on 2024-02-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attentions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attentionmodel',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]