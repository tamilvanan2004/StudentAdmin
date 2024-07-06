from django.contrib import admin
from .models import *
# Register your models here.
class studentsAdmin(admin.ModelAdmin):
    list_display = ['Name','Course','Confirm','Bcode','Email','Phone','TimeSlot','mentor']
    
class mentorAdmin(admin.ModelAdmin):
    list_display = ['Name','Mentor']
admin.site.register(Students,studentsAdmin)
admin.site.register(Mentor,mentorAdmin)

