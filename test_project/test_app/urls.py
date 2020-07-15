from django.conf.urls import url
from test_app import views

# TEMPLATE TAGGING
app_name = 'test_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faker/$', views.fakerListView.as_view(), name='faker'), # using CBV
    url(r'^faker/(?P<pk>\d+)/$', views.fakerDetailView.as_view(), name='fakerdetail'),
    url(r'^forms/$', views.forms_name, name='forms_name'),
    url(r'^relative/$', views.relative, name='relativeurl'),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^create/$', views.TopicCreateView.as_view(), name='create'),
    url(r'^create/(?P<pk>\d+)/$', views.TopicUpdateView.as_view(), name='update'),
    url(r'^create/delete/(?P<pk>\d+)$', views.TopicDeleteView.as_view(), name='delete'),
]