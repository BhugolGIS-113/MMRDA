from django.urls import path
from .views import TraningView ,TrainingListView, PhotographsView , photographsListView , updatephotographview , TrainingupdateView



urlpatterns = [
    path('traning' , TraningView.as_view() , name = 'traning'),
    path('traningList' , TrainingListView.as_view() , name = 'traning list'),
    path('traningUpdate/<int:pk>' , TrainingupdateView.as_view() , name = 'traning update'),

    
    path('photographs' , PhotographsView.as_view() , name = 'photographs') ,
    path('photographsList' , photographsListView.as_view() , name = 'photographs list '),
    path('PhotographsViewupdate/<int:pk>' , updatephotographview.as_view() , name = 'photograph update')

]