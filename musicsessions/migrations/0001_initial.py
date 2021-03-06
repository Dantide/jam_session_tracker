# Generated by Django 2.2.3 on 2019-08-05 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='date of session start')),
                ('session_type', models.CharField(choices=[('PR', 'Practice'), ('JAM', 'Jam')], default='PR', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('appx_bpm', models.IntegerField(default=0, verbose_name='approximate bpm')),
            ],
        ),
        migrations.CreateModel(
            name='Tune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('composer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TuneRealBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_num', models.IntegerField(default=0, verbose_name='page number')),
                ('real_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.RealBook')),
                ('tune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Tune')),
            ],
        ),
        migrations.AddField(
            model_name='tune',
            name='books',
            field=models.ManyToManyField(through='musicsessions.TuneRealBook', to='musicsessions.RealBook'),
        ),
        migrations.AddField(
            model_name='tune',
            name='default_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Style'),
        ),
        migrations.AddField(
            model_name='tune',
            name='default_tempo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Tempo'),
        ),
        migrations.AddField(
            model_name='tune',
            name='tags',
            field=models.ManyToManyField(to='musicsessions.Tag'),
        ),
        migrations.CreateModel(
            name='SessionTune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.RealBook')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Session')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Style')),
                ('tempo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Tempo')),
                ('tune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicsessions.Tune')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='tunes',
            field=models.ManyToManyField(through='musicsessions.SessionTune', to='musicsessions.Tune'),
        ),
    ]
