from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, PostViewSet, ForumViewSet, AttachmentViewSet

router = DefaultRouter()
router.register(r'forums', ForumViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'posts', PostViewSet)
router.register(r'attchs', AttachmentViewSet)

urlpatterns = router.urls