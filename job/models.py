from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# for DB

"""
    django model field :
        - html widget
        - validation
        - DB size   
"""

# choices in Job class
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)


# upload images with special names and save in special folders
def image_upload(instance, filename):
    imageName, extension = filename.split('.')
    return "jobs/%s/%s.%s"%(instance.id, instance.id, extension)


class Job(models.Model): # table
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # column
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True) # auto_now is (hidden) in admin page
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    # one to many Relation in DB
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

    image = models.ImageField(upload_to=image_upload)
    

    # slug = models.SlugField()

    # to return title of job at any new user
    def __str__(self):
        return self.title

# one to many Relation in DB
class Category(models.Model): # table
    name = models.CharField(max_length=20)

    # to return CategoryName of any job
    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name