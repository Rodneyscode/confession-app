from django.db import models

class AllConfessions (models.Model):
	confession = models.TextField(max_length=240, null = True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.confession


	
