from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship

def home(request):
    return render(request,'home.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)
from django.shortcuts import render, get_object_or_404
from .models import Blogs

def blog_detail(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    context = {'post': post}
    return render(request, 'blog_detail.html', context)

 
def about(request):
    return render(request,'about.html')


def internshipdetails(request):

    if not request.user.is_authenticated:
        messages.warning(request,"Please login to access this page")
        return redirect("/auth/login/")

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fcollege=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')

# converting to upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper()

        # 
        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request,"Your Details are Stored Already")
            return redirect("/internshipdetails")
        



        query=Internship(fullname=fname,usn=fusn,email=femail,college_name=fcollege,offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
        query.save()

        messages.success(request,"Form is Submitted Successful!")
        return redirect('/internshipdetails')

    return render(request,'intern.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')

# views.py

from django.shortcuts import render

def skills_page(request):
    # Define skills data
    skills = {
        'languages': ['PHP', 'HTML', 'CSS', 'JavaScript', 'Java', 'Python', 'SQL'],
        'frameworks': ['Django'],   
        'concepts': ['Object Oriented Programming', 'Data Structures',  'SDLC'],
        'other': ['Git', 'DevOps']
    }
    
    return render(request, 'skills.html', {'skills': skills})

def achievements_page(request):
    achievements = [
        {
            'title': 'Secured the third prize in an international hackathon held at Barshi Solapur.',
            'image': 'barshi_solapur.png',
        },
        {
            'title': 'Successfully navigated through two rounds of CodeVita, a coding competition organized by TCS  securing a global rank of  815  in TCS Codevita Season 11 and for showcasing exceptional coding skills.',
            'image': 'codevita.png',
        },
        {
            'title': '4-star rating on Hackerrank',
            'image': 'Hackerrank.png',
        },
    ]
    return render(request, 'achievements.html', {'achievements': achievements})

def internship(request):

    return render(request, 'internship.html')
from django.shortcuts import render

def certificates(request):
    certificates = [
        {
            'title': 'Python programming (Udemy): An in-depth exploration of fundamental and advanced Python programming concepts.',
            'image': 'python_programming.png',
        },
        {
            'title': 'Web-Development (LeadSoft IT Solution): Training covering frontend technologies (HTML, CSS, JavaScript) to enhance website development skills.',
            'image': 'web_development.png',
        },
    ]
    return render(request, 'certificates.html', {'certificates': certificates})
