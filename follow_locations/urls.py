from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowLocationList.as_view()),
    path('followers/<int:pk>/', views.FollowLocationDetail.as_view())
]
