from django.urls import path
from . import views

urlpatterns = [
    path("", views.CookieListView.as_view(), name="cookie_list"),
    path("cookie/pricelist", views.CookiePriceListView.as_view(), name="cookie_price_list"),
    path("cookie/details/<int:pk>", views.CookieDetailView.as_view(), name="cookie_detail"),
    path('cookie/add/', views.CookieCreateView.as_view(), name="cookie_add"),
    path("cookie/update/<int:pk>", views.CookieUpdateView.as_view(), name="cookie_update"),
    path("cookie/delete/<int:pk>", views.CookieDeleteView.as_view(), name="cookie_confirm_delete"),
]
