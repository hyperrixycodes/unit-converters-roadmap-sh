from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/notes_list', views.notes_list, name='notes_list'),
    path('notes/create_note', views.create_note, name='create_note'),
    path('notes/edit_note/<int:id>', views.edit_note, name='edit_note'),
    path('notes/delete_note/<int:id>', views.delete_note, name='delete_note'),
]