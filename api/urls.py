from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from secureApp import views as secViews


urlpatterns = [
    path('', views.apiView),
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # SecureApp
    path('data/', secViews.secureHubList, name="secureHubList"),
    path('data/<int:pk>/', secViews.secureHub1.as_view(), name="secureHub1"),
    # Software
    path('apps/', secViews.softwareList, name="softwareList")
]
