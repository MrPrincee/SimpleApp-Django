from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message = models.TextField(max_length=1000,null=False)
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
