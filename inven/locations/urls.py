from django.urls import path
from .views import (
                    LocationCreateView,
                    LocationDetailView,
                    LocationDeleteView,
                    LocationListView,
                    LocationUpdateView,
)
app_name= 'locations'
urlpatterns = [
    path ('', LocationListView.as_view(), name = 'location-list'),
    path ('<int:id>/', LocationDetailView.as_view(), name = 'location-detail'),
    path ('create/', LocationCreateView.as_view(), name = 'location-create'),
    path ('<int:id>/update/', LocationUpdateView.as_view(), name = 'location-update'),
    path ('<int:id>/delete/', LocationDeleteView.as_view(), name = 'location-delete'),
]