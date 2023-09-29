from django.urls import path
from .views import PersonaView


urlpatterns=[
    path('persona/', PersonaView.as_view(),name='personas_list'),
    path('persona/<int:id>', PersonaView.as_view(),name='personas_process')
]