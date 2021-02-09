from django.db import models

# Create your models here.
# for DB

"""
    django model field :
        - html widget
        - validation
        - DB size   
"""

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)

class Jop(models.Model): # table
    title = models.CharField(max_length=100) # column
    # location
    jop_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True) # auto_now is (hidden) in admin page
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    # to return title of job at any new user
    def __str__(self):
        return self.title


