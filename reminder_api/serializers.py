from rest_framework import serializers
from reminder_service.models import Reminder, ShareReminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('title','status','priority','description','created_date','due_date','creator','last_modified','editor')

# class ShareReminderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShareReminder
#         fields = ('editor','reminder')
