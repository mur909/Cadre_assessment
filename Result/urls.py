from django.urls import path
from .views.teststatus import CepingView, LoadDep
from .views.result import XygbresultView, JggbresultView, ZsdwgbresultView, XybzresultView, ZsdwbzresultView,\
    Result_all, Gb_of_all, Bz_of_all
from .views.result_view import GanbuView, BanziView, GbSearchView, BzSearchView, LineView
from .views.result_report import Personal_report, Banzi_report

urlpatterns = [
    path('loaddep', LoadDep.as_view()),
    path('status', CepingView.as_view()),
    path('xygb', XygbresultView.as_view()),
    path('jggb', JggbresultView.as_view()),
    path('zsdwgb', ZsdwgbresultView.as_view()),
    path('xybz', XybzresultView.as_view()),
    path('zsdwbz', ZsdwbzresultView.as_view()),
    path('result_all', Result_all.as_view()),
    path('gbofall', Gb_of_all.as_view()),
    path('bzofall', Bz_of_all.as_view()),
    path('gb_condition', GanbuView.as_view()),
    path('bz_condition', BanziView.as_view()),
    path('gbsearch', GbSearchView.as_view()),
    path('bzsearch', BzSearchView.as_view()),
    path('personal_report', Personal_report.as_view()),
    path('banzi_report', Banzi_report.as_view()),
    path('line', LineView.as_view())
]