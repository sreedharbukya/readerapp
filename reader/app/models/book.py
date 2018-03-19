import logging

from django.db import models

from app.core.models import AuditFieldBasic
from app.models import Author
from app.models.reader import Reader

logger = logging.getLogger(__name__)


class Book(AuditFieldBasic):
	id = models.BigAutoField(primary_key=True, db_index=True)
	isbn_number = models.CharField(max_length=13, null=False, blank=False, verbose_name="ISBN Number", unique=True)
	title = models.CharField(max_length=100, verbose_name="Book Title")
	author = models.ManyToManyField(Author, blank=True, verbose_name="Authors")
	created_by = models.ForeignKey(Reader, verbose_name="Book created by")
	
	class Meta:
		verbose_name = "Book"
	
	def __unicode__(self):
		return u'{}-{}'.format(self.isbn_number, self.title)
	
	def to_dict(self):
		return {
			"isbn_number": self.isbn_number,
			"title": self.title,
			"creator": self.created_by.to_dict(),
			"created_at": self.created_at
		}
	
	def to_details(self):
		data_dict = {}
		
		try:
			if self.bookoverallrating:
				overall_rating = {
					"overall_rating": self.bookoverallrating.to_dict()
				}
				
				data_dict.update(overall_rating)
		except Exception as ex:
			logger.error("Error Occurred {}".format(ex.message))
		
		data_dict.update(self.to_dict())
		
		return data_dict
