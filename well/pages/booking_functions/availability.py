import datetime
from pages.models import Rooms, Resorts,RegularBooking


def check_availability(Rooms, arrival_date, leave_date):
  avail_list=[]
  booking_list = RegularBooking.objects.filter(room=room)
  for RegularBooking in booking_list:
    if RegularBooking.arrival_date > leave_date or RegularBooking.leave_date < arrival_date:
      avail_list.append(True)
    else:
      avail_list.append(False)
  return all(avail_list)