from django.contrib import admin
from firetracker.fires.models import State, City, Address, Department, Station, Title, Person, StoryLink, Injury, Victim, Fire, Cause

class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class AddressAdmin(admin.ModelAdmin):
    prepopulated_fields = {'street_slug': ('street', ) }
    search_fields = ['street']

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class StationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class TitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title', ) }
    search_fields = ['title']

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('first_name', 'last_name' ) }
    search_fields = ['name']

class InjuryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'injury_slug': ('injury', ) }
    search_fields = ['injury']

class CauseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'type_slug': ('type', ) }
    search_fields = ['type']

admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(StoryLink)
admin.site.register(Injury, InjuryAdmin)
admin.site.register(Victim)
admin.site.register(Cause, CauseAdmin)
admin.site.register(Fire)