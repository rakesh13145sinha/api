from django.urls import path
from test1 import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('upload/',views.upload_file,name="upload file"),
    path('temp/',views.temp_file_store,name="tremp_file_store"),
    path('delete/<int:id>/',views.delete_file,name="delete files"),
    path('play/<int:id>/',views.play_video, name="play video"),
    path('decode/',views.decompression,name="decompression")
    
    
    
]