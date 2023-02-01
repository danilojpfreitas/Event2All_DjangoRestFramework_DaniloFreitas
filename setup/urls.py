"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from event2all.views import UsersViewSet, EventViewSet, ListEventsByUserId, UserList, UserDetail, QuotationViewSet, ListQuotationByEventId, ResponseExpectedExpenseByEventId, ResponseActualExpenseByEventId, GuestViewSet, ListGuestByEventId, ToDoListViewSet, ListToDoListByEventId
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import RegisterView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Event2All - Django Rest Framework (Python)",
      default_version='v1',
      description="API da página Event2All",
      terms_of_service="#",
      contact=openapi.Contact(email="danilojpfreitas@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('user', UsersViewSet, basename='User')
router.register('event', EventViewSet, basename='Event')
router.register('quotation', QuotationViewSet, basename='Quotation')
router.register('guest', GuestViewSet, basename='Guest')
router.register('content', ToDoListViewSet, basename='ToDoList')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('controle-geral/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include(router.urls)),
#    path('users/', UserList.as_view()),
#    path('users/<int:pk>/', UserDetail.as_view()),
    path('auth/register/', RegisterView.as_view()),
    path('auth/', TokenObtainPairView.as_view()),
    path('event/byUserID/<int:UserID>/', ListEventsByUserId.as_view()),
    path('quotation/event/<int:EventID>/', ListQuotationByEventId.as_view()),
    path('event/allExpectedExpense/<int:EventID>/', ResponseExpectedExpenseByEventId.as_view()),
    path('event/allActualExpense/<int:EventID>/', ResponseActualExpenseByEventId.as_view()),
    path('guest/event/<int:EventID>/', ListGuestByEventId.as_view()),
    path('content/event/<int:EventID>/', ListToDoListByEventId.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]
