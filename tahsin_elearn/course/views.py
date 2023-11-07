from django.shortcuts import render,HttpResponse,redirect
from elearn.models import Categories
from .models import courses

# Create your views here.

def index(request):
    all_cats = Categories.objects.all().order_by('-id')
    all_courses = courses.objects.all().order_by('-id')
    data = {'data':all_cats,'course_data':all_courses}
    return render(request,'admin/course_admin.html',data)


def insert(request):
    cat_id  = request.POST.get('cat_id')
    course_name  = request.POST.get('course_name')
    desciption  = request.POST.get('desciption')
    course_fee  = request.POST.get('course_fee')
    course_discount  = request.POST.get('course_discount')
    module  = request.POST.get('module')
    course_image = request.FILES.get('course_image')

    category = Categories.objects.get(pk=cat_id)
    course_obj = courses()
    course_obj.cat_id = category
    course_obj.name = course_name
    course_obj.description = desciption
    course_obj.fee = course_fee
    course_obj.discount = course_discount
    course_obj.module = module
    course_obj.image = course_image

    course_obj.save()

    return redirect('courseadmin')
    # return render(request,'admin/course_admin.html',data)
