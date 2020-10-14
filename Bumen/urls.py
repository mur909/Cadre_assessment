from django.urls import path
from Bumen.views import GenerateBz, ReturnInfo, EditBz, GetDepartment, AddDepartment, EditDepartment,DeleteDepartment

urlpatterns = [
    path('return_bz', ReturnInfo.as_view()),
    path('generate_bz', GenerateBz.as_view()),
    path('edit_bz', EditBz.as_view()),
    path('get_department/',GetDepartment.as_view()),
    path('add_department/', AddDepartment.as_view()),
    path('edit_department/',EditDepartment.as_view()),
    path('delete_department/', DeleteDepartment.as_view())
]