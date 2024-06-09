from django.urls import path
from .views import upload_note, upload_content, get_notes, get_note_content,get_note,download_file, delete_note,delete_content

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
]