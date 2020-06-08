from django.contrib import admin

from .models import Tune, Session, Style, Tempo, RealBook, Tag, SessionTune, TuneRealBook

# username: admin
# password: BassHEad2.0

# Register your models here.
class SessionTuneInline(admin.TabularInline):
    model = SessionTune

class TuneRealBookInline(admin.TabularInline):
    extra = 1
    model = TuneRealBook
    ordering = ['real_book','tune','page_num']


class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_title', 'start_date', 'session_type')
    inlines = [SessionTuneInline]

class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class TuneAdmin(admin.ModelAdmin):
    list_display = ('name', 'composer', 'default_style', 'default_tempo')
    inlines = [TuneRealBookInline]
    search_fields = ['name']
    list_filter = ['default_style', 'default_tempo']
    ordering = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class TempoAdmin(admin.ModelAdmin):
    list_display = ('name', 'appx_bpm')

class RealBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_company')
    inlines = [TuneRealBookInline]

admin.site.register(Session, SessionAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Tempo, TempoAdmin)
admin.site.register(Tune, TuneAdmin)
admin.site.register(RealBook, RealBookAdmin)
admin.site.register(Tag, TagAdmin)