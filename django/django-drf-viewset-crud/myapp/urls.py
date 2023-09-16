from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet, HelloWorldAPIView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('hello/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('', include(router.urls)),
]
