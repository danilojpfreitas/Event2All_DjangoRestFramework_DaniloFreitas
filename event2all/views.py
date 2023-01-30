from rest_framework import viewsets, generics, filters, status, permissions
from event2all.models import User, Event, Quotation, Guest, ToDoList
from event2all.serializer import UserSerializer, EventSerializer, ListEventsByUserIdSerializer, QuotationSerializer, \
    GuestSerializer, ToDoListSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView


# User OK

class UsersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            id = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            response['Location'] = request.build_absolute_uri() + id
            return response


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Event

class EventViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ListEventsByUserId(generics.ListAPIView):
    """Listando os events pelo ID do User"""

    def get_queryset(self):
        queryset = Event.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListEventsByUserIdSerializer


class ResponseExpectedExpenseByEventId(generics.ListAPIView):
    """Retornando a soma do ExpectedExpense pelo EventId"""
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def list(self, request, *args, **kwargs):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        response = super().list(request, *args, **kwargs)
        response.data['sum'] = queryset.aggregate(sum=Sum('expected_expense'))['sum']
        return response


class ResponseActualExpenseByEventId(generics.ListAPIView):
    """Retornando a soma do ActualExpense pelo EventId"""
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def list(self, request, *args, **kwargs):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        response = super().list(request, *args, **kwargs)
        response.data['sum'] = queryset.aggregate(sum=Sum('actual_expense'))['sum']
        return response


# Quotation

class QuotationViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Quotation"""
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class ListQuotationByEventId(generics.ListAPIView):
    """Listando as Quotation pelo ID do Event"""
    serializer_class = QuotationSerializer

    def get_queryset(self):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        return queryset


# Guest


class GuestViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Guest"""
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    http_method_names = ['put', 'delete', 'post']


class ListGuestByEventId(generics.ListAPIView):
    """Listando os Guest pelo ID do Event"""
    serializer_class = GuestSerializer

    def get_queryset(self):
        queryset = Guest.objects.filter(event_id=self.kwargs['pk'])
        return queryset


"""class PostGuestByEventId(APIView):
#    Post Guest pelo ID do Event

    def post(self, request, pk):
        guest = {
            "name": request.data.get('name'),
            "contact": request.data.get('contact'),
            "invite": request.data.get('invite'),
            "isConfirmed": request.data.get('isConfirmed'),
            "event_id": request.query_params.get('event_id')
        }
        serializer = GuestSerializer(data=guest)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


# ToDoList


class ToDoListViewSet(viewsets.ModelViewSet):
    """Exibindo todos os ToDoList"""
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    http_method_names = ['put', 'delete', 'post']


class ListToDoListByEventId(generics.ListAPIView):
    """Listando os Guest pelo ID do Event"""
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        queryset = ToDoList.objects.filter(event_id=self.kwargs['pk'])
        return queryset





