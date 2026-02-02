from urllib import request
from django.shortcuts import render
from .models import Company
from django.http import JsonResponse
# Create your views here.

def company(request):
    company=Company.objects.all()

    data={
        'company': list(company.values())
    }

    return JsonResponse(data)


def company_detail(request, company_id):
    company=Company.objects.get(id=company_id)

    data={
        'company': {
            'company_name': company.company_name,
            'company_website': company.company_website,
            'company_location': company.company_location,
        }
    }

    return JsonResponse(data)