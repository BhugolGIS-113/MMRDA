from django.urls import path
from .views import ( PapView , constructionSiteView , papupdateView ,PapListView ,LabourCampDetailsView  , PAPmanagmentAPI, RehabilitationView,
 ConstructionSitemanagment,LabourCampManagmentAPI,ConstructionSiteListView)

urlpatterns = [
    path ('pap' , PapView.as_view() , name = "project affected Person "),
    path ('pap/<int:id>' , papupdateView.as_view() , name = "project affected Person "),
    path ('paplist' , PapListView.as_view() , name = "project affected Person List "),

    path('rehabitation' , RehabilitationView.as_view() , name = "rehabitation"),

    path ('constructionsite' , constructionSiteView.as_view() , name = "constructionSiteView"),
    path ('constructionsiteList' , ConstructionSiteListView.as_view() , name = "ConstructionSiteListView"),

    path ('labourcamp' , LabourCampDetailsView.as_view() , name = "LabourCampDetailsView"),

    path('papmanagment/<str:packages>', PAPmanagmentAPI.as_view(), name="PAPmanagmentAPI"),
    path('constructionsitemanagement/<str:packages>', ConstructionSitemanagment.as_view(), name="ConstructionSitemanagment"),
    path('LabourCamp/<str:packages>', LabourCampManagmentAPI.as_view(), name="LabourCampManagmentAPI")

]