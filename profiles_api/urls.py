from django.urls import path, include

# APIView
from profiles_api import views

# ViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('hello-viewset', views.vs_hello.HelloViewSet, basename='hello-viewset')
# no tiene el 3 argumento por queryset
router.register('profile',views.vs_user_profile.UserProfileViewSet)
router.register('feed', views.vs_user_profile_feed.UserProfileFeedViewSet)

urlpatterns = [
    # APIView
    path('hello-view', views.vv_hello.HelloApiView.as_view()),
    path('login/', views.vv_user_login.UserLoginView.as_view()),
    # Viewset
    path('',include(router.urls)) # include all patterns first blank
]
