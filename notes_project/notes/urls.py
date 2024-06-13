from django.urls import path
from .views import upload_note, upload_content, get_notes, get_note_content,get_note,download_file, delete_note,delete_content, update_folder,get_folder_name,get_folder_notes,add_note_to_folder

urlpatterns = [
    path("upload_note/",upload_note,name="upload_note"),
    path("upload_content/",upload_content,name="upload_content"),
    path("get_notes/<int:user_id>/",get_notes,name="get_notes"),
    path("get_note_content/<int:note_id>/",get_note_content,name="get_note_content"),
    path("get_note/<int:note_id>/",get_note,name="get_note"),
    path("download_file/<int:content_id>/",download_file,name="download_file"),
    path("get_note_content/<int:note_id>/",get_note_content,name="get_note_content"),
    path("delete_note/<int:note_id>/",delete_note,name="delete_note"),
    path("delete_content/<int:content_id>/",delete_content,name="delete_content"),
    path("update_folder/",update_folder,name="update_folder"),
    path("get_folder_name/<int:user_id>/",get_folder_name,name="get_folder_name"),
    path("get_folder_notes/<str:folder_name>/",get_folder_notes,name="get_folder_notes"),
    path("add_note_to_folder/<int:note_id>/<int:folder_id>/",add_note_to_folder,name="add_note_to_folder")
]