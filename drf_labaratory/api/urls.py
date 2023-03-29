
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view()),
    path('tours/', get_create_tours),
    path('tours/<int:pk>/', get_edit_delete_tours),
    path('countries/', get_create_country),
    path('countries/<int:pk>/', get_edit_delete_country),
    path('excursions/', get_create_excursion),
    path('excursions/<int:pk>/', get_edit_delete_excursion),
    path('cart/', get_create_profile),
    path('cart/<int:pk>/', get_edit_delete_profile)
]