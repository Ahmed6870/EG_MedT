from django.contrib import admin
# from .models import profile
from .models import CareType
from .models import CareDR
from .models import Resorts
from .models import ResortsPhone
from .models import Diseases
from .models import DiseaseDR
from .models import Destinations
from .models import Hotels
from .models import Rooms
from .models import RoomOffers
from .models import RegularRoom
from .models import RegularBooking
from .models import Offers
from .models import OffersBooking
from .models import OffersBookingOffers
from .models import ComplainsComments
# Register your models here.
# from .models import AuthGroup

# admin.site.register(profile)
admin.site.register(CareType)
admin.site.register(CareDR)
admin.site.register(Resorts)
admin.site.register(ResortsPhone)
admin.site.register(Diseases)
admin.site.register(DiseaseDR)
admin.site.register(Destinations)
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(RoomOffers)
admin.site.register(RegularRoom)
admin.site.register(RegularBooking)
admin.site.register(Offers)
admin.site.register(OffersBooking)
admin.site.register(OffersBookingOffers)
admin.site.register(ComplainsComments)
