from django.urls import path
from . import views

app_name='melody'
urlpatterns=[
    path('index', views.MelodyIndexView.as_view(), name="index_view"),
    path('customerRegistration', views.MelodyCustomerRegistrationView.as_view(), name="customerRegistration_view"),
    path('productDashboard', views.MelodyProductDashboardView.as_view(), name="productDashboard_view"),
    path('customerDashboard', views.MelodyCustomerDashboardView.as_view(), name="customerDashboard_view"),
    path('songRegistration', views.MelodySongRegistrationView.as_view(), name="songRegistration_view"),
]