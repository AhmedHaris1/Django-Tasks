from django.test import TestCase

import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently returns false for dates set in future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently retuns false for dates set older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_with_recent_question(self):
        """
        was_published_recently return true for dates set within timeframe of 1 day
        """
        time = timezone.now() -datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(text, days):
    """
    a function for creating questions in our test class for testing different scenarios
    use +ve days for future dates
    use -ve days for past dates
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """
        if no questions exists, an appropriate text appears
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        question with past pub_date are displayed on index page
        """
        question = create_question("Past Question", -30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        """
        question with future pub_date should not be published
        """
        question = create_question("Future Question", 30)
        response = self.client.get(reverse("polls:index"))
        # self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_and_past_question(self):
        """
        display only the past question even having both past and future question
        """
        past_question = create_question("Past Question", -30)
        future_question = create_question("Future Question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question]
        )

    def test_two_past_question(self):
        """
        displaying both past questions in the right order
        """
        question1 = create_question("question 1", -30)
        question2 = create_question("question 2", -5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], 
            [question2, question1]
        )

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        question = create_question("Future question.", 5)
        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        question = create_question("Past Question", -5)
        url = reverse("polls:detail", args=(question.id,))
        respone = self.client.get(url)
        self.assertContains(respone, question.question_text)