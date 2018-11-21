from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^video/$',views.video,name="video"),
	url(r'^$',views.index,name="home"),
]