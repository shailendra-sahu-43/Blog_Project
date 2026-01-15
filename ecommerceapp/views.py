from django.shortcuts import render ,redirect
from ecommerceapp.models import uuser , Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    dt = uuser.objects.all()
    context = {
        'dt': dt
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        cont = Contact(name = name , email = email , website=website , message = message)
        cont.save()
        return render(request,'contact_success.html')
    return render(request,'contact.html')

def single_blog_page(request,id):
    mydata = uuser.objects.all().get(id = id)
    alldata = uuser.objects.order_by('-id')[:5]
    context = {
        'mydata':mydata,
        'alldata':alldata
    }
    return render(request, 'single_blog_page.html',context)

@login_required
def post_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')
        img = request.FILES.get('img')
        data = uuser(title = title,date = date, description = description,img = img)
        data.save()
        return render(request,'sucess.html')
    return render(request,'post_blog.html')


#register user form
from django.contrib.auth import login
from .form import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


# this is the alb settings 
from django.http import HttpResponse

def health(request):
    return HttpResponse("ok", status=200)


