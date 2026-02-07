from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, DepartmentViewSet, EmployeesViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]