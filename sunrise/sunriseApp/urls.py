from django.urls import path

from . import views

app_name = 'sunriseApp'
urlpatterns = [
    # ex: /sunriseApp/
    path('', views.index, name='index'),
    # ex: /sunriseApp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /sunriseApp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /sunriseApp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
