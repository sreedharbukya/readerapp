from rest_framework import routers

from app.api.author.views.author_viewset import AuthorViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'', AuthorViewSet)


urlpatterns = router.urls
