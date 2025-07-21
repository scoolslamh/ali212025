from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان التقرير')
    generated_on = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات')

    def __str__(self):
        return self.title
