from django.conf.urls import url, include, patterns
from rest_framework import routers
from client import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/gpio/all/', views.GPIOListView.as_view(), name='item_statuses'),
    url(r'^api/gpio/update/(?P<pk>[0-9]+)/', views.GPIODetailView.as_view(), name='item_update'),
   
    url(r'^api/ping/', views.Ping.as_view(), name='ping')
)
