from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Stanowisko)
admin.site.register(Osoba)