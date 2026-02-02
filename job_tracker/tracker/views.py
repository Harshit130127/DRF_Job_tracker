from urllib import request
from .models import Company
from rest_framework.response import Response
from .serializers import CompanySerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def company(request):

    company=Company.objects.all()
    serializer=CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def company_detail(request, company_id):
    company=Company.objects.get(id=company_id)

    serializer=CompanySerializer(company)
    return Response(serializer.data)