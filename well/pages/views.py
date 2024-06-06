from django.shortcuts import render, redirect , HttpResponse, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator
import ssl
import smtplib
from django.views.generic import ListView , FormView , View
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Login_Form,UpdateUserForm,UserCreationForms,AvailabilityForm
from .models import *
from .booking_functions.availability import check_availability
from django.urls import reverse_lazy




# Create your views here.

def index(request , des_id =1):
    data = Destinations.objects.all()
    # des = Destinations.objects.get(des_id=1)
    return render(request, "pages/index.html", {"data":data,"pagetitle":"Home - EG MedT"})

def cart(request):
    data = Destinations.objects.all()
    return render(request, "pages/cart.html", {"data":data})



def carts(request):
    data = Destinations.objects.all()
    res = Resorts.objects.all()
    paginator = Paginator(res, 3)
    page = request.GET.get("page")
    res = paginator.get_page(page)
    return render(request, "pages/carts.html", {"res":res,"data":data})


def single_pro(request):
    data = Destinations.objects.all()
    return render(request, "pages/single_pro.html", {"data":data})

def checkout(request):
    data = Destinations.objects.all()
    return render(request, "pages/checkout.html", {"data":data})

@login_required
def Profile(request):
    data = Destinations.objects.all()
    # detail = profile.objects.all(slug=slug)
    return render(request, "registration/profile.html", {"data":data, "pagetitle":"Home - EG MedT"})


@csrf_protect
def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
    data = Destinations.objects.all()
    return render(request, "registration/update_profile.html", {"user_form":user_form,"data":data,"pagetitle":"Home - EG MedT"})

def price(request):
    data = Destinations.objects.all()
    return render(request,"pages/price.html", {"data":data,"pagetitle": "Best Price Guarantee | EG MedT"})


def contact(request):
        data = Destinations.objects.all()
        return render(request, "pages/contact.html", {"data":data,"pagetitle": "Contact us | EG MedT"})


def destinations(request):
    des = Destinations.objects.all()
    data = Destinations.objects.all()
    return render(request, "pages/Destinations.html",{"data":data,"des":des})


def offers(request):
    data = Destinations.objects.all()
    return render(request, "pages/offers.html",{"data":data})


def Programme(request):
    data = Destinations.objects.all()
    return render(request, "pages/stay-without-programme.html",{"data":data})


def almyra(request):
    data = Destinations.objects.all()
    return render(request, "pages/almyra.html",{"data":data})


def we(request):
    data = Destinations.objects.all()
    return render(request, "pages/how-we-work.html",{"data":data})


def Siwa(request):
    try:
        des = Destinations.objects.get(des_id=1)
        R1 =Resorts.objects.get(resort_id=1)
        R2 =Resorts.objects.get(resort_id=2)
    except Destinations.DoesNotExist:
        return HttpResponseNotFound("des not found")
    data =Destinations.objects.all()
    return render(request, "pages/Siwa.html",{"des":des,"R1":R1,"R2":R2,"data":data})


