from flask import Flask, redirect, url_for, request, render_template,session,flash
import requests, pdb
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes


app=Flask(__name__)
app.secret_key='thisisasecret'
app.config['SECRET_KEY'] = "thisisasecret"

debug = DebugToolbarExtension(app)

@app.route('/', methods=["POST", "GET"])
def home():
    print("this is a test")
    if request.method == "POST":
    #setting values and getting values from start.html
        # return render_template('result.html')
        amount = request.form.get('amount')
        converting_from = request.form.get('converter-from')
        converting_to = request.form.get('converter-to')
                
        print(amount)
        print(converting_from)
        print(converting_to)
        #flash and stop if symbols are not valid (make sure to upper them)
       
        if not is_valid_currency(converting_from ):
            flash(f"Invalid currency code: {converting_from}")
            return redirect(url_for('home'), 'error')
        if not is_valid_currency(converting_to):
            flash(f"Invalid currency code: {converting_to}")
            return redirect(url_for('home'), 'error')
        try:
            amount = float(amount)
        except ValueError:
            error_msg = f"Invalid amount: {amount}"
            return redirect('start.html', error_msg=error_msg)
        
        #converting currencies
        url = f"https://api.exchangerate.host/convert?from={converting_from}&to={converting_to}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        
        exchange_rate = data['result']
        print(exchange_rate)

        

        # Display the result to the user
        result = f"{exchange_rate}"
        session[result] = result
        print(result)
        return render_template('result.html', result=result)
    return render_template('start.html')

def is_valid_currency(currency_code):
    api_url = f"https://api.exchangerate.host/symbols"
    response = requests.get(api_url)
    if response.status_code != 200:
        return False
    data = response.json()
    if 'symbols' not in data:
        return False
    return currency_code in data['symbols']


@app.route('/result')
def result():
    result = session.get('result')
    return render_template('result.html', result=result)