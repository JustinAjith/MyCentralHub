from rest_framework import viewsets
from apps.job_application.models import Company
from apps.job_application.serializers import CompanySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(methods=['get'], detail=True, url_path='update-applyed')
    def updateApplyedStatus(self, request, pk=None):
        company = self.get_object()
        company.is_apply = True
        company.save()
        return Response({'message': 'Job applyed successfuly!'}, status=200)