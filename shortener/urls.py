from django.conf.urls import url

from shortener import views

urlpatterns = [
    url(r'^(?P<slug>[\w]{,16})/$', views.UrlRedirectView.as_view(), name="url_redirect")
]
