from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def do_login(request):
    """
    Execute the authentication login function on the request if username & password are valid.
    Args:
        request : The request object.
    """
    kwargs = {"error": ""}

    user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))

    if user is not None:
        login(request, user)
        return redirect('accounts')
    else:
        kwargs['error'] = "The information given is invalid"

    return render(request, 'index.html', kwargs)

def do_logout(request):
    """
    Execute the authentication logout function on the request
    Args:
        request : The request object.
    """
    logout(request)