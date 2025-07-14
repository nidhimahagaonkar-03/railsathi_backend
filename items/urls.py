from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'', ItemViewSet)  # <-- register at root, not 'items'

urlpatterns = [
    path('items/', include(router.urls)),  # now /items/ will work
]