from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('projects/', views.projects, name='projects'),
    path('projects/add/', views.add_project, name='add-project'),

    path('contact/', views.contact, name='contact'),

    path('testimonies/', views.TestimonyListView.as_view(), name='testimony-list'),
    path('testimonies/add/', views.add_testimony, name='add-testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony-detail'),
]