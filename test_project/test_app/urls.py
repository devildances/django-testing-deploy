from django.conf.urls import url
from test_app import views

# TEMPLATE TAGGING
app_name = 'test_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faker/$', views.faker, name='faker'),
    url(r'^forms/$', views.forms_name, name='forms_name'),
    url(r'^relative/$', views.relative, name='relativeurl'),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
]