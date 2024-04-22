from django.urls import path

from parking.views import ParkingZoneListView, ParkingZoneDetail
from parking.views import user_arrived, user_went, get_nearby_parking_zones

urlpatterns = [
    path('parkings/', ParkingZoneListView.as_view(), name='parking-list'),
    path('user_arrived/<int:parking_lot_id>/car', user_arrived, name='user_arrived'),
    path('user_went/<int:parking_lot_id>/car', user_went, name='user_went'),
    path('near_parking/location', get_nearby_parking_zones, name='near_parking'),
    path('parking/<int:pk>/', ParkingZoneDetail.as_view(), name='parking_detail'),
]
