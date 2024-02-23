from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MyModelViewSet

# デフォルトのルーターを作成
router = DefaultRouter()

# MyModelViewSetをルーターに登録
router.register(r'models', MyModelViewSet)

# APIのルートURLを設定
urlpatterns = [
    path('', include(router.urls)),
]
