from rest_framework.routers import DefaultRouter
from .views import UserViewSet, InventoryViewSet, ChangeLogViewSet, login_view, signup , logout , profile_view
from django.urls import path

router = DefaultRouter()
router.register("items", InventoryViewSet, basename="items")
router.register("changes", ChangeLogViewSet, basename="changes")
router.register("users", UserViewSet)




urlpatterns = router.urls + [
    path('login/',login_view, name = 'login'),
    path('signup/',signup, name = 'signup'),
    path('logout/',logout, name = 'logout'),
    path('profile/', profile_view, name='profile'),
]