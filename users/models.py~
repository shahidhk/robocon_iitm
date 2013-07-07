from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """ 
        A profile that holds the extra data for every user in the site
        
    """
    user=models.OneToOneField(User) # A foreign one-to-one field which holds the auth user
    
    nick = models.CharField(max_length = 30) # Nick name of user
    dept = models.CharField(max_length = 30) # Department @Shahid : what is this for ?
    roll_no = models.CharField(max_length = 8) # Roll number of the user
    dob = models.DateField() # date of birth
    mobile = models.IntegerField(max_length = 10) # The mobile number of the user
    display_pic = models.ImageField(upload_to = 'users', blank = True, null = True) # A display pic for every user. @Shahid : put a default pic, remove null/blank
    facebook = models.URLField() # Facebook social-id
    twitter = models.URLField() # Twitter social-id
    linkedin = models.URLField() # LinkedIn social-id
    team = models.CharField(max_length = 30) # the team th user is in @Shahid : why is this charfield ?
    year = models.IntegerField(max_length = 4) # the year(s) in which person was in robocon. @Shahid : there should be a range here. PS : there is a date field which you can configure for this.
    # @Shahid : put youtube link here also.
    
    def __unicode__(self):
        return self.user.username
    
    def get_name(self):
        if self.nick :
            return self.user.first_name + " " + self.user.last_name + " (" + self.nick + ")"
        else :
            return self.user.first_name + " " + self.user.last_name

class Team(models.Model):
    '''Defines team members'''
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
