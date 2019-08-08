import os
import csv

from django.db import models

# Create your models here.
class Style(models.Model):
    name = models.CharField(
        max_length=20,
        default=20,
    )
    description = models.CharField(
        max_length=100,
        default="",
    )

    def __str__(self):
        return self.name


class Tempo(models.Model):
    name = models.CharField(
        max_length=50,
        default="",
    )
    appx_bpm = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class RealBook(models.Model):
    name = models.CharField(max_length=100)
    pub_company = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tune(models.Model):
    name = models.CharField(max_length=50)
    composer = models.CharField(max_length=50)
    default_style = models.ForeignKey(Style, on_delete=models.CASCADE)
    default_tempo = models.ForeignKey(Tempo, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    books = models.ManyToManyField(RealBook, through='TuneRealBook', blank=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    PRACTICE = 'PR'
    JAM = 'JAM'
    SESSION_TYPE_CHOICES = [
        (PRACTICE, 'Practice'),
        (JAM, 'Jam'),
    ]
    session_title = models.CharField(max_length=200)
    start_date = models.DateTimeField('date of session start')
    session_type = models.CharField(
        max_length=50,
        choices=SESSION_TYPE_CHOICES,
        default=PRACTICE,
    )
    tunes = models.ManyToManyField(Tune, through='SessionTune')

    def __str__(self):
        return self.session_title

    def number_of_tunes(self):
        pass



# Linking Tables
class SessionTune(models.Model):
    tune = models.ForeignKey(Tune, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    real_book = models.ForeignKey(RealBook, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    tempo = models.ForeignKey(Tempo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.session) + ": " + str(self.tune)


class TuneRealBook(models.Model):
    real_book = models.ForeignKey(RealBook, on_delete=models.CASCADE)
    tune = models.ForeignKey(Tune, on_delete=models.CASCADE)
    page_num = models.IntegerField('page number', default=0)

    def __str__(self):
        return str(self.real_book) + ": " + str(self.tune)