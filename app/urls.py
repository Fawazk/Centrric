from unicodedata import name
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    # login with jwt token
    path('login/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    # jwt refresh token api
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    # register api
    path('register', views.Register.as_view(), name ='Register'),
    # api to follow 
    path('follow',views.UserFollowViews.as_view(),name='follow'),
    # api to get following 
    path('get-following',views.Getfollowing.as_view(),name="getfollowing"),
    # api to get followers
    path('get-followers',views.GetFollowers.as_view(),name="getfollowers"),
    # api to unfollow
    path('unfollow/<int:uid>',views.UnFollow.as_view(),name="unfollow"),
    # To get user details
    path('user-details',views.userDetails.as_view(),name="userdetails")
]