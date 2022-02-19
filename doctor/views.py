from __future__ import print_function
from time import time
from urllib import response

from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserMainF
from django.contrib.auth.models import User
from .models  import UserCreation,Address, Speciality
from blog.models import Blog
#******************************************************************************
# For Calendar



import datetime, pytz
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#******************************************************************************

def proper_time(t):

    timedel=datetime.timedelta(minutes=45)

    t=datetime.datetime.strptime(t,"%Y-%m-%dT%H:%M:%S")

    t=(t+timedel)
    t=str(t)[:10]+'T'+str(t)[11:]
    return t




#------------------------------------------------------------------------------
def create_cal(uname):
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
            'https://www.googleapis.com/auth/calendar',
            'https://www.googleapis.com/auth/calendar.events',
            'https://www.googleapis.com/auth/calendar.events.readonly'
    ]


    def main():
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)
            request_body={
                'summary':uname
            }

            response=service.calendars().insert(body=request_body).execute()
        
        except HttpError as error:
            print('An error occurred: %s' % error)
        return response

    res=main()
    return res['id']
#------------------------------------------------------------------------------

#-**-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def create_event(cal_id,specs,datet):
    def main():
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
                'https://www.googleapis.com/auth/calendar',
                'https://www.googleapis.com/auth/calendar.events',
                'https://www.googleapis.com/auth/calendar.events.readonly'
        ]
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        print(datet,"**-*-*-*-*-**-*-*")
        print(proper_time(datet+':00'))
        
        try:
            service = build('calendar', 'v3', credentials=creds)
            event = {
                    'summary': specs,
                    'description': 'A chance to hear more about Google\'s developer products.',
                    'start': {
                        'dateTime':  datet+':00',
                        'timeZone': 'Asia/Kolkata',
                    },
                    'end': {
                        'dateTime':  proper_time(datet+':00'),
                        'timeZone': 'Asia/Kolkata',
                    },
            }
            event = service.events().insert(calendarId=cal_id, body=event).execute()
            print('reached******')
            
        except HttpError as error:
            print('An error occurred: %s' % error)


    main()

#-**-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

###################################################################################

def event_list(id):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/calendar.events.readonly'
        ]


    def main():
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)
            
            now = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).isoformat() #+ 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId=id, timeMin=now,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items')
            

            if not events:
                print('No upcoming events found.')
                return
            event_l=[]
            # Prints the start and name of the next 10 events
            for event in events:
                start = event['start'].get('dateTime')
                timedel=datetime.timedelta(hours=5,minutes=30)
                start=datetime.datetime.strptime(start[:-1],"%Y-%m-%dT%H:%M:%S")
                start=(start+timedel)
                event_l.append(start)
                print()
                print()
                print(start, event['summary'])
                print()

        except HttpError as error:
            print('An error occurred: %s' % error)
        return event_l

    return main()
###################################################################################

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def conflict(start_time,id):
    e_list=event_list(id)
    print(e_list)
    if (e_list)==None:
        return True
    time_list=[]
    conflict_dict={}

    l=0
    for obj in e_list:
        k=0
        time_list.append(obj)
        while k<45:
            timedel=datetime.timedelta(minutes=1)
            # obj=datetime.strptime(str(obj),"%Y-%m-%d %H:%M:%S")
            obj=(obj+timedel)
            time_list.append(obj)
            k=k+1
        conflict_dict[l]=time_list
        l=l+1
        time_list=[]
    print(conflict_dict)
    if len(conflict_dict)==0:
        print(True)
        return True

    conflict_starttime_dict=dict()
    k=0
    obj=start_time
    time_list.append(obj)
    while k<45:
        timedel=datetime.timedelta(minutes=1)
        # obj=datetime.strptime(str(obj),"%Y-%m-%d %H:%M:%S")
        obj=(obj+timedel)
        time_list.append(obj)
        k=k+1
    conflict_starttime_dict[0]=time_list
    # print(conflict_starttime_dict[0])

    k=0
    while k<len(conflict_dict):
        for i in conflict_starttime_dict[0]:
            if i in conflict_dict[k]:
                print('false')
                return False
        k=k+1
    return True
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def home(request):
    objs=Blog.objects.all()
    stat=None
    statp=False
    try:
        if request.user.usercreation.choice=='1':
            stat=1
        elif request.user.usercreation.choice=='2':
            statp=True
    except:
        stat=None
    return render(request,'doctor/home.html',{'posts':objs,"status":stat,'statusp':statp})


