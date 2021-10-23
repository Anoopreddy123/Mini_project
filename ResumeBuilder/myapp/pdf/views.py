from django.shortcuts import render
from .models import Profile

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("Name","")
        phone = request.POST.get("Phone","")
        Email = request.POST.get("Email","")
        School = request.POST.get("School","")
        degree = request.POST.get("degree","")
        university = request.POST.get("university","")
        skills = request.POST.get("skills","")
        objective = request.POST.get("objective","")
        city = request.POST.get("city","")
        school_cgpa = request.POST.get("school_cgpa","")
        university_cgpa = request.POST.get("school_cgpa","")
        degree_cgpa = request.POST.get("school_cgpa","")
        project = request.POST.get("projec","")
        profile = Profile(school_cgpa=school_cgpa,degree_cgpa=degree_cgpa,university_cgpa=university_cgpa,name=name,phone = phone,Email=Email,School = School,degree = degree,university = university,skills = skills,objective = objective,city = city,project = project)
        profile.save()
    return render(request ,"form.html")


def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    return render(request,"resume.html",{'user_profile':user_profile})