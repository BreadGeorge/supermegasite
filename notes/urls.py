from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.index, name='index'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('delete_note/<note_id>', views.delete_note, name='delete_note'),
    path('delete_block/<block_id>', views.delete_block, name='delete_block'),
]