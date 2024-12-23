from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet, GenreViewSet, BookViewSet, BorrowViewSet

router = DefaultRouter()
router.register(r'author', AuthorViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'book', BookViewSet)
router.register(r'borrow', BorrowViewSet)



urlpatterns = router.urls


