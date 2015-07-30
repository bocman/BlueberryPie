from django.conf.urls import url, include
from rest_framework import routers
from client import views

router = routers.DefaultRouter()
router.register(r'rest/users', views.UserViewSet)
router.register(r'rest/groups', views.GroupViewSet)
# router.register(r'rest/update/(?P<pk>[0-9]+)', views.GPIOUpdateView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^rest/update/$', views.GPIOUpdateView.as_view(), name='detail'),
    url(r'^rest/gpio/all/', views.GPIOListView.as_view(), name='item_statuses'),
    url(r'^rest/gpio/update/(?P<pk>[0-9]+)/', views.GPIODetailView.as_view(), name='item_update')

]