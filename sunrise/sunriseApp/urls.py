from django.urls import path

from . import views

app_name = 'sunriseApp'
urlpatterns = [
    # ex: /sunriseApp/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /sunriseApp/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /sunriseApp/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /sunriseApp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
