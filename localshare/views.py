from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response("registrationpage.html",context_instance=RequestContext(request))


def sharable(request):
    customer_pickup=request.POST['pickup']
    customer_drop=request.POST['drop']
    customer_time=request.POST['time']
    return HttpResponseRedirect("/"+"Utoo/"+customer_pickup+"-to-"+customer_drop+"/")
#    return render_to_response("sharepage.html",{"customer_pickup":customer_pickup, "customer_drop":customer_drop, "customer_time":customer_time},context_instance=RequestContext(request))


def finaldisplay(request, route):
    return render_to_response("sharepage.html",{"route":route},context_instance=RequestContext(request))

