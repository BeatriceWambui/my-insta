from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^subscribe/',views.mysubscribe,name = 'subscribe'),
    url(r'^search/',views.search_results,name='search_results'),
    (url(r'^profile/$',views.profile,name='profile'))
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
