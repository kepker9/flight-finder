from bs4 import BeautifulSoup
import requests
import datetime

def best_airport_to_fly_to_rt (airport_from: str,
        list_of_airports: list[str],
        start_date: datetime.date,
        end_date: datetime.date):
    for airport_to in list_of_airports:
        link = (f'https://www.google.com/travel/flights?q=Flights%20to'
                f'%20{airport_to}%20from%20{airport_from}%20on%20{start_date}'
                f'%20through%20{end_date}&curr=USD')
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        price = soup.find('div', class_='YMlIz FpEdX jLMuyc')

        print(f'From {airport_from}, prices start from {price.text}')

def best_airport_to_fly_to (airport_from: str,
        list_of_airports: list[str],
        date: datetime.date):
    for airport_to in list_of_airports:
        link = (f'https://www.google.com/travel/flights?q=Flights%20'
                f'to%20{airport_to}%20from%20{airport_from}%20'
                f'on%20{date}%20oneway&curr=USD')
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        price = soup.find('div', class_='YMlIz FpEdX jLMuyc')

        print(f'From {airport_from}, prices start from {price.text}')


def best_airport_to_fly_from_rt (list_of_airports: list[str],
                         airport_to: str,
                         start_date: datetime.date,
                        end_date: datetime.date):
    result_lines = []

    for airport_from in list_of_airports:
        link = (f'https://www.google.com/travel/flights?q=Flights%20to'
                f'%20{airport_to}%20from%20{airport_from}%20on%20{start_date}'
                f'%20through%20{end_date}&curr=USD')
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        price = soup.find('div', class_='YMlIz FpEdX jLMuyc')

        if price:  # make sure it's found
            result_lines.append(f'✈️ From {airport_from}: prices start from {price.text}')
        else:
            result_lines.append(f'✈️ From {airport_from}: price not found')

    final_message = "\n".join(result_lines)

    return final_message



def best_airport_to_fly_from (list_of_airports: list[str],
                         airport_to: str,
                         date: datetime.date) -> str:
    result_lines = []

    for airport_from in list_of_airports:
        link = (f'https://www.google.com/travel/flights?q=Flights%20'
                f'to%20{airport_to}%20from%20{airport_from}%20'
                f'on%20{date}%20oneway&curr=USD')
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        price = soup.find('div', class_='YMlIz FpEdX jLMuyc')

        if price:  # make sure it's found
            result_lines.append(f'✈️ From {airport_from}: prices start from {price.text}')
        else:
            result_lines.append(f'✈️ From {airport_from}: price not found')

    final_message = "\n".join(result_lines)

    return final_message
