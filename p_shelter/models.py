from django.db import models

# класс вида животного
class Kind(models.Model):
    DOG = 'СОБАКА'
    CAT = 'КОШКА'
    PARROT = 'ПОПУГАЙ'
    KIND_OF_ANIMALS = [
        (DOG, 'СОБАКА'),
        (CAT, 'КОШКА'),
        (PARROT, 'ПОПУГАЙ'),
    ]
    name = models.CharField(
        max_length=10,
        choices=KIND_OF_ANIMALS,
        default=DOG,
    )
    def __str__(self):
        return self.name
#порода
class Breed(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Порода")
    def __str__(self):
        return self.name

# класс вида животного
class Animal(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256, verbose_name="Кличка")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name="Порода")
    description=models.TextField(verbose_name="Описание")
    date=models.DateTimeField(auto_now_add=True, verbose_name="Время")
    kind = models.ForeignKey(Kind,on_delete=models.CASCADE,blank=True, verbose_name="Вид животного")
    photo = models.ImageField(upload_to='photo', blank=True, verbose_name="Фото")
    def __str__(self):
        return "{} ({}, {})".format(self.name, self.kind, self.breed)

