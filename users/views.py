from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate
from .forms import RegistrationForm, UpdateForm
from django.contrib import messages






def landinPage(request):
    return render(request, 'users/landingpage.html')





def signUp(request):
    page = 'signup'
    user = get_user_model()
    
    if request.user.is_authenticated:
        return redirect('books:dashboard')
    
    # If the requst is a POST method, present the form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        # If the form is valid, then process and save the user
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"User Created Successfully...")
            return redirect('users:more_about')
        
        else:
            messages.error(request, f"Something Went Wrong, Please try again...")
    
    else:
        form = RegistrationForm()
        
    context = {
        'page': page,
        #'form': form
    }
    
    return render(request, 'users/signup.html', context)




def signIn(request):
    page = 'signin'
    User = get_user_model()
    
    if request.user.is_authenticated:
        return redirect('books:dashboard')
    
    # If the requst is a POST method, present the form
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        
        except:
            messages.error(request, f"Bad Request, Check Your details and try again")
            
        user = authenticate(request, email=email, password=password) 
        
        if user is not None:
            login(request, user)
            messages.success(request, f"You've been Signed in")
            return redirect('books:dashboard')
            
        else:
            messages.error(request, f"Please, Confirm You typed in the correct details...")       
    
    context = {'page': page}
    return render(request, 'users/signin.html', context)




def signOut(request):
    page = 'signout'
    
    logout(request)
    
    context = {'page': page}
    return render(request, 'users/signout.html', context)