from django.urls import path
from Renyuan import views
from Renyuan.views import EditCeping, EditBeiCeping

urlpatterns = [
    path('query_beiceping/',views.query_beiceping),
    path('add_beiceping/', views.add_beiceping.as_view()),
    path('update_beiceping/', views.update_beiceping.as_view()),
    path('delete_a_beiceping/', views.delete_a_beiceping),
    path('delete_beicepings/', views.delete_beicepings),

    path('get_beicepings/',views.get_beicepings),
    path('get_cepings/',views.get_cepings),
    path('query_ceping/', views.query_ceping),
    path('add_ceping/', views.add_ceping.as_view()),
    path('update_ceping/', views.update_ceping.as_view()),
    path('delete_a_ceping', views.delete_a_ceping),
    path('delete_cepings/', views.delete_cepings),

    path('edit_cepings', EditCeping.as_view()),
    path('edit_beicepings', EditBeiCeping.as_view()),
]