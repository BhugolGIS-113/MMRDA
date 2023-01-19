from django.urls import path
from .views import *

urlpatterns = [
    # for social Monitoring
    path('PAPDashboardcategory', PAPCategoryDashboardView.as_view(),
         name='PAP Dashboard View'),
    path('IdentifiedPAPView', IdentifiedPAPDashboardView.as_view(),
         name='PAP Dashboard View'),
    path('LabourcampFaciliteis<str:labourCampName>',
         LabourCampFacilitiesDashboardView.as_view(), name='labour Dashboard View'),
    path('RehabilitatedPAP', RehabilitatedPAPDashboardView.as_view(),
         name='Rehabilated Dashboard View'),





]
