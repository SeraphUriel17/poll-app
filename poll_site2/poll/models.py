import datetime
from django.db import models
from django.utils import timezone
from flask import request
from accounts.models import profile

class poll_number(models.Model):
        profile = models.ForeignKey(profile, on_delete=models.CASCADE)
        poll_id = models.IntegerField()

        
        def __init__(self, *args, **kwargs):
            self.profile = request.user.profile
        
        def __str__(self):
            return self.poll_id

class Poll(models.Model):
    question = models.TextField()
    user_id = models.IntegerField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    
    def __init__(self, *args, **kwargs):
        super(Poll, self).__init__(*args, **kwargs)
        self.pub_date = timezone.now()
        #self.user_id = request.user.id
        poll_num = poll_number.objects.create()
        poll_num.poll_id = self.id
    
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count
    
    def was_published_recently(self):
        return (timezone.now() >= self.pub_date >= (timezone.now() - datetime.timedelta(days=1)))
    
    def __str__(self):
        return self.question
    
    
