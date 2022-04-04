# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('<str:sexChoice>/<int:age>/<str:bmi>/<str:eduChoice>/<str:incomeChoice>/<str:genHealthChoice>/<str:healthCareChoice>/<str:noDocChoice>/<int:alcohol>/<str:cigarChoice>/<str:physicalChoice>/<str:fruitChoice>/<str:veggiesChoice>/<str:diffWalkChoice>/<str:BPChoice>/<str:cholChoice>/<str:cholCheckChoice>/<str:strokeChoice>/<str:heartDiseaseChoice>/<int:mental>/<int:physicalHealth>/results/', results, name='results'),
]
