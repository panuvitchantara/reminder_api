from django.urls import path
from .views import ReminderList, ReminderDetail, ShareReminderList

urlpatterns = [
    path('reminder/<int:pk>/',ReminderDetail.as_view(), name='detailcreate'),
    path('reminder/',ReminderList.as_view(),name='listcreate'),
    # path('share-reminder/',ShareReminderList.as_view(),name='share-list-create'),
]
