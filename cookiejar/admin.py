from django.contrib import admin

from .models import Ingredient, Cookie, CookieIngredient

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["ingredient_name", "cost", ]
    ordering = ["ingredient_name", ]
    list_filter = ["ingredient_name", ]
    fields = [
        ('ingredient', 'cost')
    ]

class CookieAdmin(admin.ModelAdmin):
    list_display = ["user", "cookie_name", "price", "instructions", ]
    ordering = ["user", "-id", ]
    list_filter = ["user", "id", "cookie_name", ]
    fields = [
        'user',
        'cookie_name',
        'price',
        'instructions'
    ]

class CookieIngredientAdmin(admin.ModelAdmin):
    list_display = ["cookie", "measure", "ingredient", ]
    ordering = ["cookie", ]
    fields = [
        'cookie',
        ('measure', 'ingredient')
    ]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Cookie, CookieAdmin)
admin.site.register(CookieIngredient, CookieIngredientAdmin)
