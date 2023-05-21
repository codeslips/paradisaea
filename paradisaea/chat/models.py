from django.db import models

class ListModel(models.Model):
    sender = models.CharField(max_length=100, verbose_name='Sender', default="")
    receiver = models.CharField(max_length=100, verbose_name='Receiver', default="")
    read = models.BooleanField(default=False, verbose_name="Readed")
    detail = models.CharField(max_length=100, verbose_name='Chat text', default="")
    is_delete = models.BooleanField(default=False, verbose_name='Delete label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Update time')

    class Meta:
        db_table = 'chat'
        verbose_name = 'Chat'
        verbose_name_plural = "Chat"
        ordering = ['-update_time']

    def __str__(self):
        return self.sender
