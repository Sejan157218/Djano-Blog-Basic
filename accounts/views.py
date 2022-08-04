from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.


def signupPage(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('articles:articles-list')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})



def loginPage(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                 return redirect(request.POST.get('next'))
            else:
                return redirect('articles:articles-list')  
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    print('sdsd')
    if request.method=="POST":
        logout(request)
        return redirect('articles:articles-list')