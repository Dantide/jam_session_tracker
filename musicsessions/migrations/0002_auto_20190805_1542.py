# Generated by Django 2.2.3 on 2019-08-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsessions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempo',
            name='appx_bpm',
        ),
        migrations.AlterField(
            model_name='style',
            name='name',
            field=models.CharField(choices=[('BO', 'Bossa Nova'), ('LA', 'Latin'), ('SW', 'Swing'), ('LA/SW', 'Latin/Swing')], default='SW', max_length=10),
        ),
        migrations.AlterField(
            model_name='tempo',
            name='name',
            field=models.CharField(choices=[('SLO', 'Slow'), ('MED', 'Medium'), ('FST', 'Fast')], default='MED', max_length=50),
        ),
    ]
