from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

STATUS = (
	(0,"Private"),
	(1,"Published")
)

class Post(models.Model):
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')

	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200) 	# Todo make keyword list!

	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now= True)
	status = models.IntegerField(choices=STATUS, default=0)

	content = models.TextField()

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
