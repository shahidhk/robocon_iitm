from django.db import models

class Contact(models.Model):
    """
        Don't know what this is for
        Even i'm confused
        Where did this come from?
    """
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField()
    phone = models.IntegerField()

    def __unicode__(self):
        return self.title
