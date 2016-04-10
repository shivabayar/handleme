from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^$', views.get_index_page),
    url(r'^search/twitter/query/(?P<handler>([aA-zZ]+))/$', views.UserViewSet.as_view()),
]
