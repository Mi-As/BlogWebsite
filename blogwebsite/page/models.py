from django.db import models
from django.core.exceptions import ValidationError

LANGUAGE_CODE = (
	("en","english"),
	("de","deutsch"),
	("pt","português"),
	("es","español"),
	("ru","русский")
)

# creating a validator function
def custom_slug_validator(value):
    if value in ["blog", "admin", ""]:
        raise ValidationError("This slug is not allowed!")
    else:
        return value

class Page(models.Model):
	slug = models.SlugField(max_length=200, unique=True, validators=[custom_slug_validator])

	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	language_code = models.CharField(max_length=2, choices=LANGUAGE_CODE, default="en")

	content = models.TextField()

	def __str__(self):
		return self.title