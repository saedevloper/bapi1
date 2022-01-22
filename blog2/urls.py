from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [

    url(r'^gear/all/$', views.AllGearAPIView.as_view(), name='all_gear'),
    url(r'^gear/submit/$', views.SubmitGearAPIView.as_view(), name='submit_gear'),
    url(r'^gear/delete/$', views.DeleteGearAPIView.as_view(), name='delete_gear'),

]
