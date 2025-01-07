from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, GroupViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
