from django.db import models

class Sponsor(models.Model):
    """
        Contains data about sponsors
    """
    name = models.CharField(max_length=50) # Name of the sponsor/company
    logo = models.ImageField(upload_to='spons', blank=True, null=True) # An image field for their logo
    website = models.URLField() # URL of their site
    # @shahid put youtube, facebook, etc here also.

    def __unicode__(self):
        return self.name


class ContactRequests(models.Model):
    """
        Prospective sponsors / people who want to contact us
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return self.name
