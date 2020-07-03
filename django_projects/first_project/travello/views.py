from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def travello(request):
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City never Sleeps'
    # dest1.image = 'destination_1.jpg'
    # dest1.price = 700
    #
    # dest2 = Destination()
    # dest2.name = 'Kolkata'
    # dest2.desc = 'The City of Palaces'
    # dest2.image = 'destination_2.jpg'
    # dest2.price = 770
    #
    # dest3 = Destination()
    # dest3.name = 'Bangalore'
    # dest3.desc = 'The City of Gardens'
    # dest3.image = 'destination_3.jpg'
    # dest3.price = 777
    #
    # dest4 = Destination()
    # dest4.name = 'Delhi'
    # dest4.desc = 'The Capital City'
    # dest4.image = 'destination_4.jpg'
    # dest4.price = 900
    #
    # dest5 = Destination()
    # dest5.name = 'Guwahati'
    # dest5.desc = 'The North East Gateway'
    # dest5.image = 'destination_5.jpg'
    # dest5.price = 590
    #
    # dest6 = Destination()
    # dest6.name = 'Goa'
    # dest6.desc = 'The City of Party'
    # dest6.image = 'destination_6.jpg'
    # dest6.price = 975
    # dest6.offer = True

    # dests = [dest1,dest2,dest3,dest4,dest5,dest6]

    dests = Destination.objects.all()

    return render(request,'index.html',{'dests': dests})
# def add(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     res = val1+val2
#     return render(request, 'result.html',{'result': res})