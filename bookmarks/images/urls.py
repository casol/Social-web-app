from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$',
        views.image_created,
        name='create'),

    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.image_detail,
        name='detail'),

    # Ajax action with jQuery
    url(r'^like/$',
        views.image_like,
        name='like'),

    # AJAX pagination
    url(r'^$',
        views.image_list,
        name='list'),

    # REDIS ranking
    url(r'^ranking/$',
        views.image_ranking,
        name='create'),

]