import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import BlogPost


class BlogPostModelTests(TestCase):

    def test_was_published_recently_with_future_blogpost(self):
        """
        was_published_recently() returns False for blog posts whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_blogpost = BlogPost(pub_date=time)
        self.assertIs(future_blogpost.was_published_recently(), False)

    def test_was_published_recently_with_old_blogpost(self):
        """
        was_published_recently() returns False for blogpost whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_blogpost = BlogPost(pub_date=time)
        self.assertIs(old_blogpost.was_published_recently(), False)

    def test_was_published_recently_with_recent_blogpost(self):
        """
        was_published_recently() returns True for blogpost whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_blogpost = BlogPost(pub_date=time)
        self.assertIs(recent_blogpost.was_published_recently(), True)

def create_blogpost(blogpost_text, days):
    """
    Create a blogpost with the given `blogpost_text` and published the
    given number of `days` offset to now (negative for blogpost published
     in the past, positive for blogpost that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return BlogPost.objects.create(blogpost_text=blogpost_text, pub_date=time)


class BlogPostIndexViewTests(TestCase):
    def test_no_blogpost(self):
        """
        If no blogpost exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No blogposts are available.")
        self.assertQuerysetEqual(response.context['latest_blogpost_list'], [])

    def test_past_blogpost(self):
        """
        blogposts with a pub_date in the past are displayed on the
        index page.
        """
        blogpost = create_blogpost(blogpost_text="Past blogpost.", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_blogpost_list'],
            [blogpost],
        )

    def test_future_blogpost(self):
        """
        blogposts with a pub_date in the future aren't displayed on
        the index page.
        """
        create_blogpost(blogpost_text="Future blogpost.", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "No blogposts are available.")
        self.assertQuerysetEqual(response.context['latest_blogpost_list'], [])

    def test_future_blogpost_and_past_blogpost(self):
        """
        Even if both past and future blogposts exist, only past blogposts
        are displayed.
        """
        blogpost = create_blogpost(blogpost_text="Past blogpost.", days=-30)
        create_blogpost(blogpost_text="Future blogpost.", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_blogpost_list'],
            [blogpost],
        )

    def test_two_past_blogposts(self):
        """
        The blogposts index page may display multiple blogposts.
        """
        blogpost1 = create_blogpost(blogpost_text="Past blogpost 1.", days=-30)
        blogpost2 = create_blogpost(blogpost_text="Past blogpost 2.", days=-5)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_blogpost_list'],
            [blogpost2, blogpost1],
        )

class BlogPostDetailViewTests(TestCase):
    def test_future_blogpost(self):
        """
        The detail view of a blogpost with a pub_date in the future
        returns a 404 not found.
        """
        future_blogpost = create_blogpost(blogpost_text='Future blogpost.', days=5)
        url = reverse('blog:detail', args=(future_blogpost.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_blogpost(self):
        """
        The detail view of a blogpost with a pub_date in the past
        displays the blogpost's text.
        """
        past_blogpost = create_blogpost(blogpost_text='Past blogpost.', days=-5)
        url = reverse('blog:detail', args=(past_blogpost.id,))
        response = self.client.get(url)
        self.assertContains(response, past_blogpost.blogpost_text)