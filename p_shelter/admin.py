#импортируем блок регистрации моделей
from django.contrib import admin
#импортируем необходимые модели
from p_shelter.models import Breed,Animal,Kind

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    pass
