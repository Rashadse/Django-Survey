"""ed_reviews URL Configuration"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/exam/', include('exam.urls', namespace='surveys')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    path('', include( 'exam.urls' ) ),
]