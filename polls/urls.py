from . import views
from django.urls import path

from .views import IndexView, DetailView, VoteView, ResultsView

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('cbv/', IndexView.as_view(), name='cbv-index'),
    path('cbv/<int:pk>/', DetailView.as_view(), name='cbv-detail'),
    path('cbv/<int:pk>/results/', ResultsView.as_view(), name='cbv-results'),
    path('cbv/<int:pk>/vote/', VoteView.as_view(), name='cbv-vote')
]

# generic view
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]
