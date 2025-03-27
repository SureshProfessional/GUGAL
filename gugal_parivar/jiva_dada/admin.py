from django.contrib import admin
from .models import *

class Jiva(admin.ModelAdmin):
    list_display = ["name"]

class Dada(admin.ModelAdmin):
    list_display = ["son_of_jivadada","dada_name"]

class Uncle(admin.ModelAdmin):
    list_display = ["son_of_dada","uncle_name"]



admin.site.register(Son_of_jivadada,Jiva)
admin.site.register(Son_of_dada,Dada)
admin.site.register(Son_of_uncle,Uncle)
