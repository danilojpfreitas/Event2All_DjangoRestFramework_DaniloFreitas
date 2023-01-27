from rest_framework import viewsets, generics
from event2all.models import User, Event
from event2all.serializer import UserSerializer, EventSerializer, ListEventsByUserIdSerializer
from rest_framework.permissions import IsAuthenticated


class UsersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

