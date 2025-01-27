from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

# Rejestruje model x z konfiguracją xAdmin
# Klasa PersonAdmin dostosowuje widok modelu Person w panelu administracyjnym
admin.site.register(Team) # Team Prosty widok w panelu administracyjnym
class PersonAdmin(admin.ModelAdmin):
    # list_display: Lista pól, które będą wyświetlane w widoku listy obiektów modelu Person. 
    # Dodaje możliwość filtrowania obiektów
    list_display = ['name', 'shirt_size', 'team']
    list_filter = ['team']


# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Person, PersonAdmin)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "opis"]
    list_filter = ["nazwa"]
    
admin.site.register(Stanowisko, StanowiskoAdmin)
class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description = "Stanowisko (ID)")
    def stanowisko_with_id(self, obj):
        if obj.stanowisko:
            return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
        return "Brak stanowiska"
    
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_with_id', 'data_dodania']
    list_filter = ["stanowisko", "data_dodania"]
    
admin.site.register(Osoba, OsobaAdmin)