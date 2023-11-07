from django.shortcuts import render

from elearn.models import Categories
from course.models import courses
from itertools import zip_longest

def index(req):
    data = Categories.objects.all()
    data2 = courses.objects.order_by('-pk')[:4]
    data3 = courses.objects.filter(cat_id_id=1).order_by('-pk')[:4]
    data4 = courses.objects.order_by('-discount')[:4]
    length = len(data3)
    length = length !=0
    print("asdasdasdasdasdasdasdasdasdasdadasdasdadasdasdasdd",length)
    
    discount_fee_list = []
    discount_fee_list2 = []
    discount_fee_list3 = []
    for i,j,k in zip(data2,data3,data4):
        print(i)
        print("helo",i.fee)
        print("heellwdadasd",i.discount)
        discount_fee = i.fee - ((i.fee*i.discount)/100)
        discount_fee2 = j.fee - ((j.fee*j.discount)/100)
        discount_fee3 = k.fee - ((k.fee*k.discount)/100)
        discount_fee_list.append(discount_fee)
        discount_fee_list2.append(discount_fee2)
        discount_fee_list3.append(discount_fee3)
    # data = Categories.objects.all()
    zipped_data = zip_longest(data2, discount_fee_list)
    zipped_data2 = zip_longest(data3, discount_fee_list2)
    zipped_data3 = zip_longest(data4, discount_fee_list3)
    cat = {'all_cat':data,'data_2':zipped_data,'data_3':zipped_data2,'size1':length,'data4':zipped_data3}
    return render(req,'user/home.html',cat)

def product_list(req,id):
    course_obj = courses.objects.filter(cat_id_id=id)
    discount_fee_list = []
    for i in course_obj:
        print(i)
        print("helo",i.fee)
        print("heellwdadasd",i.discount)
        discount_fee = i.fee - ((i.fee*i.discount)/100)
        discount_fee_list.append(discount_fee)
    # data = Categories.objects.all()
    zipped_data = zip_longest(course_obj, discount_fee_list)

    course_obj1 = {'all_course':zipped_data}
    return render(req,'user/product_list.html',course_obj1)

# Create your views here.
def details(req,id):
    course_obj = courses.objects.get(id=id)
    discount_fee = course_obj.fee - ((course_obj.fee*course_obj.discount)/100)
    course_obj1 = {'all_course':course_obj,"discount":discount_fee}
   
    return render(req,'user/detail.html',course_obj1)

def cart(req):
   
    return render(req,'user/cart.html')