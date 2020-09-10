from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from string import ascii_letters as strlet
from string import digits as strdig
from django.core.validators import EmailValidator as validate_email

def homepage(request):
    return render(request, 'users/index.html')

def login(request):
    if request.method == 'POST': # If user wants to log in
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'users/login.html', {'err':True})
    else:
        return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST': # If user wants to make an account
        ok_chars = tuple(strlet) + tuple(strdig) + tuple("_-")
        bad_username = False
        username_taken = False
        bad_firstname = False
        bad_lastname = False
        bad_password = False
        bad_email = False
        if request.POST['password'] != request.POST['ccpassword']:
            bad_password = True
        if len(request.POST['firstname']) > 30: # Even through the max length in Django 3.1 their names are not 20 characters at best
            bad_firstname = True
        if len(request.POST['lastname']) > 30:
            bad_lastname = True
        try:
            user = User.objects.get(username=request.POST['username'])
            username_taken = True
        except User.DoesNotExist:
            pass
        strings = {
            'user_err': None,
            'fnam_err': None,
            'lnam_err': None,
            'mail_err': None,
            'pass_err': None,
        }
        if not username_taken:
            for i in request.POST['username']:
                if not i in ok_chars:
                    bad_username = True
                    break
        bad_email = not validate_email(request.POST['email'])
        if bad_username:
            strings['user_err'] = 'Your username contains invalid characters.'
        elif username_taken:
            strings['user_err'] = 'Your username is already taken.'
        if bad_firstname:
            strings['fnam_err'] = 'Your first name contains invalid characters.'
        if bad_lastname:
            strings['lnam_err'] = 'Your last name contains invalid characters.'
        if bad_email:
            strings['mail_err'] = 'Your email does not exist or invalid.'
        if bad_password:
            strings['pass_err'] = 'Your passwords do not match.'
        if bad_username or username_taken or bad_firstname or bad_lastname or bad_email or bad_password:
            strings['has_err'] = True
            return render(request, 'users/register.html', strings)
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            auth.login(request, user)
            return redirect('homepage')
    else:
        return render(request, 'users/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')
    else:
        return redirect('register')
