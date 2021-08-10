from django.shortcuts import render
from .models import post
from django.core.paginator import Paginator
# Create your views here.
def listed_post(request):
    all_post =post.objects.all().order_by('id')
    paginator =Paginator(all_post,3)
    no_of_pages = paginator.num_pages
    no_of_pages = [nu for nu in range(1,no_of_pages+1)]
    # print(no_of_pages,"no_of_page..")
    page_number =request.GET.get('page')
    # print(page_number)
    page_obj =paginator.get_page(page_number)
    # print(page_obj.paginator.count,"count..")
    return render(request,"blo/home.html",{'all_post':page_obj,'no_of_pages':no_of_pages})