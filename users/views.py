from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForms


# Create your views here.
def register(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST) 
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request,f'Account is created for {username}')
            return redirect('blog')

    else:
        forms = UserRegisterForm() 
    return render(request,'users/register.html',{'forms': forms})


@login_required
def profile(request):
    if request.method == 'POST':
       u_form = UserUpdateForm(request.POST,instance=request.user)
       p_form = ProfileUpdateForms(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request,f'your account has been updated')
    else:
       u_form = UserUpdateForm(instance=request.user)
       p_form = ProfileUpdateForms(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form,
        
    }
    return render(request,'users/profile.html',context)


