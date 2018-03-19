from django.db import models

from app.core.models import AuditFieldBasic
from app.models import Reader, Book


class BookReview(AuditFieldBasic):
	id = models.BigAutoField(primary_key=True, db_index=True)
	review_by = models.ForeignKey(Reader, verbose_name="review_by")
	rating = models.PositiveIntegerField(default=1, verbose_name="rating value")
	comment = models.TextField(max_length=300, verbose_name="Comments about book")
	book = models.ForeignKey(Book, verbose_name="book details")
	
	class Meta:
		verbose_name = "Book Review"
		unique_together = ('review_by', 'book')
	
	def __unicode__(self):
		return u'{}-{}-{}'.format(self.review_by, self.book, self.rating)
	
	def to_dict(self):
		return {
			"book": self.book.to_details(),
			"rating": self.rating,
			"comment": self.comment,
			"review_by": self.review_by.to_dict()
		}
