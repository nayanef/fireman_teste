from rest_framework import routers
from django.urls import path, include
from quotes import views


router = routers.DefaultRouter()
router.register(r'quotes', views.QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]