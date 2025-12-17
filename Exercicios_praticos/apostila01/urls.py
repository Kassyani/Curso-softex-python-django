
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet, basename='tarefas')

urlpatterns = [
    path('api/', include(router.urls)),
]
