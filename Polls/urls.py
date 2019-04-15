from django.urls import include, re_path
from Polls import views

app_name = 'Polls'
urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^(?P<question_id>\d)/$', views.detail, name = 'detail'),
    re_path(r'^(?P<question_id>\d)/result/$', views.results, name = 'result'),
    re_path(r'^(?P<question_id>\d)/vote/$', views.vote, name = 'vote'),
]