import logging

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.core.models import AuditFieldBasic
from app.models import BookReview
from app.models.book import Book

logger = logging.getLogger(__name__)


@receiver(post_save, sender=BookReview)
def update_book_overall_rating(sender, instance, **kwargs):
	print ("Overall rating changed")
	
	overall_rating, status = BookOverAllRating.objects.get_or_create(book=instance.book)

	
	if status:
		logging.info("New rating received")
		overall_rating.total_sum = instance.rating
		overall_rating.total_count = 1
		overall_rating.save()
	else:
		logging.info("New rating updated")
		overall_rating.total_sum = overall_rating.total_sum + instance.rating
		overall_rating.total_count = overall_rating.total_count + 1
		overall_rating.save()


class BookOverAllRating(AuditFieldBasic):
	id = models.BigAutoField(primary_key=True, db_index=True)
	book = models.OneToOneField(Book, verbose_name="Book")
	total_sum = models.FloatField(default=0.0, verbose_name="Total Sum")
	total_count = models.PositiveIntegerField(default=0, verbose_name="Total Rating Count")
	
	def __unicode__(self):
		return u"{}-{}-{}".format(self.book, self.average(), self.total_count)
	
	def average(self):
		if self.total_sum and self.total_count:
			return self.total_sum / self.total_count
		else:
			return 0
	
	def to_dict(self):
		return {
			"average": self.average(),
			"total_sum": self.total_sum,
			"total_count": self.total_count,
			"last_review": self.updated_at
		}