def D1(request):
    Resort =Resorts.objects.get(resort_id=2)
    Room =Rooms.objects.get(room_id=1)
    Rom =Rooms.objects.get(room_id=2)
    offer =Offers.objects.get(resort_id=1)
    data = Destinations.objects.all()
    DD = offer.total /offer.period
    PP = offer.total -DD
    return render(request, "pages/Dream_Lodge_Siwa.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer, "PP":PP, "DD":DD})


def D2(request):
    try:
        Resort =Resorts.objects.get(resort_id=1)
        Room =Rooms.objects.get(room_id=1)
        Rom =Rooms.objects.get(room_id=2)
        offer =Offers.objects.all()
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    except Rooms.DoesNotExist:
        return HttpResponseNotFound("Rooms not found")
    data = Destinations.objects.all()
    return render(request, "pages/Siwa_Shali.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer})


def Sinia(request):
    try:
        des = Destinations.objects.get(des_id=2)
        R3 =Resorts.objects.get(resort_id=3)
        R4 =Resorts.objects.get(resort_id=4)
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    data = Destinations.objects.all()
    return render(request, "pages/Sinia.html",{"data":data,"des":des,"R3":R3,"R4":R4})


def D3(request):
    try:
        Resort =Resorts.objects.get(resort_id=4)
        Room =Rooms.objects.get(room_id=1)
        Rom =Rooms.objects.get(room_id=2)
        offer =Offers.objects.all()
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    except Rooms.DoesNotExist:
        return HttpResponseNotFound("Rooms not found")
    data = Destinations.objects.all()
    return render(request, "pages/Savoy_Sharm.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer})


def D4(request):
    try:
        Resort =Resorts.objects.get(resort_id=5)
        Room =Rooms.objects.get(room_id=1)
        Rom =Rooms.objects.get(room_id=2)
        offer =Offers.objects.all()
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    except Rooms.DoesNotExist:
        return HttpResponseNotFound("Rooms not found")
    data = Destinations.objects.all()
    return render(request, "pages/Mövenpick_Resort_Aswan.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer})


# def D4(request):
#     data = Destinations.objects.all()
#     return render(request, "pages/amanwella.html",{"data":data})


def D5(request):
    try:
        Resort =Resorts.objects.get(resort_id=6)
        Room =Rooms.objects.get(room_id=1)
        Rom =Rooms.objects.get(room_id=2)
        offer =Offers.objects.all()
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    except Rooms.DoesNotExist:
        return HttpResponseNotFound("Rooms not found")
    data = Destinations.objects.all()
    return render(request, "pages/Eco_Nubia.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer})

# def D5(request):
#     data = Destinations.objects.all()
#     return render(request, "pages/swaswara.html",{"data":data})


def D7(request):
    try:
        Resort =Resorts.objects.get(resort_id=3)
        Room =Rooms.objects.get(room_id=1)
        Rom =Rooms.objects.get(room_id=2)
        offer =Offers.objects.all()
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    except Rooms.DoesNotExist:
        return HttpResponseNotFound("Rooms not found")
    data = Destinations.objects.all()
    return render(request, "pages/Baron_Palms_Resort.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer})


def Aswan(request):
    try:
        des = Destinations.objects.get(des_id=3)
        R6 =Resorts.objects.get(resort_id=6)
        R5 =Resorts.objects.get(resort_id=5)
    except Resorts.DoesNotExist:
        return HttpResponseNotFound("Resorts not found")
    data = Destinations.objects.all()
    return render(request, "pages/Aswan.html",{"data":data,"des":des,"R6":R6,"R5":R5})


def D6(request):
    data = Destinations.objects.all()
    return render(request, "pages/amal-tamara.html",{"data":data})




# @csrf_protect
# def user_login(request):
#     if request.method == 'POST':
#         form = Login_Form()
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('index')
#         else:
#             messages.error(request, ('يبدو أن البريد الإلكتروني و/أو كلمة المرور غير صحيحين. يرجى المحاولة مرة أخرى'))
#             return redirect('user_login')
#     else:
#         messages.error(request, ('يبدو أن البريد الإلكتروني و/أو كلمة المرور غير صحيحين. يرجى المحاولة مرة أخرى'))
#         form = Login_Form()
#         data = Destinations.objects.all()
#         return render(request, "pages/user_login.html",{"data":data,"form":form})


def forgetpass(request):
    data = Destinations.objects.all()
    return render(request, "pages/forgetpassword.html",{"data":data,"pagetitle": " EG - MedT"})


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
#         data = Destinations.objects.all()
#         return render(request, "userauths/signup.html", {"form":form,"data":data,"pagetitle": " EG - MedT"})
#     form =UserCreationForms()
#     data = Destinations.objects.all()
#     return render(request, "userauths/signup.html", {"form":form,"data":data,"pagetitle": " EG - MedT"})








def Helwan(request):
    data = Destinations.objects.all()
    return render(request, "pages/Helwan.html", {"data":data,"pagetitle": " EG - MedT"})




def P1 (request):
    Resort =Resorts.objects.get(resort_id=2)
    Room =Rooms.objects.get(room_id=1)
    Rom =Rooms.objects.get(room_id=2)
    offer =Offers.objects.get(resort_id=1)
    data = Destinations.objects.all()
    DD = offer.total /offer.period
    PP = offer.total -DD
    return render(request, "pages/P1.html",{"data":data,'resort':Resort,'room':Room,'rom':Rom,'offer':offer, "PP":PP, "DD":DD})



class RoomListView(ListView):
    model = Rooms

class BookingList(ListView):
    model = RegularBooking

# class RoomDetailView(View):
#     def get(self , request , *args ,**kwargs):
#         room_type = self.kwargs.get('room_type', None)
#         room_list = Rooms.objects.filter(room_type=room_type)
#         room = room_type[0]
#         return render (request, )


    def post(self , request , *args ,**kwargs):
        room_list = Rooms.objects.filter(room_type=room_type)
        available_rooms=[]
        for room in room_list:
            if check_availability(room,data['arrival_date'], data['leave_date']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking =RegularBooking.objects.create(
                user = self.request.user,
                room =room,
                arrival_date = data['arrival_date'],
                leave_date = data['leave_date'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('جميع الغرف محجوزة ، جرب غرفة من نوع أخر')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'pages/availability_form.html'
    success_url = reverse_lazy('index')
    def form_invalid(self, form):
        data =form.cleaned_data
        room_list = Rooms.objects.filter(room_type=data['room_type'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room,data['arrival_date'], data['leave_date']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking =RegularBooking.objects.create(
                user = self.request.user,
                room =room,
                arrival_date = data['arrival_date'],
                leave_date = data['leave_date'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('جميع الغرف محجوزة ، جرب غرفة من نوع أخر')

