from django.db import models

from app.core.models import AuditFieldBasic


class Author(AuditFieldBasic):
	id = models.BigAutoField(db_index=True, primary_key=True)
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	
	class Meta:
		verbose_name = "Author"
		unique_together = ('first_name', 'last_name')
	
	def __unicode__(self):
		return u'Author : {}-{}'.format(self.id, self.first_name)
