from django.db import models





class Book(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    PustotaA = models.CharField(max_length=50)
    Tel1B = models.CharField(max_length=100)
    Tel2C = models.CharField(max_length=100)
    typ1 = 'cisco-voice-gateway'
    typ2 = 'inside-users'
    typ3 = 'longdistance'
    YEAR_IN_SCHOOL_CHOICES = [
        (typ1, 'cisco-voice-gateway'),
        (typ2, 'inside-users'),
        (typ3, 'longdistance'),
    ]
    Typ_zvonkaD = models.CharField(max_length=100,choices=YEAR_IN_SCHOOL_CHOICES,)
    KtoE = models.CharField(max_length=100)
    SIPF = models.CharField(max_length=100)
    SIPG = models.CharField(max_length=100)
    StatusH = models.CharField(max_length=100)
    SIPI = models.CharField(max_length=100)
    # TimeStartJ = models.CharField(max_length=100)
    TimeStartJ = models.DateTimeField(max_length=100, null = True)
    TimeMidK = models.CharField(max_length=100)
    TimeFFL = models.DateTimeField(max_length=100, null = True)
    Number1M = models.CharField(max_length=100)
    Number2N = models.CharField(max_length=100)
    StateO = models.CharField(max_length=100)
    DocP = models.CharField(max_length=100)
    IdQ = models.CharField(max_length=100)
    TimeStartJ2 = models.DateField()

    def __str__(self):
        return f'Id {self.id}: {self.KtoE}'

    # pdf = models.FileField(upload_to='books/pdfs/')
    #
    #
    # Contr_ID = models.IntegerField(null = True)
    # ContrN = models.CharField(max_length=10)
    # Uch_ID = models.IntegerField(null = True) #ограничение длинные int игнорится
    # AttachType = models.CharField(max_length=30, null = True)
    # Attachimage = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    # AttachDate = models.DateField(default=timezone.now)
    # MainAttach_ID =models.IntegerField(null = True)  #ограничение длинные int игнорится
    # Note = models.CharField(max_length=255, null = True, blank=True)
    # '''STATUS_CHOICES = [
    # ('new', 1),
    # ('old', 2),
    # ('redacted', 3)
    # ]
    # Status = models.IntegerField(
    #     choices= STATUS_CHOICES,
    #     default= 'new')'''
    # Status = models.IntegerField(default = 1)
    # EditDate = models.DateField(default=timezone.now)
    # Contr = models.IntegerField(null = True)
    # City = models.CharField(max_length=255, null = True)
    # Naim_Potr = models.CharField(max_length=255, null = True)
    # TY = models.CharField(max_length=255, null = True)
    # pdff = models.FileField(upload_to='books/pdfs/' , null = True)
    #
    #
    # def __str__(self):
    #     return self.ContrN
    #
    # def delete(self, *args, **kwargs):
    #     self.pdf.delete()
    #     super().delete(*args, **kwargs)



