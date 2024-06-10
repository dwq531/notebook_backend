from django.urls import path
from .views import upload_user, get_user_by_name, download_file

urlpatterns = [
    path('upload_user/', upload_user),
    path('download_file/<int:user_id>/', download_file),
    path('get_user_by_name/<str:username>/', get_user_by_name)
]