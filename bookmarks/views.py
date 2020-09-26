from django.shortcuts import redirect


def redirect_account(request):
    return redirect('login', permanent=True)
