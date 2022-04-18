from django.shortcuts import render
from rest_framework import generics
from reminder_service.models import Reminder, ShareReminder
from .serializers import ReminderSerializer, ShareReminderSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Create your views here.

class ReminderUserWritePermission(BasePermission):
    message = 'You are not allowed to see this.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.creator == request.user


class ReminderList(generics.ListCreateAPIView, ReminderUserWritePermission):
    serializer_class = ReminderSerializer
    permission_classes = [ReminderUserWritePermission]
    
    def get_queryset(self):
        current_user = self.request.user
        return Reminder.objects.filter(creator=current_user)


class ReminderDetail(generics.RetrieveUpdateDestroyAPIView, ReminderUserWritePermission):
    permission_classes = [ReminderUserWritePermission]
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


# class ShareReminderList(generics.ListCreateAPIView):
#     serializer_class = ShareReminderSerializer
#     queryset = ShareReminder.objects.all()
    
#     # def get_queryset(self):
#         # current_user = self.request.user
#         # return ShareReminder.objects.filter(editor=current_user)

# class ShareReminderDetail(generics.RetrieveUpdateAPIView, ReminderUserWritePermission):
#     # permission_classes = [ReminderUserWritePermission]
#     # serializer_class = ShareReminderSerializer
#     # reminder = Reminder.objects.get(Reminder.id)

#     pass

