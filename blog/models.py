from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        # Determines what you see when blogs are listed in /admin
        return self.title + '  [ ' + self.text[:20] + ' ... ]'
