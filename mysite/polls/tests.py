from django.test import TestCase
import datetime 
from django.utils import timezone
from .models import Question
from django.urls import reverse
def create_question(question_text, days):
	pub_date = timezone.now() + datetime.timedelta(days = days)
	return Question.objects.create(pub_date = pub_date, question_text = question_text)
class QuestionModelTests(TestCase):
	def test_was_published_older_than_day(self):
		time = timezone.now() + datetime.timedelta(days = 1, seconds = 1)
		old_question = Question(pub_date = time)
		self.assertIs(old_question.was_published_recently(), False)
	def test_was_published_recently(self):
		time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
		recent_question = Question(pub_date = time)
		self.assertIs(recent_question.was_published_recently(), True)
	def test_Was_published_recently_with_future_question(self):
		time =timezone.now() + datetime.timedelta(days = 30)
		future_question = Question(pub_date = time)
		self.assertIs(future_question.was_published_recently(), False)