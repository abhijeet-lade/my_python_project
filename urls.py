

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('index/', index_view),
    path('booking/', booking_view),
    path('display/', display_view),
    path('update/<int:booking_id>/', update_view),
    path('delete/<int:booking_id>/', delete_view),
    path('photos/', photos_view),
    path('student/', getStudent),
    path('employees/',getEmployee),
    path('product/',product),
    path('saveInformation/', saveInformation),
    path('updateinfotmations',updateStudent),
    path('getinformation/<rollnumber>',getInformation),
    path('deleteinformation/<rollnumber>',deleteStudent),
    path('getAllStudents',getAllStudents),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('addition/',addition),
    
    path('showregister', showregister),
    path('saveUserData', saveUserData),
    path('checkusername', checkUsername)
    
    
]