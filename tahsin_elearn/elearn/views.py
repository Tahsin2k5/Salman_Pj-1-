from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .models import Categories
def index(request):
    categories = Categories.objects.all().order_by('-id')
    cat_data = {'data':categories}
    return render(request,'admin/cat.html',cat_data)
    
def insert(request):
    cat_name = request.POST.get('cat_name')
    if cat_name:
        if len(cat_name)<4:
            messages.success(request, 'the cat name field length minimum 3')

        elif Categories.objects.filter(name=cat_name).exists():
            messages.success(request, 'This value already exists.')
        else:

            cat_obj = Categories()
            cat_obj.name = cat_name

            cat_obj.save()
            messages.success(request, 'Category Inserted successfully')    
    else:
        messages.success(request, 'The field can not be empty')
       

    # cat_obj = Categories()
    # cat_obj.name = cat_name

    # cat_obj.save()
    # messages.success(request, 'Category Inserted successfully')
    return redirect('catadmin')

def edit_index(request,id):
    
    cat_obj = Categories.objects.get(id=id)
    single_cat = {'cat_data':cat_obj,'id':id}
    return render(request,'admin/cat_edit.html',single_cat)


def update(request):
    cat_name = request.POST.get('cat_name')
    cat_id = request.POST.get('cat_id')
    if cat_name:
        if len(cat_name)<4:
            messages.success(request, 'the cat name field length minimum 3')

        elif Categories.objects.filter(name=cat_name).exists():
            messages.success(request, 'This value already exists.')
        else:

            cat_obj = Categories.objects.get(id=cat_id)
            cat_obj.name = cat_name

            cat_obj.save()
            messages.success(request, 'Category Updated successfully')    
    else:
        messages.success(request, 'The field can not be empty')
    
    return redirect('catadmin')

def delete(request,id):
    
    cat_obj = Categories.objects.get(id=id)
    cat_obj.delete() #delete from table where id = id
    return redirect('catadmin')