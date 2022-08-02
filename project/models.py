from django.db import models
from django.forms import ImageField
from django.utils.text import slugify



class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

	

class Project(models.Model):
	title = models.CharField(max_length=200)
	sub_title = models.CharField(max_length=200, null=True, blank=True)
	front_page = models.ImageField(null=True, blank=True, upload_to="images", default="images/broken-image.png")
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	skills = models.ManyToManyField(Skill, null=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title
	
	def save(self, *args, **kwargs):
    
		if self.slug == None:
			slug = slugify(self.title)

			has_slug = Project.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.title) + '-' + str(count) 
				has_slug = Project.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)


