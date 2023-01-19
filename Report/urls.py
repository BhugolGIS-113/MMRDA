from django.urls import path
from .views import *

urlpatterns = [
    # for social Monitoring
    path('labourcampreportpackage/<str:packages>/<str:labourCampName>',
         LabourcampReportPackageView.as_view(), name='Labourcamp Report View package'),
    path('labourcampreportquarter/<str:quarter>/<int:year>/<str:labourCampName>',
         LabourCampReportQuarterView.as_view(), name='Labourcamp Report View quarter'),

    path('constructioncampreportPackage/<str:packages>/<str:constructionSiteName>',
         ConstructionCampReportPackageView.as_view(), name='ConstructionSite Report'),
    path('constructioncampreportQuarter/<str:packages>/<str:constructionSiteName>',
         ConstructionCampReportQuarterView.as_view(), name='ConstructionSite Report'),

    path('papreportpackage/<str:packages>',
         PAPReportPackageView.as_view(), name='PAP Report package'),
    path('papreportquarter/<str:quarter>/<int:year>',
         PAPReportQuarterView.as_view(), name='PAP Report quarter'),

    path('Rehabilationreportpackage/<str:packages>',
         RehabilitationReportPackageView.as_view(), name=' Rehabilitation Report package'),
    path('Rehabilationreportquarter/<str:quarter>/<int:year>',
         RehabilitationReportQuarterView.as_view(), name=' Rehabilitation Report quarter'),

    # Env Monitoring Routes

    path('airReportpackage/<str:packages>',
         AirReportPackageView.as_view(), name='AirReport Package View'),
    path('airReportquarter/<str:month>/<int:year>',
          AirReportQuarterView.as_view(), name='AirReport Package View'),

    path('noisereportpackage/<str:packages>',
         NoiseReportpackageView.as_view(), name='Noisereport Package View'),
    path('noisereportquarter/<str:quarter>/<int:year>',
         NoiseReportQuarterView.as_view(), name='Noisereport Package View'),

    path('waterReportpackage/<str:packages>',
         waterReportPackageView.as_view(), name='Water Report Package View'),
    path('waterReportquarter/<str:quarter>/<int:year>',
         waterReportQuarterView.as_view(), name='Water Report Package View'),

    path('wastetreatmentpackage/<str:package>',
         WasteTreatmentsPackageView.as_view(), name='Water Report Package View'),
    path('wastetreatmentquarter/<str:quarter>/<int:year>',
         WasteTreatmentsQuarterView.as_view(), name='Water Report Quarter View'),

    path('materialmanagementpackage/<str:packages>',
         MaterialManagementReporetpackageView.as_view(), name='Material Management Package'),
    path('materialmanagementquarter/<str:quarter>/<int:year>',
         MaterialManagementReporetQuarterView.as_view(), name='Material Management Quarter'),

     path('TreeMangementReportPackage/<str:packages>',
         TreeMangementReportPackage.as_view(), name='Tree Management Package'),
     path('TreeManagementReportQuarterView/<str:quarter>/<int:year>',
         TreeManagementReportQuarterView.as_view(), name='Tree Management Quarter')
]
