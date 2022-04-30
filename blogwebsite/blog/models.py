from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

STATUS = (
	(0,"Private"),
	(1,"Published")
)

LANGUAGE_CODE = (
	("en","english"),
	("de","deutsch"),
	("pt","português"),
	("es","español"),
	("ru","русский")
)

class Post(models.Model):
	slug = models.SlugField(max_length=254, unique=True, primary_key=True)
	author = models.ForeignKey(User, on_delete= models.PROTECT,related_name='blog_posts')

	title = models.CharField(max_length=254)
	description = models.CharField(max_length=254)
	keywords = models.CharField(max_length=254) 	# Todo make keyword list!
	language_code = models.CharField(max_length=2, choices=LANGUAGE_CODE, default="en")

	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now= True)
	status = models.IntegerField(choices=STATUS, default=0)

	content = models.TextField()

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	parent_id = models.IntegerField(default=-1)
	post_slug = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='blog_comments')

	name = models.CharField(max_length=256, default="Anonymous")
	email = models.EmailField(max_length=256)
	created_on = models.DateTimeField(auto_now_add=True)

	content  = models.TextField(validators=[
		MinLengthValidator(2, 'at least 2 characters')])
	votes = models.IntegerField(default=0)


