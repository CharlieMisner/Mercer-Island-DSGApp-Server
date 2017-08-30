from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emails import views

urlpatterns = [
    url(r'^emails/$', views.EmailTest.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)