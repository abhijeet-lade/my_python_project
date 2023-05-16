from django.shortcuts import render,redirect
from .models import *
from rest_framework .response import Response
from rest_framework .decorators import api_view
from bookingapp.serializer import InfoSerializer
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import render,HttpResponse
from .models import *


# Create your views here.

def index_view(request):
    return render(request, 'bookingapp/homepage.html')
 
def booking_view(request):
    print(request.method)
    if request.method == 'POST':
      uname=request.POST.get('name')
      mobile=request.POST.get('mobile')
      email_id=request.POST.get('email_id')
      booking_date=request.POST.get('booking_date')
      bike_type=request.POST.get('bike_type')
    
      bike=Booking(name=uname,mobile=mobile,email_id=email_id,booking_date=booking_date,bike_type=bike_type)
      bike.save()
      return redirect('/bookingapp/display/')


    return render(request, 'bookingapp/bookingpage.html')


def display_view(request):
    data=Booking.objects.all()
    context={'data':data}
    return render(request, 'bookingapp/display.html',context)

def update_view(request,booking_id):
    data = Booking.objects.get(pk=booking_id)
    context = {'data': data}

    if request.method == 'POST':
        uname = request.POST.get('name')
        mobile= request.POST.get('mobile')
        email= request.POST.get('email_id')
        date = request.POST.get('booking_date')
        biketype = request.POST.get('bike_type')

        # book=Booking(Name=uname,mobile=mobile,email_id=email,days=days,adhar_no=adhar,booking_date=date,status=status,no_of_persons=noofpersons,room_type=roomtype)

        data.name = uname
        data.mobile = mobile
        data.email_id = email
        data.booking_date = date
        data.bike_type = biketype
        data.save()

        return redirect('/bookingapp/display/')


    return render(request, 'bookingapp/update.html', context)

def delete_view(request,booking_id):
    data=Booking.objects.get(pk=booking_id)
    data.delete()
    return redirect('/bookingapp/display/')


def photos_view(request):
    return render(request, 'bookingapp/photos.html')

# @api_view(['GET','POST'])
# def hello(request):
#     return Response({"rno":2,"name":"akshay"})

# @api_view(['GET','POST'])
# def employee(request):
#     return Response({"eid":2,"e_name":"ganesh"})

@api_view(['GET','POST'])
def hello(request):
    return Response({"rno":1, "name":"abhi",})

@api_view(['GET','POST'])
def getStudent(request):
    return Response({"rno":1, "name":"abhi", "marks":80})

@api_view(['GET','POST'])
def getEmployee(request):
    return Response({"Eid":1, "name":"abhi", "salary":80000})

@api_view(['GET','POST'])
def product(request):
    return Response({"product_no":1, "product_name":"honda","prize":800000})

@api_view(['POST'])
def saveStudent(request):
    datafromclient=request.data
    Boys.object.create(rno=datafromclient['rno'],marks=datafromclient['marks'])
    # Boys.object.create(rno=1,marks=70)
    return Response("data store in db")

@api_view(['GET'])
def getInformation(request,rollnumber):
    informationfromdb=Info.objects.get(rno=rollnumber)
    # boysfromdb=>["rno":1, "name":"abhi"]
    # return Response({"rno":informationfromdb.rno, "name":informationfromdb.name:, "marks":informationfromdb.marks})
    infoSerializer=InfoSerializer(informationfromdb)
    response=Response(infoSerializer.data)
    return response

@api_view(['POST'])
def saveInformation(request):
    datafromclient=request.data
    print(datafromclient)
    # {"rno":1, "name":"abhi", "marks":80}
    # boysfromdb=>["rno":1, "name":"abhi"]
    # rnofromclient=datafromclient['rno']
    # namefromclient=datafromclient['name']
    # marksfromclient=datafromclient['marks']
    
    # Info.objects.create(rno=rnofromclient,name=namefromclient,marks=marksfromclient)
    
    infoSerializer=InfoSerializer(data=datafromclient)
    
    if infoSerializer.is_valid():
        infoSerializer.save()
        
    return Response("data stored in database")



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

def updateStudent(request):
    
     
    datafromclient=request.data
    
    print(datafromclient) #{"rno":105,"name":"rahul","marks":70}

    # there is already record of rno 105 and we want to update it

    studentfromdb=Info.objects.get(rno=datafromclient["rno"])

    serializer=InfoSerializer(studentfromdb,data=datafromclient,partial=False)
    
    if(serializer.is_valid()):
        serializer.save()

    return Response("data updated in database")



@api_view(['DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])

def deleteStudent(request,rollnumber):
    
    Info.objects.get(rno=rollnumber).delete()

    return Response("data deleted in database")




@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def getAllStudents(request):
    
    allstudentsfromdb=Info.objects.all()

    seriliazer=InfoSerializer(allstudentsfromdb,many=True)
    
    response=Response(seriliazer.data)

    return response


def addition(request):
     no1=request.GET['no1']
     no2=request.GET['no2']
     no3=int(no1)+int(no2)
     #return HttpResponse(no3)
     return render(request,'bookingapp/addition.html',{'answer':no3,'no1':no1,'no2':no2})
 
 
 
 



def saveUserData(request):

    print(type(request))
    name=request.POST['name']
    password=request.POST['password']
    mobno=request.POST['mobno']
    email=request.POST['email']
    photo=request.FILES['photo']
    imagepath='/upload/'+photo.name

    with open('examapp/static/upload/'+photo.name, 'wb+') as destination:  
                for data in photo.chunks():  
                    destination.write(data)
    
    User.objects.create(name=name,password=password,mobno=mobno,email=email,imagepath=imagepath)
   
    return render(request,'examapp/login.html',{'message':'registration successful.please login now','imagepath':imagepath})



def showregister(request):
    return render(request,"examapp/register.html")



def checkUsername(request):
    print(request.GET["username"])
    message="username already present"
    try:
        userdata=User.objects.get(name=request.GET["username"])
        print(userdata)
    except:
        traceback.print_exc()
        message='username does not exist'

    data={
          'message':message
       }
    json_data=json.dumps(data) # dumps() converts python dictionary into JSON String
    print(json_data)
    response=HttpResponse(f'{json_data}',content_type='application/json')
    return response










