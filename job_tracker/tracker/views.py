from urllib import request
from .models import Company
from django.http import JsonResponse
from .serializers import CompanySerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def company(request):

    company=Company.objects.all()
    serializer=CompanySerializer(company, many=True)
    return JsonResponse(serializer.data, safe=False)



def company_detail(request, company_id):
    company=Company.objects.get(id=company_id)

    serializer=CompanySerializer(company)
    return JsonResponse(serializer.data, safe=False)