from django.urls import path 

from . import views

# set app namespace-> django can distinguish which app is referenced

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),

    # /polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),

    #/poll/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    #/poll/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
