from django.db import models
from django.contrib.auth.models import User

class Citation(models.Model):
    """A citation created by a user"""
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    note = models.TextField()
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.title) > 50:
            return self.title[:50] + "..."
        else:
            return self.title
