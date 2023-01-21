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
          
     path('CashCompensationTypeChar', CashCompensationTypeCharView.as_view(),
         name='Cash Compensation Dashboard View'),

     path('ExistingTreeCount', ExistingTreeCount.as_view() , name = 'Exiting tree count'),

     path('typeofwastecount', WasteTypeCount.as_view() , name = 'Wastecount'),
     path('wastehandelingtype', WasteHandelingChart.as_view() , name = 'Wastecount'),

     path('Sourceofmaterial',MaterialSourceTypeCountChart.as_view() , name = 'Material'),
     path('Materilcondition',MaterialConditionChart.as_view() , name = 'Material'),
     path('Incidenttype',IncidenttypeCountchart.as_view() , name = 'Incident Type char'),




]