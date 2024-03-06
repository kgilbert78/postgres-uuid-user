from rest_framework.routers import DefaultRouter
from .views import FileViewSet

router = DefaultRouter()
router.register(r'file-dates', FileViewSet, basename='file-dates')
urlpatterns = router.urls