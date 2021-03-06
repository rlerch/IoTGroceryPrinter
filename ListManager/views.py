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

	printer.setLineHeight()
	printer.setSize('L')
	printer.justify('C')
	printer.println("My Grocery List")

	printer.feed()
	printer.justify('L')
	printer.setSize('M')

	for item in list_data:
		length = len(item["name"])
		printer.println(item["name"] + " " * (25 - length) + item["amount"])
		printer.feed()

	printer.feed(3)
	return HttpResponse()