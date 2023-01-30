from rest_framework import viewsets, generics, filters, status
from event2all.models import User, Event, Quotation, Guest, ToDoList
from event2all.serializer import UserSerializer, EventSerializer, ListEventsByUserIdSerializer, QuotationSerializer, \
    GuestSerializer, ToDoListSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


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

    def get_queryset(self):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        return queryset

    serializer_class = QuotationSerializer


# Quotation

class QuotationViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Guest"""
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class ListQuotationByEventId(generics.ListAPIView):
    """Listando as Quotation pelo ID do Event"""

    def get_queryset(self):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        return queryset

    serializer_class = QuotationSerializer
