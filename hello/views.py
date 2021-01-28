from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic import View
from config import username,password
import datetime
from .models import Client, Log
from gettingstarted.utils import render_to_pdf


def index(request):
	return render(request, "index.html")

def home(request):
	if request.method == "POST":
		u=request.POST['username']
		p=request.POST['password']
		if u==username and p==password:

			clients = Client()
			clientsRows =Client.objects.all().order_by("clientId")
			return render(request, "home.html", {"clientsRows": clientsRows,'aut':''})
		else:
			return render(request, "index.html",{'error':'Username or password incorrect'})
	else:
		return render(request, "index.html")

class GeneratePdf(View):
	def post(self, request, *args, **kwargs):
		if request.method == "POST":
			clientId=request.POST['clientId']
			first_name=request.POST['first_name']
			last_name=request.POST['last_name']
			email=request.POST['email']
			phone=request.POST['phone']
			size=request.POST['size']
			tireName=request.POST['tireName']
			tireCount=request.POST['tireCount']
			platesNum=request.POST['platesNum']
			note=request.POST['note']
			dateIn=request.POST['dateIn']
			dateOut=request.POST['dateOut']
			totalDays = request.POST['totalDays']
			price=request.POST['price']
			totalPrice=request.POST['totalPrice']
			onCall=request.POST['onCall']
			data = {
					'today': datetime.date.today(),
					'amount': totalPrice,
					'customer_name':f'{first_name} {last_name}',
					'order_id': clientId}
			pdf = render_to_pdf('invoice.html', data )
			return HttpResponse(pdf, content_type='application/pdf')


def removeClient(request):
	if request.method == "GET":
		clientId=request.GET.get('clientId')
		jopa = Client.objects.filter(clientId=clientId).delete()
		clients = Client()
		clientsRows =Client.objects.all().order_by("clientId")
		return render(request, "home.html", {"clientsRows": clientsRows,'aut':''})

def createClient(request):
	if request.method == "POST":
		clientId=request.POST['clientId']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		phone=request.POST['phone']
		size=request.POST['size']
		tireName=request.POST['tireName']
		tireCount=request.POST['tireCount']
		platesNum=request.POST['platesNum']
		note=request.POST['note']
		dateIn=request.POST['dateIn']
		dateOut=request.POST['dateOut']
		totalDays = request.POST['totalDays']
		price=request.POST['price']
		totalPrice=request.POST['totalPrice']
		onCall=request.POST['onCall']
		if Client.objects.filter(clientId=clientId).exists():
			clientsRows =Client.objects.all().order_by("clientId")
			return render(request, "home.html", {"clientsRows": clientsRows,'error':'clientId already exists','aut':''})
		else:
			clients = Client(clientId=clientId,first_name = first_name,last_name = last_name, email=email,
						phone=phone,size=size,tireName =tireName,tireCount = tireCount,
						platesNum = platesNum,note= note,dateIn=dateIn,dateOut=dateOut,price = price,
						totalPrice=totalPrice,totalDays=totalDays,onCall= onCall)
			log = Log(clientId=clientId,first_name = first_name,last_name = last_name, email=email,
						phone=phone,size=size,tireName =tireName,tireCount = tireCount,
						platesNum = platesNum,note= note,dateIn=dateIn,dateOut=dateOut,price = price,
						totalPrice=totalPrice,totalDays=totalDays,onCall= onCall)
			log.save()
			clients.save()
			clientsRows =Client.objects.all().order_by("clientId")
			return render(request, "home.html", {"clientsRows": clientsRows,'aut':''})


def updateClient(request):
	if request.method == "POST":
		clientId=request.POST['clientId']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		phone=request.POST['phone']
		size=request.POST['size']
		tireName=request.POST['tireName']
		tireCount=request.POST['tireCount']
		platesNum=request.POST['platesNum']
		note=request.POST['note']
		dateIn=request.POST['dateIn']
		dateOut=request.POST['dateOut']
		price=request.POST['price']
		totalPrice=request.POST['totalPrice']
		totalDays = request.POST['totalDays']
		onCall=request.POST['onCall']

		#e = Client.objects.get(id=clientId)
		e = Client.objects.get(clientId=clientId)

		e.clientId=clientId
		e.first_name=first_name
		e.last_name=last_name
		e.email=email
		e.phone=phone
		e.size=size
		e.tireName=tireName
		e.tireCount=tireCount
		e.platesNum=platesNum
		e.note=note
		e.dateIn=dateIn
		e.dateOut=dateOut
		e.price=price
		e.totalPrice=totalPrice
		e.totalDays=totalDays
		e.onCall=onCall
		e.save()

		log = Log(clientId=clientId,first_name = first_name,last_name = last_name, email=email,
						phone=phone,size=size,tireName =tireName,tireCount = tireCount,
						platesNum = platesNum,note= note,dateIn=dateIn,dateOut=dateOut,price = price,
						totalPrice=totalPrice,totalDays=totalDays,onCall= onCall)
		log.save()



		clientsRows = Client.objects.all().order_by("clientId")
		return render(request, "home.html", {"clientsRows": clientsRows,'aut':''})


def editClient(request):
	if request.method == "POST":
		clientId=request.POST['clientId']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		phone=request.POST['phone']
		size=request.POST['size']
		tireName=request.POST['tireName']
		tireCount=request.POST['tireCount']
		platesNum=request.POST['platesNum']
		note=request.POST['note']
		dateIn=request.POST['dateIn']
		dateOut=request.POST['dateOut']
		price=request.POST['price']
		totalPrice=request.POST['totalPrice']
		totalDays = request.POST['totalDays']
		onCall=request.POST['onCall']

		
		logRows =Log.objects.filter(clientId=clientId).order_by("-when")
		return render(request, "editClient.html", 
			{"clientId": clientId,
			"first_name": first_name,
			"last_name": last_name,
			"email": email,
			"phone": phone,
			"size": size,
			"tireCount": tireCount,
			"tireName": tireName,
			"platesNum": platesNum,
			"note": note,
			"dateIn": dateIn,
			"dateOut": dateOut,
			"price": price,
			"totalPrice": totalPrice,
			"totalDays":totalDays,
			"onCall": onCall,
			"clientsRows": logRows,
			'aut':''
			})