from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    date = datetime.datetime.now()
    My_dict = {'date': date}
    return render(request,'newsApp/index.html',context=My_dict)

def moviesinfo(request):
    head_msg = "latest movie news"
    msg1 = "Stree movie crossed 100cr in two weeks made amazing progress awsome achievement"
    msg2 = "Thug of Hindustan Amitabh bacchan poster released !! looking challanging"
    msg3 = "Robot 2.O teaser released on Aksahay Kumar Birthday got trolled"
    msg4 = "GOvinda Movie FRYDAY trailer realsed people liked it"
    MY_DICT = {'head_msg': head_msg,'msg1': msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsApp/news.html',context=MY_DICT)

def sportsinfo(request):
    head_msg = "latest Sports news"
    msg1 = "India Match with pakistan at 6:00 pm IST today"
    msg2 = "India won by Honkong by 26 Runs"
    msg3 = "Indian Caption Rohit sharma praises hongkong for playing good "
    msg4 = "Fifa is coming soon"
    MY_DICT = {'head_msg': head_msg,'msg1': msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsApp/news.html',context=MY_DICT)

def politicsinfo(request):
    head_msg = "latest politics news"
    msg1 = "Strike by General and OBC against resevation"
    msg2 = "Modi Foreign tour to America on 2nd october"
    msg3 = "karnataka Govt. reduces petrol price by 2 rs"
    msg4 = "Shivraj singh to visit Gwalior on Monday"
    MY_DICT = {'head_msg': head_msg,'msg1': msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsApp/news.html',context=MY_DICT)
