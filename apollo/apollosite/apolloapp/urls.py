from django.urls import URLPattern, path
from . import views




app_name='apolloapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('<int:pk>/',views.TicketDetail.as_view(),name='detail'),
    path('ticket/',views.CreateTicket.as_view(),name='ticket'),
    path('tclist',views.viewtickets,name='tclist'),
    path('delete/<int:id>/',views.ticket_delete,name='ticket_delete'),
    path('update/<int:id>/',views.ticket_update,name='ticket_update'),
    path('supdate/<int:id>/',views.ticket_supdate,name='ticket_supdate'),
    
]