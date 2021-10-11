from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('posts', views.PostRetrieveListView, basename='posts-api')

urlpatterns = router.urls
