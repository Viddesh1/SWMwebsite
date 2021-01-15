from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from . forms import SignUpForm, LoginForm, ListForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime
from . models import List
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    return render(request, "mywebsite_t/home.html")

def main(request):
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name()
        current_date_time = datetime.datetime.now() 
        your_list = List.objects.all()
        # group = Group.objects.get(name='User')
        gps = user.groups.all()
    return render(request, "mywebsite_t/main.html", {'full_name': full_name, 'current_date_time': current_date_time, 'your_list': your_list, 'groups':gps})

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation !! Sign In Successfully .')
            form = form.save()
            user = request.user
            # group = Group.objects.get(name='User')
            # user.groups.add(User)
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'mywebsite_t/signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/main/')
        else:
            form = LoginForm()
        return render(request, 'mywebsite_t/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/main/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ListForm(request.POST)
            if form.is_valid():
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                desc = form.cleaned_data['desc']
                pst = List(start_time=start_time, end_time=end_time, desc=desc)
                pst.save()
                messages.success(request, "Your Task Added Successfully")
                form = ListForm()
        else:
            form = ListForm()
        return render(request, 'mywebsite_t/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = List.objects.get(pk=id)
            form = ListForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Task Edited Successfully')
        else:
            pi = List.objects.get(pk=id)
            form = ListForm(instance=pi)
        return render(request, 'mywebsite_t/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = List.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Your Task Deleted Successfully')
        return HttpResponseRedirect('/main/')
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def contact(request):
    return render(request, 'mywebsite_t/contact.html')