from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=342)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return str(self.title) + " | " + str(self.author)

    def get_absolute_url(self):
        # return reverse("blog-detail", kwargs={"pk": self.pk})
        return reverse("home")