def userform(request):
    if request.method=='POST':
        userf_obj=UserMainF(request.POST,request.FILES)
        print(request.POST['choice'])
        print(request.POST['username'])
        if userf_obj.is_valid():
            userf_obj.save()
            address_obj=Address(line1=request.POST['line1'],city=request.POST['city'],
                                state=request.POST['state'],pincode=request.POST['pincode'])
            if request.POST['choice']=='1':
                calendar_id=create_cal(request.POST['username'])
            else:
                calendar_id=''
            address_obj.save()
            user_obj=User.objects.get(username=request.POST['username'])
            status_obj=UserCreation(user=user_obj,choice=request.POST['choice'],
                                    address=address_obj,pic=request.FILES["pic"],
                                    cal_id=calendar_id)
            status_obj.save()
            print(status_obj)
            return redirect('/login')
    else:
        userf_obj=UserMainF()
    return render(request,'doctor/form.html',{'form':userf_obj})


def dashb(request):
    if request.user.usercreation.choice=='1':
        stat='Doctor'
    else:
        stat='Patient'
    return render(request,'doctor/dashb.html',{"status":stat})


def doc_list(request):
    doc_l=[]
    user_obj=User.objects.all()
    print(user_obj)

    stat=None
    statp=False
    try:
        if request.user.usercreation.choice=='1':
            stat=1
        elif request.user.usercreation.choice=='2':
            statp=True
    except:
        stat=None
        statp=False

    for doc in user_obj:
        if doc.usercreation.choice=='1':
            doc_l.append(doc)
            print(doc.first_name)
    print(doc_l)
    for i in doc_l:
        print(i.first_name)

    return render(request,'doctor/doclist.html',{'docs':doc_l,'statusp':statp})


def book(request,id):
    if request.method=='POST':
        print(request.POST['speciality'],request.POST['datetime'])
        da_te=request.POST['datetime'][8:10]+':'+request.POST['datetime'][5:7]+':'+request.POST['datetime'][:4]
        ti_me=request.POST['datetime'][11:16]
        start_time=datetime.datetime.strptime(request.POST['datetime'],"%Y-%m-%dT%H:%M")
        if not conflict(start_time,id):
            messages.info(request,f'Slot at time: {ti_me} and on {da_te} not available, choose \
                                a different slot.')
            return redirect(f'/book/{id}')
        create_event(id,request.POST['speciality'],request.POST['datetime'])
        
        start_time=datetime.datetime.strptime(request.POST['datetime'],"%Y-%m-%dT%H:%M")
        
            # return render()
        
        ucobj=UserCreation.objects.get(cal_id=id)
        doc_name=ucobj.user.first_name+ " " + ucobj.user.last_name
        print(doc_name)
        da_te=request.POST['datetime'][8:10]+':'+request.POST['datetime'][5:7]+':'+request.POST['datetime'][:4]
        ti_me=request.POST['datetime'][11:16]
        end_time=proper_time(request.POST['datetime']+':00')[11:16]
        return render(request,'doctor/set_appoint.html',{'doc_name':doc_name,
                'date':da_te,'time':ti_me,'endtime':end_time})

    print(id)
    print(datetime.datetime.now())

    stat=None
    statp=False
    try:
        if request.user.usercreation.choice=='1':
            stat=1
        elif request.user.usercreation.choice=='2':
            statp=True
    except:
        stat=None
        statp=False



    specs=Speciality.objects.all()
    return render(request,'doctor/appointmentp.html',{'specs':specs,'calendar_id':id,'statusp':statp})