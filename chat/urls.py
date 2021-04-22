from django.urls import include, path
from rest_framework import routers
from chat import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/all', views.fetch_users),
    path('api/groups/all', views.fetch_groups),
]