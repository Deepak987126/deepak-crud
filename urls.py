from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [

    path('', views.StudentList.as_view(), name="get_student_list"),
    path('create/', views.StudentCreate.as_view(), name="crate_student_record"),
    path('re/<int:pk>/', views.StudentRetrieve.as_view(), name="Retrieve_record"),
    path('up/<int:pk>/', views.StudentUpdate.as_view(), name="update_record"),
    path('del/<int:pk>/', views.StudentDelete.as_view(), name="update_record"),

    # jwt root
    path('gettoken/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('verifytoken/', TokenVerifyView.as_view(), name="token_verify"),
]
