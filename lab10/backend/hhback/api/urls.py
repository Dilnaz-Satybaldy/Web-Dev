from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name = 'company-list-create'),
    path('vacancies/', views.get_vacancy_list, name = 'vacancy-list-create'),
    path('companies/<int:id>/', views.CompanyDetailsByIdView.as_view(), name = 'company-by-id'),
    path('companies/<int:id>/vacancies/', views.get_company_vacancies, name = 'company-vacancy-list'),
    path('vacancies/<int:id>/', views.VacancyDetailByIdView.as_view(), name = 'vacancy-by-id'),
    path('vacancies/top_ten/', views.get_vacancy_top, name = 'vacancies-top-ten')

]