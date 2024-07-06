from django.shortcuts import render
from app.models import *
from django.http import JsonResponse

# Create your views here.

def  abc(request):
    return render(request,'login.html')

def xyz(request):
    studentData = Students.objects.filter(status=0)  
    mentor = Mentor.objects.all()
    return render(request, 'admin.html', {'students': studentData,'mentors':mentor})

def registers(request):
    if request.method == "POST":
        name = request.POST.get('username')
        mentor = request.POST.get('mentor')
        timeslot = request.POST.get('time_slot')

        abc = Mentor(Name=name,Mentor= mentor,TimeSlot=timeslot)
        abc.save()
    
    return render(request,"register.html")

def home(request):
    return render(request,"home.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        course = request.POST.get('course')
        confirm = request.POST.get('password_confirm')
        bcode = request.POST.get('b_code')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        time_slot = request.POST.get('time_slot')

        abc = Students(Name=name,Course= course,Confirm=confirm,Bcode=bcode,Email=email,Phone=phone,TimeSlot=time_slot)
        abc.save()
    
    return render(request,"register.html")




from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json

def save_booking(request):
    print('Started')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            data = json.loads(request.body)
            student_id = data.get('stdId')
            mentor_name = data.get('mentorName')
            mentor = data.get('mentor')
            
            student = Students.objects.get(id=student_id)
            student.mentor = mentor_name
            print(mentor)
            print(mentor_name)
            student.save()
            
            return JsonResponse({'message': 'Booking saved successfully'})
        
        except Students.DoesNotExist:
            print(f'Student with id {student_id} does not exist')
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        print('Invalid request')
        return JsonResponse({'error': 'Invalid request'}, status=400)


