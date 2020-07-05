from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from p_shelter.models import Kind, Breed, Animal
from django.views.generic import DetailView

#отображение индекс
def index(request):
    #метод самостоятельно проверит предварительно созданную папку templates и найдет шаблон
    template = loader.get_template('index.html')
    #считаем количесвто животных
    animals_count = Animal.objects.all().count()
    #словарь , в котором есть  ключи, используемых в  html-шаблоне
    animals_data = {"title": "Приют домашних животных", "animals_count": animals_count }
    return HttpResponse(template.render(animals_data))

#отображение контактов
def contact(request):
    #метод самостоятельно проверит предварительно созданную папку templates и найдет шаблон
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def pets_list(request):
    template = loader.get_template('pets_list.html')
    pets = Animal.objects.all()
    #фильтрация собак
    dog = Kind.objects.get(name="СОБАКА")
    pets_dog = Animal.objects.filter(kind=dog)
    #фильтрация попугаев
    parrot = Kind.objects.get(name="ПОПУГАЙ")
    pets_parrot = Animal.objects.filter(kind=parrot)
    #фильтрация кошек
    cat = Kind.objects.get(name="КОШКА")
    pets_cat = Animal.objects.filter(kind=cat)
    pets_data = {
        "pets": pets,
        "pets_dog": pets_dog,
        "pets_cat":pets_cat,
        "pets_parrot":pets_parrot,
    }
    return HttpResponse(template.render(pets_data))
    
class PetView(DetailView):
      model = Animal
      template_name = 'pet_detail.html'