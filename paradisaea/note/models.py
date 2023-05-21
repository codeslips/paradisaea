from django.db import models

def default_json():
   return []

class ListModel(models.Model):
    note_code = models.CharField(max_length=255, verbose_name="Note Code", unique = True, null = True)
    note_title = models.CharField(max_length=255, verbose_name="Note Title", default = '', null = True)
    note=models.TextField('note',default='', null = True)
    note_tags = models.JSONField(verbose_name="Tag", default=default_json, null = True)
    rating = models.IntegerField(verbose_name="rating", default=0, null=True)
    creater = models.CharField(max_length=255, verbose_name="Who Created", null = True, default = 'system')
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label', null = True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")
    class Meta:
        db_table = 'note'
        verbose_name = 'note'
        ordering = ['-update_time']

    def __str__(self):
        return self.note_code