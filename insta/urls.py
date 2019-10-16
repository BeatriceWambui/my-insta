from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^subscribe/',views.mysubscribe,name = 'subscribe'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^like/(?P<image_id>[0-9]+)$',views.likePost, name='likePost'),
    url(r'^upload/$',views.upload,name='upload')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
