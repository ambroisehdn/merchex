# Generated by Django 4.1.1 on 2022-09-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.CharField(default='une description heee', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='band',
            name='type',
            field=models.CharField(choices=[('RC', 'Records'), ('CH', 'Clothings'), ('PT', 'Posters'), ('ML', 'Miscellaneous')], default='CH', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('AR', 'Alternative Rock'), ('SP', 'Synth Pop')], max_length=5),
        ),
    ]
