from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,TicketForm,SticketForm
from .models import Ticket
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request,'apolloapp/home.html')



def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=RegisterForm()       

    return render(request,'apolloapp/register.html',{'form':form})



class CreateTicket(LoginRequiredMixin,CreateView):
    model=Ticket
    fields=['title','description']
    template_name='apolloapp/ticket.html'
    
    def form_valid(self,form):
        form.instance.username=self.request.user
        return super().form_valid(form)
    

class TicketDetail(LoginRequiredMixin,DetailView):
    model=Ticket
    template_name='apolloapp/detail.html'
    context_object_name='tickets'

@login_required
def viewtickets(request):
    if request.user.is_superuser:
        tlist=Ticket.objects.all()
        return render(request,'apolloapp/tclist.html',{'tlist':tlist})
    else:
    
        tlist=Ticket.objects.filter(username__id=request.user.id)
        return render(request,'apolloapp/userlist.html',{'tlist':tlist})
    




def ticket_delete(request,id):
    ticket = Ticket.objects.get(id=id)
    if request.method=='POST':
        ticket.delete()
        return redirect('apolloapp:tclist')
    return render(request,'apolloapp/ticket-delete.html',{'ticket':ticket})


def ticket_update(request,id):
    ticket=Ticket.objects.get(id=id)
    form=TicketForm(request.POST or None,instance=ticket)

    if form.is_valid():
        form.save()
        return redirect('apolloapp:tclist')
    return render(request,'apolloapp/ticket.html',{'form':form})


def ticket_supdate(request,id):
    ticket=Ticket.objects.get(id=id)
    form=SticketForm(request.POST or None,instance=ticket)

    if form.is_valid():
        form.save()
        return redirect('apolloapp:tclist')
    return render(request,'apolloapp/ticket.html',{'form':form})
