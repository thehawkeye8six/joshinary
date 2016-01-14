import datetime

from django.db import models

from django.utils import timezone

class Word(models.Model):
	id = models.AutoField(primary_key=True)
	word = models.CharField(db_index=True,max_length=255)
	short_definition = models.CharField(max_length=255)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	long_definition = models.TextField()

	def __str__(self):
		return self.word

	def was_created_recently(self):
		return self.created_date >= timezone.now() - datetime.timedelta(days=1)

	def was_updated_recently(self):
		return self.updated_date >= timezone.now() - datetime.timedelta(days=1)
