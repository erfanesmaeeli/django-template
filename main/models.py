from django.db import models
from datetime import datetime
from jalali_date import datetime2jalali, date2jalali


class General(models.Model):
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', null=True, blank=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    
    class Meta:
        abstract = True
    
    def get_created_at(self):
        return datetime2jalali(self.created_at).strftime("%H:%M - %Y/%m/%d")
    get_created_at.short_description = 'تاریخ ایجاد'

    def get_updated_at(self):
        return datetime2jalali(self.updated_at).strftime("%H:%M - %Y/%m/%d")
    get_updated_at.short_description = 'آخرین بروزرسانی'

    def get_created_at__date(self):
        today = datetime.today().date()
        if self.created_at.date() == today:
            return "امروز"
        return self.created_at.strftime("%Y/%m/%d")
    get_created_at.short_description = 'تاریخ ایجاد'

    def get_smart_created_at(self):
        now = datetime.now()
        time = now - self.created_at
        seconds = time.seconds
        minutes = int(seconds / 60)
        hours = int(minutes / 60)
        days = time.days

        if days > 0:
           return self.get_created_at()
        
        elif hours > 0:
            return f"{hours} ساعت پیش"

        elif minutes > 0:
            return f"{minutes} دقیقه پیش"

        else:
            return "به تازگی"