from django.urls import path

from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('add/', views.journal_add, name='journal-add'),
    path('<int:pageID>/', views.journal_edit, name='journal-edit'),
    path('delete/<int:pageID>', views.journal_delete, name='journal-delete'),
    path('graph/', views.graph, name='graph'),
]