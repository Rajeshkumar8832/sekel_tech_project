from django.urls import path, include
from sekel_app.views import CategoryViewset, ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("category", CategoryViewset, basename="category")
router.register("product", ProductViewset, basename="product")

urlpatterns = [
    path('', include(router.urls))
]
