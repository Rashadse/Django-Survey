from django.conf.urls import include, url
from django.contrib import admin
from .views import home_view, rest_view, survey_forwarding, confirm
from . import views

admin.autodiscover()
app_name = 'exam'

urlpatterns = [


    url(r'questions/$', views.ListCreateQuestion.as_view(), name='question_list'),

    url(r'questions/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyQuestion.as_view(),
        name='question_detail'),

    url(r'responses/$', views.ListCreateResponse.as_view(), name='response_list'),

    url(r'responses/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyResponse.as_view(),
        name='response_detail'),

    url( r'^$', home_view, name='home' ),
    url( r'^rest/$', rest_view, name='home' ),
    url( r'(?P<id>\d+)/$', survey_forwarding, name='survey_detail' ),
    url( r'^confirm/$', confirm, name='confirmation' ),
    url( r'^admin/doc/', include( 'django.contrib.admindocs.urls' ) ),
    url( r'^admin/', admin.site.urls ),

]
