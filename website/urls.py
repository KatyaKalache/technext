from django.urls import path
from . import views

urlpatterns = [
    path('search-patents/', views.get_data)
]