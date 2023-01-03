
from django.urls import path
from .views import ( AirView , AirListView, WaterView , waterListView, NoiseView ,NoiseListView,
TreeManagementView, TereeManagementView,WasteTreatmentsView  ,MaterialSourcingView)
from .views import *

urlpatterns = [
# path('envmonitoring' , EnvMonitoringView.as_view() , name = 'envmonitoring'),
    path('air' , AirView.as_view() , name = 'Air Details'),
    path('airList', AirListView.as_view() , name = 'ListAirView'),

    path('water' , WaterView.as_view() , name = 'water Details'),
    path('waterList' , waterListView.as_view() , name = 'water Details'),

    path('noise' , NoiseView.as_view() , name = "Noise Details"),
    path('noiseList' ,NoiseListView.as_view() , name = "Noise"),

    # path('envview' , envMonitoringView.as_view() , name = 'EnvQualityMonitoring'),
    path('tree' , TreeManagementView.as_view() , name = "Tree Management"),
    path('treeView' , TereeManagementView.as_view() , name = "Tree Management list"),


    path('waste' , WasteTreatmentsView.as_view() , name = "Waste Management"),
    path('materialsourcing' , MaterialSourcingView.as_view() , name = "Material Sourcing") ,
    
     path('treemanagement/<str:packages>' , TreemanagmentAPI.as_view() , name = "TreemanagmentAPI"),
    path('Airmanagement/<str:packages>' , AirAPI.as_view() , name = "AirAPI"),
    path('Noisemanagement/<str:packages>' , NoiseAPI.as_view() , name = "NoiseAPI"),
    path('wastemanagement/<str:packages>' , WasteTreatmentsAPI.as_view() , name = "NoiseAPI"),
    path('materialmanagement/<str:packages>' , MaterialSourcingAPI.as_view() , name = "MaterialSourcingAPI"),
    path('watermanagement/<str:packages>' , WatermanagmentAPI.as_view() , name = "WatermanagmentAPI"),
 ]