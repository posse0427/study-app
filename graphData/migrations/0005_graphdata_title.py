# Generated by Django 3.0.2 on 2020-01-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphData', '0004_remove_graphdata_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdata',
            name='title',
            field=models.CharField(default=2, help_text='※任意', max_length=50, verbose_name='タイトル'),
            preserve_default=False,
        ),
    ]
