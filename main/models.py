from django.db import models
from jalali_date import datetime2jalali, date2jalali
from django.core.validators import MaxLengthValidator


# ----------------------- General Models  -----------------------
class General(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        abstract = True

    def get_created_at(self):
        return datetime2jalali(self.created_at).strftime('%H:%M - %Y/%m/%d')
    get_created_at.short_description = 'تاریخ ایجاد'

    def get_updated_at(self):
        return datetime2jalali(self.updated_at).strftime('%H:%M - %Y/%m/%d')
    get_updated_at.short_description = 'آخرین بروزرسانی'
# ----------------------- end General Models  -----------------------