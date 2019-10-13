from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^subscribe/',views.mysubscribe,name = 'subscribe'),
]