from django.db import models
from datetime import datetime

class boast(models.Model):
    content =  models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    posted_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering=['-posted_at']
    
    def votescore(self):
        return self.upvotes - self.downvotes


class roast(models.Model):
    content =  models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    posted_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering=['-posted_at']
    
    def votescore(self):
        return self.upvotes - self.downvotes
