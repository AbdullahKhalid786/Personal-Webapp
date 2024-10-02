from django import forms

class OptionPriceForm(forms.Form):
    stock_price = forms.FloatField(label='Current Stock Price (S)', required=True)
    strike_price = forms.FloatField(label='Strike Price (K)', required=True)
    time_to_maturity = forms.FloatField(label='Time to Expiration (T, in years)', required=True)
    volatility = forms.FloatField(label='Volatility (σ)', required=True)
    interest_rate = forms.FloatField(label='Risk-Free Interest Rate (r)', required=True)
    option_type = forms.ChoiceField(label='Option Type', choices=[
        ('call', 'Call Option'),
        ('put', 'Put Option')
    ])
