from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import pprint

from .models import Ingredient, Cookie, CookieIngredient

# Create your views here.

class CookieListView(LoginRequiredMixin, ListView):
    context_object_name = 'cookie_list'
    template_name = 'cookiejar/cookie_list.html'
    queryset = Cookie.objects.all()
    paginate_by = 10

    def get_queryset(self):  # return all cookies for current user
        queryset = super(CookieListView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class CookiePriceListView(LoginRequiredMixin, ListView):
    model = Cookie
    context_object_name = 'cookie_price_list'
    template_name = 'cookiejar/cookie_price_list.html'
    queryset = Cookie.objects.all().order_by("price")
    paginate_by = 10

    def get_queryset(self):  # return all cookies sorted by price for current user
        queryset = super(CookiePriceListView, self).get_queryset()
        return queryset.filter(user=self.request.user)

class CookieDetailView(LoginRequiredMixin, DetailView):
    model = Cookie
    context_object_name = 'recipe'
    template_name = 'cookiejar/cookie_detail.html'

    def get_queryset(self):
        queryset = super(CookieDetailView, self).get_queryset()
        return queryset.filter(user=self.request.user)

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

class CookieCreateView(LoginRequiredMixin, CreateView):
    model = Cookie
    fields = ['cookie_name', 'price', 'instructions', 'ingredients']
    template_name = 'cookiejar/cookie_add.html'
    success_url = reverse_lazy('cookie_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CookieCreateView, self).form_valid(form)

class CookieUpdateView(LoginRequiredMixin, UpdateView):
    model = Cookie
    fields = ['cookie_name', 'price', 'instructions']
    template_name = 'cookiejar/cookie_update.html'
    success_url = reverse_lazy('cookie_list')

    def get_queryset(self):
        queryset = super(CookieUpdateView, self).get_queryset()
        return queryset.filter(user=self.request.user)

class CookieDeleteView(LoginRequiredMixin, DeleteView):
    model = Cookie
    context_object_name = 'recipe'
    template_name = 'cookiejar/cookie_confirm_delete.html'
    success_url = reverse_lazy('cookie_list')

    def get_queryset(self):
        queryset = super(CookieDeleteView, self).get_queryset()
        return queryset.filter(user=self.request.user)

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
