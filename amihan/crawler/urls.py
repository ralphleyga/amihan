from rest_framework import routers

from .views import CrawlerViewSet

router = routers.SimpleRouter()
router.register(r'crawler', CrawlerViewSet)
urlpatterns = router.urls
