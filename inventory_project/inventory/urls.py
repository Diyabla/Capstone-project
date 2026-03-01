from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, ChangeLogViewSet

router = DefaultRouter()
router.register("items", InventoryViewSet, basename="items")
router.register("changes", ChangeLogViewSet, basename="changes")

urlpatterns = router.urls