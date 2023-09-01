from django.urls import path
from . import views

urlpatterns = [
    path("cookie_list", views.CookieListView.as_view(), name="cookie_list"),
    path("cookie_pricelist", views.CookiePriceListView.as_view(), name="cookie_price_list"),
    path("cookie_recipe/<int:pk>", views.CookieDetailView.as_view(), name="cookie_detail"),
    path('cookie_add/', views.CookieCreateView.as_view(), name="cookie_add"),
    path("cookie_update/<int:pk>", views.CookieUpdateView.as_view(), name="cookie_update"),
    path("cookie_delete/<int:pk>", views.CookieDeleteView.as_view(), name="cookie_confirm_delete"),
]
