from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

# one ingredient can be in multiple cookies
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    cost = models.FloatField()

    class Meta:
        ordering = ['ingredient_name', ]

    def __str__(self):
        return f"{self.ingredient_name}, {self.cost}"

# one cookie can have multiple ingredients
class Cookie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    cookie_name = models.CharField(max_length=50)
    price = models.IntegerField()
    instructions = models.CharField(max_length=500)
    ingredients = models.ManyToManyField(Ingredient, through='CookieIngredient')

    class Meta:
        ordering = ['user', '-id', ]

    def get_absolute_url(self):
        return reverse('cookie_update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.user}, {self.cookie_name}, {self.price}, {self.instructions}"

# connect a Cookie its Ingredients
class CookieIngredient(models.Model):
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE, related_name='cookie')
    measure = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient')

    class Meta:
        ordering = ['cookie', 'ingredient', ]

    def __str__(self):
        return "{}_{}_{}".format(self.cookie.__str__(), self.measure.__str__(), self.ingredient.__str__())
