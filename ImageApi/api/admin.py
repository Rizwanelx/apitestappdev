from django.contrib import admin
from ImageApi.api.models import Movie
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title','image', 'description')
