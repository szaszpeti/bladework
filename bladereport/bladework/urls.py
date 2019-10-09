from django.urls import path, include
from . import views
from .views import (HomeView, TurbineCreateView, DamageCreateView, PhotoView,TurbineListView, TurbineDeleteView, TurbineDetailView,TurbineUpdateView)

app_name = 'bladework'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('getturbinedata', TurbineCreateView.as_view(), name='get_turbine_data'),
    path('getdamage', DamageCreateView.as_view(), name='damage'),
    path('takephoto', PhotoView.as_view(), name='take_photo'),
    path('turbinelist', TurbineListView.as_view(), name='turbine_list_view'),
    # path('list/', MeditaterListView.as_view(), name='meditater_list'),
    path('detail/<int:pk>/', TurbineDetailView.as_view(), name='turbine_detail'),
    path('delete/<int:pk>/', TurbineDeleteView.as_view(), name='turbine_delete'),
    path('edit/<int:pk>/', TurbineUpdateView.as_view(), name='turbine_edit'),
    # path('create/', MeditaterCreateView.as_view(), name='meditater_create'),
    path('find_index/', views.find_index, name='find_index'),
    path('photo_upload/', views.photo_upload, name='photo_upload'),
    # #path('find_index/', FindView.as_view(), name='find_index'),
    # path('email_formating/<int:pk>', views.email_view, name='email_formating'),
    # # path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    # path('upload_file/', views.upload_file, name='upload_file'),
    # path('export_to_excel_from_search/', views.export_to_excel_from_search, name='export_to_excel_from_search'),
    # path('meditater_statistic/', views.meditater_statistic, name='meditater_statistic'),
    # path('statistic_country/', views.statistic_country, name='statistic_country'),
    # path('statistic_profession/', views.statistic_profession, name='statistic_profession'),
    # path('statistic_gender/', views.statistic_gender, name='statistic_gender'),
    # path('statistic_born/', views.statistic_born, name='statistic_born'),
    # path('statistic_year/', views.statistic_year, name='statistic_year'),
]