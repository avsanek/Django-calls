from django import forms

from .models import Book


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('PustotaA', 'Tel1B','Tel2C', 'Typ_zvonkaD', 'KtoE', 'SIPF', 'SIPG', 'StatusH','SIPI' ,'TimeStartJ','TimeMidK','TimeFFL','Number1M','Number2N','StateO','DocP','IdQ')
        labels = {
            'PustotaA' : 'ПустотаA' ,'Tel1B' : 'Телефон1B' ,'Tel2C' : 'Телефон2C' ,
            'Typ_zvonkaD' : 'Тип звонкаD' ,'KtoE' : 'Кто звонилE' ,'SIPF' : 'SIPF' , 'SIPG' : 'SIPG' ,
            'StatusH' : 'Статус' ,'SIPI' : 'SIPI' , 'TimeStartJ' : 'Начало звонка', 'TimeMidK' : 'Перераспределение' , 'TimeFFL' : 'Конец звонка' ,
            'Number1M': 'Число 1', 'Number2N': 'Число 2','StateO': 'Статус', 'DocP': 'Док', 'IdQ': 'Id'
        }



