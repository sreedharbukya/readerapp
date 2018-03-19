import uuid

from django.db import models


class Reader(models.Model):
	id = models.BigAutoField(primary_key=True, db_index=True)
	uuid = models.CharField(editable=False, unique=True, max_length=40, db_index=True, verbose_name="UUID")
	username = models.CharField(max_length=30, verbose_name="username", unique=True)
	first_name = models.CharField(max_length=60, verbose_name="First Name")
	last_name = models.CharField(max_length=60, verbose_name="Last Name")
	email = models.EmailField(max_length=60, blank=True, null=True)
	phone_number = models.CharField(max_length=15, blank=True, null=True)
	is_active = models.BooleanField(default=False, verbose_name="Is Active")
	
	class Meta:
		verbose_name = "Reader"
	
	def __unicode__(self):
		return u'{}-{}-{}'.format(self.id, self.first_name, self.last_name)
	
	def to_dict(self):
		return {
			"first_name": self.first_name,
			"last_name": self.last_name,
			"username": self.username,
			"email": self.email,
			"phone_number": self.phone_number,
			"is_active": self.is_active,
			"uuid": self.uuid
		}
	
	def save(self, *args, **kwargs):
		if self.id is None:
			self.uuid = uuid.uuid4()
		
		return super(Reader, self).save(*args, **kwargs)
