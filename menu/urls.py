from django.urls import path
from . import views

urlpatterns = [
    path('', views.qr_code_view, name='qr_code'),
    path('select_table/', views.select_table, name='select_table'),
    path('menu/<int:table_no>/', views.show_menu, name='show_menu'),
    path('kitchen/', views.kitchen_display, name='kitchen_display'),
]