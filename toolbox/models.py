
from django.db import models

class Tool(models.Model):
	slug = models.SlugField(unique=True)
	name = models.CharField(max_length=200)
	summary = models.TextField(blank=True)
	website = models.URLField(blank=True, null=True)
	categories = models.JSONField(default=list, blank=True)
	content_html = models.TextField()
	content_markdown_path = models.CharField(max_length=300)

	def __str__(self):
		return self.name


class Resource(models.Model):
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=200)
	summary = models.TextField(blank=True)
	categories = models.JSONField(default=list, blank=True)
	content_html = models.TextField()
	source_file = models.CharField(max_length=300)
	source_format = models.CharField(max_length=20)

	def __str__(self):
		return self.title
