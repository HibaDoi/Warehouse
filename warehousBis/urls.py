#la propriete path chemain de django
from django.urls import path 
#view ces celui qui affiche  path la réponse 
from . import views
#path utilise route (urls) le chemin, le seconde est fonction de views
urlpatterns =[
path('home/',views.say_hello),
path('get_temperature_data/', views.get_temperature_data),
]

