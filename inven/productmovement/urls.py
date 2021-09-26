from django.urls import path
from .views import (
                    ProductMovementCreateView,
                    ProductMovementDetailView,
                    ProductMovementListView,
                    ProductMovementUpdateView,
                    ProductMovementDeleteView
)
app_name= 'productmovement'
urlpatterns = [
    path ('', ProductMovementListView.as_view(), name = 'productmov-list'),
    path ('createmov/', ProductMovementCreateView.as_view(), name = 'productmov-create'),
    path ('<int:id>/', ProductMovementDetailView.as_view(), name = 'productmov-detail'),
    path ('<int:id>/update/', ProductMovementUpdateView.as_view(), name = 'productmov-update'),
    path ('<int:id>/delete/', ProductMovementDeleteView.as_view(), name = 'productmov-delete'),

]