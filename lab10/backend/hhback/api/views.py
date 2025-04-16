from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
from django.shortcuts import get_object_or_404

class CompanyListView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class VacancyListView(APIView):
#     def get(self, request):
#         vacancies = Vacancy.objects.all()
#         serializer = VacancySerializer(vacancies, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = VacancySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def get_vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CompanyDetailsByIdView(APIView):
    def get(self, request, id: int):
        company = get_object_or_404(Company, pk=id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

# class CompanyVacancyListlView(APIView):
#     def get(self, request, id: int):
#         company = get_object_or_404(Company, pk=id)
#         serializer = VacancySerializer(company.vacancies.all(), many=True)
#         return Response(serializer.data)    

@api_view(['GET'])
def get_company_vacancies(request, id):
    company = get_object_or_404(Company, pk=id)
    vacancies = company.vacancies.all()
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
    
class VacancyDetailByIdView(APIView):
    def get(self, request, id: int):
        vacancy = get_object_or_404(Vacancy, pk=id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    
# class VacancyTopView(APIView):
#     def get(self, request):
#         vacancies = Vacancy.objects.all().order_by("-salary")[:10]
#         serializer = VacancySerializer(vacancies, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
def get_vacancy_top(request):
    vacancies = Vacancy.objects.all().order_by("-salary")[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
