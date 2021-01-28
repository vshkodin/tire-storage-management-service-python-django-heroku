from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Client(models.Model):
		active = models.BooleanField(default=True,null=True)
		clientId=models.TextField(blank=True, null=True)
		first_name = models.TextField(blank=True, null=True, help_text='First Name')
		middle_name = models.TextField(blank=True, null=True, help_text='middle Name')
		last_name = models.TextField(blank=True, null=True, help_text='Second Name')
		email = models.TextField(blank=True,null=True, help_text='example@example.com')
		phone = models.TextField(blank=True,help_text='+7**********')
		size = models.TextField(blank=True,null=True,  help_text='255/65/19')
		tireName = models.TextField(blank=True,null=True, help_text='Continental')
		tireCount = models.TextField(blank=True,null=True, help_text='4')
		platesNum = models.TextField(blank=True,null=True, help_text='o000oo30')
		car = models.TextField(blank=True, null=True)
		withRims = models.TextField(blank=True, null=True)
		note= models.TextField(blank=True,null=True)
		dateOut=models.TextField(blank=True,null=True)
		dateIn=models.TextField(blank=True,null=True)
		totalDays=models.TextField(blank=True,null=True)
		price = models.TextField(blank=True,null=True)
		totalPrice=models.TextField(blank=True,null=True)
		onCall=models.TextField(blank=True,null=True)
		when = models.DateTimeField("date created", auto_now_add=True,null=True, blank=True)
		


class Log(models.Model):
		active = models.BooleanField(default=True,null=True)
		clientId=models.TextField(blank=True, null=True)
		first_name = models.TextField(blank=True, null=True, help_text='First Name')
		middle_name = models.TextField(blank=True, null=True, help_text='middle Name')
		last_name = models.TextField(blank=True, null=True, help_text='Second Name')
		email = models.TextField(blank=True,null=True, help_text='example@example.com')
		phone = models.TextField(blank=True,help_text='+7**********')
		size = models.TextField(blank=True,null=True,  help_text='255/65/19')
		tireName = models.TextField(blank=True,null=True, help_text='Continental')
		tireCount = models.TextField(blank=True,null=True, help_text='4')
		platesNum = models.TextField(blank=True,null=True, help_text='o000oo30')
		car = models.TextField(blank=True, null=True)
		withRims = models.TextField(blank=True, null=True)
		note= models.TextField(blank=True,null=True)
		dateOut=models.TextField(blank=True,null=True)
		dateIn=models.TextField(blank=True,null=True)
		totalDays=models.TextField(blank=True,null=True)
		price = models.TextField(blank=True,null=True)
		totalPrice=models.TextField(blank=True,null=True)
		onCall=models.TextField(blank=True,null=True)
		when = models.DateTimeField("date created", auto_now_add=True,null=True, blank=True)