from django.shortcuts import render, redirect
from users.forms import CustomRegistration

# Creates account registration form and renders register page
def register(request):
    if request.method == 'POST': # If the request method is POST, it will add input data to the database
        registration = CustomRegistration(request.POST)
        if registration.is_valid(): # If the content of the post has valid values for each field, the form will be saved to the database and redirect user back to home page
            registration.save()
            return redirect('home')
    else: # If the request method is GET, it will render the account registration page again
        registration = CustomRegistration()
    return render(request, 'newaccount.html', {'registration': registration})
