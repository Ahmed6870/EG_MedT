from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from userauths.models import User,Profile
from pages.forms import UserCreationForms
from userauths.forms import UserRegisterForm , Login_Form
from pages.models import *
# Create your views here.

def RegisterView(request):
    # if request.user.is_authenticated:
      #   messages.warning(request, f"You are already logged in")
      #   return redirect("index")
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('userauths:user_login')
            full_name = form.cleaned_data.get("full_name")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                profile = Profile.objects.get(user=request.user)
                profile.full_name = full_name
                profile.phone = phone
                profile.save()
                return redirect("index")
            else:
                messages.error(request, 'تأكد من أن البيانات يتم إدخالها بشكل صحيح كما هو مطلوب ثم أعد المحاولة')
                return redirect('userauths:signup')
    else:
        form = UserRegisterForm()
        context = {
        'form':form
        }
        return render(request, "registration/signup.html", context)


# def loginViewTemp(request):
#   if request.user.is_authenticated:
#     messages.warning(request,"سجلت الدخول بالفعل")
#     return redirect("index")
#   if request.method == "POST":
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     try:
#       user_query = user.objects.get(email=email)
#       user_auth = authenticate(request,email=email,password=password)
#       if user_query is not None:
#         login(request,user_auth)
#         messages.success(request,"تم تسجيل الدخول")
#         next_url =request.GET.get("next","index")
#         return redirect(next_url)
#       else:
#         messages.error(request,"يبدو أن البريد الإلكتروني و/أو كلمة المرور غير صحيحين. يرجى المحاولة مرة أخرى")
#         return redirect("userauths:user_login")
#     except:
#       messages.error(request,"يبدو أن البريد الإلكتروني و/أو كلمة المرور غير موجودين. يرجى التسجيل و إعادة المحاولة")
#       return redirect("userauths:user_login")
#   return render (request,"registration/user_login.html")


def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        email = request.POST['email']
        password = request.POST['password1']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
        # Authentication failed, display error message
            messages.error(request, 'تأكد من أسم المستخدم و كلمة المرور ثم أعد المحاولة')
            return redirect('userauths:user_login')
    else:
        form = Login_Form()
        data = Destinations.objects.all()
        return render(request, "registration/user_login.html", {"data": data, "form": form})




def logout_user(request):
    logout(request)
    return redirect ('index')

# def signup(request):
#     if request.user.is_authenticated:
#         messages.warning(request, f"You are already logged in")
#         return redirect("index")
#     if request.method == 'POST':
#         form = UserCreationForms(request.POST or None)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             userr = authenticate(username=username,password=password)
#             login(request,userr)
#             profile = Profile.objects.get(user=request.user)
#             profile.full_name = full_name
#             profile.phone = phone
#             profile.save()
#             return redirect("index")
#         else:
#             messages.error(request, 'تأكد من أن البيانات يتم إدخالها بشكل صحيح كما هو مطلوب ثم أعد المحاولة')
#             return redirect('signup')
#     else:
#         form =UserCreationForms()
#         data = Destinationss.objects.all()
#         return render(request, "userauths/signup.html", {"form":form,"data":data,"pagetitle": " EG - MedT"})
#     form =UserCreationForms()
#     data = Destinationss.objects.all()
#     return render(request, "userauths/signup.html", {"form":form,"data":data,"pagetitle": " EG - MedT"})
