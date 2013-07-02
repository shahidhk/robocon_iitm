from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
	'''Additional data for users'''
	# This field is required.
	user=models.OneToOneField(User)
	# Other fields here.
	dept = models.CharField(max_length=30)
	roll_no = models.CharField(max_length=8)
	dob = models.DateField()
	mobile = models.IntegerField(max_length=10)
	display_pic = models.ImageField(upload_to='users', blank=True, null=True)
	facebook = models.URLField()
	twitter = models.URLField()
	linkedin = models.URLField()
	team = models.CharField(max_length=30)
	year = models.IntegerField(max_length=4)

	def __unicode__(self):
		return self.user.username

class Thread(models.Model):
	'''Defines the data posted in thread'''
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now=True,null=False)
	pic = models.ImageField(upload_to='blog')
	description = models.TextField()

	def __unicode__(self):
		return self.title

class Contact(models.Model):
	'''Defines arbitrary contact information'''
	title = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	website = models.URLField()
	phone = models.IntegerField()

	def __unicode__(self):
		return self.title

class Sponsor(models.Model):
	'''Defines data about sponsors'''
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='spons', blank=True, null=True)
	website = models.URLField()

	def __unicode__(self):
		return self.name

class Team(models.Model):
	'''Defines team members'''
	name=models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class ContactRequests(models.Model):
	'''Stores data from the contact us form in home page'''
	name=models.CharField(max_length=50)
	email=models.EmailField()
	message=models.TextField()

	def __unicode__(self):
		return self.name