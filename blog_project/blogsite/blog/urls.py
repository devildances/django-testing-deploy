from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='postlist'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='postnew'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='postdetail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='postedit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='postremove'),
    url(r'^drafts/$', views.PostDraftView.as_view(), name='postdraft'),
    url(r'^about/$',views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='commentpost'),
    url(r'^comment/(?P<pk>\d+)/approval/$', views.approve_comment, name='commentapprove'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.remove_comment, name='commentremove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='postpublish')
]