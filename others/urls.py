from django.urls import path
from others.views.account import Register1View, Register2View, LoginView, AccountView
from others.views import excel_in_out
from others.views.excel_in_out import Export_excel, Export_report_excel, Export_linereport

urlpatterns = [
    path('register1', Register1View.as_view()),
    path('register2', Register2View.as_view()),
    path('login', LoginView.as_view()),
    path('managers', AccountView.as_view()),
    path('import_ceping', excel_in_out.import_ceping),
    path('import_beiceping', excel_in_out.import_beiceping),
    path('import_department', excel_in_out.import_department),
    path('import_lingdaobanzi', excel_in_out.import_lingdaobanzi),
    path('export_excel', Export_excel.as_view()),
    path('export_excel1', Export_report_excel.as_view()),
    path('export_excel2', Export_linereport.as_view()),
]