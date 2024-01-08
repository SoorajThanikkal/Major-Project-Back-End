from django.urls import path
from .views import ClientRegisterView,FreelanceRegisterView,UserLoginView,FreelancerLoginView,ClientProfileView


urlpatterns = [
    path('client-register/',ClientRegisterView.as_view(),name = 'Cregister'),
    path('freelancer-register/',FreelanceRegisterView.as_view(),name = 'Fregister'),
    path('login/',UserLoginView.as_view(),name = 'Ulogin'),
    # path('freelance-login/',FreelancerLoginView.as_view(),name = 'Flogin'),
    path('clients-create/', ClientProfileView.as_view(), name='client-create'),
]
