from bs4 import BeautifulSoup
import requests
import datetime


#cheapest day for {length_of_trip} long round trip flight
def all_dates_rt(airport_from: str,
                             airport_to: str,
                             the_date: datetime.date,
                             length_of_trip: int,
                             analyze_prices_for: int):
    output: str = f''
    for i in range(analyze_prices_for):
        start_date = the_date + datetime.timedelta(days=i)
        end_date = start_date + datetime.timedelta(days=length_of_trip)
        link = (f'https://www.google.com/travel/flights?q=Flights%20to'
                f'%20{airport_to}%20from%20{airport_from}%20on%20{start_date}'
                f'%20through%20{end_date}&curr=USD')
        html_text = requests.get(link).text

        soup = BeautifulSoup(html_text, 'lxml')

        price = soup.find('div', class_='YMlIz FpEdX jLMuyc')

        try:
            output = output + f'On {start_date} prices start from {price.text}\n'
        except Exception as e:
            output = output + f'Error occured trying to find flights on {start_date}\n'

    print(output)

#cheapest day for one-way flight
def cheapest_dates(airport_from: str,
                             airport_to: str,
                             the_date: datetime.date,
                             analyze_prices_for: int):
    flights = []
    for i in range(analyze_prices_for):
        start_date = the_date + datetime.timedelta(days=i)
        link = (f'https://www.google.com/travel/flights?q=Flights%20'
                f'to%20{airport_to}%20from%20{airport_from}%20'
                f'on%20{start_date}%20oneway&curr=USD')
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')

        price = soup.find('div', class_='YMlIz FpEdX jLMuyc')

        try:
            flights.append({
                "date": f'{start_date}',
                "price": int(price.text.replace("$", "")),
                "link": link
            })
        except Exception as e:
            continue
    flights = sorted(flights, key=lambda x: x["price"])
    cheapest_flights = flights[:5]
    for flight in cheapest_flights:
        print(f'Date: {flight['date']}, Price: ${flight['price']}, Link: {flight["link"]}')