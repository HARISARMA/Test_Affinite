from __future__ import unicode_literals

from django.db import models

GENDER_CHOICES = (
    ('MALE', "Male"),
    ('FEMALE', "Female")
    )


class ShoeDetails(models.Model):
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='MALE')
	featured_image = models.ImageField(upload_to="images")
	price = models.FloatField()

	def __unicode__(self):
		return self.name
