from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logoutview),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': views.logoutview}),
    
    url(r'^accounts/confirm/(?P<activation_key>[a-z0-9\-]+)/',views.register_confirm),
    url(r'^accounts/profile/',views.post_list),
    url(r'^register/success/',views.register_success),
    url(r'^register$',views.register),
]
