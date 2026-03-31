from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Kwa ajili ya kuonyesha feedback

def login_view(request):
    # 1. SECURITY: Kama mtumiaji ameshalogin, asiruhusiwe kuona ukurasa wa login
    if request.user.is_authenticated:
        return redirect('dashboard_index')

    if request.method == 'POST':
        # 2. VALIDATION: AuthenticationForm inashughulikia usalama wa CSRF na SQL Injection
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Hakikisha mtumiaji yupo na akaunti yake iko hai (Active)
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # 3. CORRECTION: Tunatumia 'dashboard_index' kama tulivyofafanua kwenye urls.py
                messages.success(request, f"Karibu tena {user.get_full_name() or user.username}!")
                return redirect('dashboard_index')
            else:
                messages.error(request, "Username au Password siyo sahihi.")
        else:
            messages.error(request, "Jaribio la kuingia halijafanikiwa. Tafadhali kagua taarifa zako.")
            
    else:
        form = AuthenticationForm()
        
    return render(request, 'login/login.html', {'form': form})