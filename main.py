from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()


sheet_data = data_manager.get_destination_data()
print(sheet_data)


tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")

iataCode = 'iataCode'
lowestPrice = 'lowestPrice'

for destination in sheet_data:
    # update the city with correct IATA codes
    if iataCode not in destination or destination[iataCode] == '':
        destination[iataCode] = flight_search.get_destination_code(destination['city'])
        data_manager.update_destination_code(destination[iataCode], destination['id'])
    # check for flight for that destination
    flight = flight_search.check_flights(
        departure_city_code='LON',
        destination_city_code=destination['iataCode'],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    
    if flight:

        if lowestPrice not in destination or destination[lowestPrice] == '':
            data_manager.update_price(flight.price, destination['id'])

        elif flight.price < destination[lowestPrice]:
            destination[lowestPrice] = flight.price
            data_manager.update_price(destination[lowestPrice], destination['id'])
            notification_manager.send_sms(
                text=f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.departure_date} to {flight.return_date}."
            )











