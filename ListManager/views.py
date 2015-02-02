import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Adafruit_Thermal import *


printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# Create your views here.


def list_manager(request):
	return render(request, 'listManager.html')

@csrf_exempt
def print_list(request):
	list_data = json.loads(request.body)

	printer.setSize('L')
	printer.justify('C')
	printer.println("My Grocery List")

	printer.setSize('M')
	printer.justify('L')

	for item in list_data:
		printer.println(item["name"])
		printer.feed()

	return HttpResponse()