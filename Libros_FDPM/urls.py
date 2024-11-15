from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.LibroListView.as_view(), name='libro_list'),
    path('libro/<int:pk>/', views.LibroDetailView.as_view(), name='libro_detail'),
    path('libro/new/', views.LibroCreateView.as_view(), name='libro_new'),
    path('libro/<int:pk>/edit/', views.LibroUpdateView.as_view(), name='libro_edit'),
    path('libro/<int:pk>/delete/', views.LibroDeleteView.as_view(), name='libro_delete'),
]