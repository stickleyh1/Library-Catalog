from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username

class Genre(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a media topic")
	def __str__(self):
		return self.name

class Media(models.Model):
	mediaType = models.CharField('Type',max_length=200, help_text="The type of the media", default="Book")
	title = models.CharField(max_length=200)
	isbn = models.CharField('ISBN', max_length=13, help_text="13 character ISBN number", blank=True)
	topic = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name="Topic")
	subtopics = models.ManyToManyField(Genre, help_text="Select the subtopics for this book")
	image = models.FileField(upload_to='images/', null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('media-detail', args=[str(self.id)])

class MediaInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this media")
	media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True)
	due_date = models.DateField(null=True, blank=True)
	rental_history = models.ManyToManyField(UserProfile, help_text="Select the past renters")
	borrower = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="Borrower")


	AVAILABILITY = (
		('a', 'Available'),
		('o', 'On Loan'),
	)

	status = models.CharField(max_length=1, choices=AVAILABILITY, blank=True, default='a', help_text="Media availability")

	class Meta:
		ordering = ["due_date"]

	def __str__(self):
		return '%s (%s)' % (self.id, self.media.title)