from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader, response

import pdfkit  
import io

def accept(request):
    if request.method == "POST":
        name = request.POST.get("Name","")
        phone = request.POST.get("Phone","")
        Email = request.POST.get("Email","")
        School = request.POST.get("School","")
        degree = request.POST.get("degree","")
        university = request.POST.get("university","")
        skill = request.POST.get("skills","")
        objective = request.POST.get("objective","")
        city = request.POST.get("city","")
        school_cgpa = request.POST.get("school_cgpa","")
        university_cgpa = request.POST.get("school_cgpa","")
        degree_cgpa = request.POST.get("school_cgpa","")
        project = request.POST.get("project","")
        profile = Profile(school_cgpa=school_cgpa,degree_cgpa=degree_cgpa,university_cgpa=university_cgpa,name=name,phone = phone,Email=Email,School = School,degree = degree,university = university,skill = skill,objective = objective,city = city,project = project)
        profile.save()
    return render(request ,"form.html")


def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    skill = Profile.objects.values_list('skill')
    return render(request,"resume.html",{'user_profile':user_profile,'skill':skill[id-1]})


def list(request):
    profile = Profile.objects.all()
    return render(request,"list.html",{'profile':profile})
