from django.urls import path
from follow_locations import views

urlpatterns = [
    path('follow/', views.FollowLocationList.as_view()),
    path('follow/<int:pk>/', views.FollowLocationDetail.as_view())
]
