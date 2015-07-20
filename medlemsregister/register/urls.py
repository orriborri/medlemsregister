from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^add/$',views.add, name='add'),
    url(r'^add_member/$',views.add_member,name='add_member'),
    url(r'^$',views.index, name='index'),
]
