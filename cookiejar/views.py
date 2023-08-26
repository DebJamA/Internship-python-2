from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import pprint

from .models import Ingredient, Cookie, CookieIngredient

# Create your views here.

class CookieListView(ListView):
    context_object_name = 'cookie_list'
    template_name = 'cookie_list.html'
    queryset = Cookie.objects.all()
    paginate_by = 10

    num = len(queryset)
    list1 = ' cookies in Cookie Jar '
    list2 = '(view first five):'
    print(f'\n{num}{list1}{list2}\n')

    cookielistslice = queryset[:5]
    for c in cookielistslice:
        print(c)
    print('\n')

class CookiePriceListView(ListView):
    model = Cookie
    context_object_name = 'cookie_price_list'
    template_name = 'cookiejar/cookie_price_list.html'
    queryset = Cookie.objects.all().order_by("price")
    paginate_by = 10

    num = len(queryset)
    prcl1 = ' cookies sorted by price, low to high'
    prcl2 = '(view first five):\n'
    print(f'\n{num}{prcl1}{prcl2}')

    pricelistslice = queryset[:5]
    for p in pricelistslice:
        print(p)
    print('\n')

class CookieDetailView(DetailView):
    model = Cookie
    context_object_name = 'recipe'
    template_name = 'cookiejar/cookie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = CookieIngredient.objects.filter(cookie_id=self.kwargs['pk']
                                                            ).prefetch_related('ingredient')
        context['ids'] = context['recipe'].values_list("ingredient_id", flat=True)
        context['total_cost'] = Ingredient.objects.filter(
            id__in=context['ids']).aggregate(totalcost=Sum('cost'))['totalcost']
        context['ingredient_count'] = Ingredient.objects.filter(id__in=context['ids']).count()

        print('\nAll ingredients for the selected cookie and total cost:\n')
        pprint.pprint(context)
        return context

class CookieCreateView(CreateView):
    model = Cookie
    fields = ['cookie_name', 'price', 'instructions']
    template_name = 'cookiejar/cookie_add.html'
    success_url = reverse_lazy('cookie_list')
    print('\nForm to CREATE new cookie\n')

class CookieUpdateView(UpdateView):
    model = Cookie
    fields = ['cookie_name', 'price', 'instructions']
    template_name = 'cookiejar/cookie_update.html'
    success_url = '/'
    print('\nForm to UPDATE cookie\n')

class CookieDeleteView(DeleteView):
    model = Cookie
    context_object_name = 'recipe'
    template_name = 'cookiejar/cookie_confirm_delete.html'
    success_url = reverse_lazy('cookie_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = CookieIngredient.objects.filter(cookie_id=self.kwargs['pk']
                                                            ).prefetch_related('ingredient')
        context['ids'] = context['recipe'].values_list("ingredient_id", flat=True)
        context['total_cost'] = Ingredient.objects.filter(
            id__in=context['ids']).aggregate(totalcost=Sum('cost'))['totalcost']
        context['ingredient_count'] = Ingredient.objects.filter(id__in=context['ids']).count()

        print('\nConfirm cookie DELETE:\n')
        pprint.pprint(context)
        return context
