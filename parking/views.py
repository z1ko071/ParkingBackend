from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ParkingZone
from .serializer import ParkingZoneSerializer


class ParkingZoneListView(APIView):
    @staticmethod
    def get(request):
        parking_zones = ParkingZone.objects.all()
        serializer = ParkingZoneSerializer(parking_zones, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def user_arrived(request, parking_lot_id):
    try:
        is_electro = request.query_params.get('electro')
        parking_lot = ParkingZone.objects.get(id=parking_lot_id)

        if is_electro == 'False' and parking_lot.empty_count != 0:
            parking_lot.empty_count -= 1
            parking_lot.save()
            return Response({"message": "Parkovkaga joylandi ody"})
        elif is_electro == 'True' and parking_lot.empty_electro_count != 0:
            parking_lot.empty_electro_count -= 1
            parking_lot.save()
            return Response({"message": "Parkovkaga joylandi electro"})
        else:
            parking_lot.save()
            return Response({"message": "Joy qolmagan !!!"}, status=status.HTTP_404_NOT_FOUND)

    except ParkingZone.DoesNotExist:
        return Response({"message": "Bunday Parkovka mavjud emas !!!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def user_went(request, parking_lot_id):
    try:
        is_electro = request.query_params.get('electro')
        parking_lot = ParkingZone.objects.get(id=parking_lot_id)

        print(is_electro == 'True')
        print(is_electro == 'False')

        if is_electro == 'False' and parking_lot.empty_count < parking_lot.max_count:
            parking_lot.empty_count += 1
            parking_lot.save()
            return Response({"message": "Parkovkadan ketti ody"})
        elif is_electro == 'True' and parking_lot.empty_electro_count < parking_lot.electro_count:
            parking_lot.empty_electro_count += 1
            parking_lot.save()
            return Response({"message": "Parkovkadan ketti electro"})
        else:
            parking_lot.save()
            return Response({"message": "Max darajada bosh"}, status=status.HTTP_404_NOT_FOUND)

    except ParkingZone.DoesNotExist:
        return Response({"message": "Bunday Parkovka mavjud emas !!!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_nearby_parking_zones(request):
    try:
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')

        if lon and lat:

            user_lat = float(lat)
            user_lon = float(lon)

            radius = 0.015
            lat_min = user_lat - radius
            lat_max = user_lat + radius
            lon_min = user_lon - radius
            lon_max = user_lon + radius
            nearby_parking_zones = ParkingZone.objects.filter(
                lat__range=(lat_min, lat_max),
                lon__range=(lon_min, lon_max)
            )
            serializer = ParkingZoneSerializer(nearby_parking_zones, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Lat lon jonating !!!"}, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        return Response({"message": "Invalid latitude or longitude provided."}, status=status.HTTP_400_BAD_REQUEST)


class ParkingZoneDetail(APIView):
    @staticmethod
    def get(request, pk):
        try:
            parking_zone = ParkingZone.objects.get(pk=pk)
            serializer = ParkingZoneSerializer(parking_zone)
            return Response(serializer.data)
        except ParkingZone.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
