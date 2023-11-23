# vehicle/views.py
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from .models import Vehicle,History
from parkingzone.models import Zone
from .serializers import VehicleSerializer,VehicleHistorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'message': "Vehicle created successfully."
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': list(serializer.errors.items())[0][1][0]
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[::-1])

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer



class VehicleHistoryCreateView(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = VehicleHistorySerializer

    def create(self, request, *args, **kwargs):
        # Add your conditions before creating the object
        try:
            vehicle_id = request.data.get('vehicle')
            qr_id = request.data.get('qr_id')
            try:
                zone = Zone.objects.get(qr_id=qr_id)
            except:
                response = {
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': "Madarchod kaha qr scan karuchu"
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            data = request.data.copy()
            data['zone'] = zone.id
            check_online = len(History.objects.filter(vehicle=Vehicle.objects.get(id=vehicle_id),completed = False))
            if check_online == 0:
                # Your custom logic here
                serializer =  VehicleHistorySerializer(data = data)
                if not serializer.is_valid():
                    status_code = status.HTTP_400_BAD_REQUEST
                    response = {
                        'success': False,
                        'status code': status_code,
                        'message': list(serializer.errors.items())[0][1][0]
                    }
                else:
                    serializer.save()
                    response = {
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': "Successful checkin."
                    }
                return Response(response, status=status.HTTP_200_OK)
            else:
                # Handle the case where the condition is not met
                response = {
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': "You have already checked-in please checkout"
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': "Something went wrong, Please try again",
                'error': str(e)
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def check_extra_cost(history):
    from datetime import datetime, timezone

    in_time = history.in_time
    current_time = datetime.now(timezone.utc)
    parking_duration = abs((current_time - in_time).total_seconds()) / 60
    slot_duration = history.slot.time_duration
    extra_cost = 0
    total_cost = history.slot_cost
    if parking_duration > slot_duration:
        extra_cost = (parking_duration - slot_duration)*10
        total_cost += extra_cost
    return extra_cost , total_cost
@api_view(['GET'])
def parking_bill(request):
    try:
        history_id = request.GET.get('history_id')
        qr_id = request.GET.get('qr_id')
        if qr_id:
            try:
                zone = Zone.objects.get(qr_id=qr_id)
                history = History.objects.get(id = history_id,zone=zone)
            except Exception as e:
                response = {
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': "Madarchod kaha qr scan karuchu",
                    'error': str(e)
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            history = History.objects.get(id=history_id)

        extra_cost, total_cost = check_extra_cost(history)
        history.extra_cost = extra_cost
        history.total_cost = total_cost
        history.save()
        history = VehicleHistorySerializer(instance = history,many=False)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': "",
            'data':history.data
        }
        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        response = {
            'success': False,
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': "Something went wrong, Please try again",
            'error': str(e)
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
def vehicle_checkout(request):
    try:
        history_id = request.POST.get('history_id')
        history = History.objects.get(id=history_id)
        history.completed = True
        history.save()

        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': "Checkout Successful",
        }
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            'success': False,
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': "Something went wrong, Please try again",
            'error': str(e)
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
