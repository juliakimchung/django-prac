from django.conf.urls import url
from . import views
app_name = "products_app"
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^lists', views.home, name='home'),
	url(r'^create/$', views.template_to_create, name='create'),
	url(r'^(?P<product_id>[0-9]+)specific/$', views.specifics, name='specific'),
	url(r'^detail/$', views.create, name='detail'),
	url(r'^register/$', views.Register.as_view(), name="register"),
	url(r'^register_user/$', views.register_user, name='register_user'),
	url(r'^login/$', views.login_user, name='login'),
	url(r'^logout/$', views.logout_user, name="logout"),
]