import datetime

from django import forms

from .models import Booking, Vehicle


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_location', 'end_location', 'start_time', 'vehicle']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'start_location': forms.TextInput(attrs={'class': 'form-control'}),
            'end_location': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'start_location': 'Место отправления',
            'end_location': 'Место назначения',
            'start_time': 'Время отправления',
            'vehicle': 'Транспортное средство'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.all()
        self.fields['start_time'].initial = datetime.datetime.now()

    def calculate_price(self):
        start_location = self.cleaned_data.get('start_location')
        end_location = self.cleaned_data.get('end_location')
        vehicle = self.cleaned_data.get('vehicle')

        distance = self.get_distance(start_location, end_location)
        base_rate = 100  # Базовый тариф
        vehicle_rate = {
            'car': 1.0,
            'van': 1.5,
            'truck': 2.0,
        }
        price = base_rate * distance * vehicle_rate[vehicle.type]
        return price

    def get_distance(self, start_location, end_location):
        # В данном примере просто возвращаем фиксированное значение
        return 10


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)
