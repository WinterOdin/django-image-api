from .views import PictureViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('picture', PictureViewset, basename="picture")
urlpatterns = router.urls