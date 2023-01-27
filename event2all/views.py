from rest_framework import viewsets, generics, filters
from event2all.models import User, Event, Quotation, Guest, ToDoList
from event2all.serializer import UserSerializer, EventSerializer, ListEventsByUserIdSerializer, QuotationSerializer, \
    GuestSerializer, ToDoListSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# User OK

class UsersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']

    permission_classes = (IsAuthenticated,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = (IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsAuthenticated,)


# Event

class EventViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = (IsAuthenticated,)


class ListEventsByUserId(generics.ListAPIView):
    """Listando os events pelo ID do User"""

    def get_queryset(self):
        queryset = Event.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListEventsByUserIdSerializer

    permission_classes = (IsAuthenticated,)


class ResponseExpectedExpenseByEventId(generics.ListAPIView):

    def get_queryset(self):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        return queryset

    serializer_class = QuotationSerializer

    permission_classes = (IsAuthenticated,)


# Quotation

class QuotationViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Guest"""
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    permission_classes = (IsAuthenticated,)


class ListQuotationByEventId(generics.ListAPIView):
    """Listando as Quotation pelo ID do Event"""

    def get_queryset(self):
        queryset = Quotation.objects.filter(event_id=self.kwargs['pk'])
        return queryset

    serializer_class = QuotationSerializer

    permission_classes = (IsAuthenticated,)
