from django.contrib import admin
from .models import Joke


class JokeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Joke, JokeAdmin)
