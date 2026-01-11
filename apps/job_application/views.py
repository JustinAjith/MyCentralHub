from rest_framework import viewsets
from apps.job_application.models import Company
from apps.job_application.serializers import CompanySerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer