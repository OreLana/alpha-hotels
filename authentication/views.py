from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth
from django.contrib import messages
from .decorators import unauthenticated_user
from booking_payment.models.booking import Booking


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
from authentication.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested for Alpha Hotels"
                    email_template_name = "authentication/password_reset/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': 'hotelms.herokuapp.com',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'hotelsalpha@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="authentication/password_reset/password_reset.html",
                  context={"password_reset_form": password_reset_form})


# Create your views here.
def home_index(request):
    return render(request, 'authentication/home_index.html', context=None)


@unauthenticated_user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            auth(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'authentication/register.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'authentication/register.html', {'form': form})


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            auth(request, user)
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('login')
    else:
        return redirect('login')


@login_required
def dashboard(request):
    user = request.user
    bookings = Booking.objects.filter(customer=user)
    print(bookings)
    context = {
        'user': user,
        "bookings":bookings
    }
    return render(request, 'authentication/dashboard.html', context)
