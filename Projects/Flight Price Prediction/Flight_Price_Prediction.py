import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load('Flight_Model.lb')

duration = int(input("\nEnter the Duration of Flight (in hours): "))
days_left = int(input("\nEnter the number of Days Left: "))

print('\nSelect Airline:')
print('1. AirAsia')
print('2. Air India')
print('3. Go First')
print('4. Indigo')
print('5. SpiceJet')
print('6. Vistara')
airline = int(input("Enter Airline (1-6): "))
airline_AirAsia = airline_Air_India = airline_GO_FIRST = airline_Indigo = airline_SpiceJet = airline_Vistara = 0
if airline == 1:
    airline_AirAsia = 1
elif airline == 2:
    airline_Air_India = 1
elif airline == 3:
    airline_GO_FIRST = 1
elif airline == 4:
    airline_Indigo = 1
elif airline == 5:
    airline_SpiceJet = 1
elif airline == 6:
    airline_Vistara = 1
else:
    print("Invalid choice, defaulting to Vistara.")
    airline_Vistara = 1

print('\nSelect Source City:')
print('1. Bangalore')
print('2. Chennai')
print('3. Delhi')
print('4. Hyderabad')
print('5. Kolkata')
print('6. Mumbai')
source = int(input("Enter Source City (1-6): "))
source_city_Bangalore = source_city_Chennai = source_city_Delhi = source_city_Hyderabad = source_city_Kolkata = source_city_Mumbai = 0
if source == 1:
    source_city_Bangalore = 1
elif source == 2:
    source_city_Chennai = 1
elif source == 3:
    source_city_Delhi = 1
elif source == 4:
    source_city_Hyderabad = 1
elif source == 5:
    source_city_Kolkata = 1
elif source == 6:
    source_city_Mumbai = 1
else:
    print("Invalid choice, defaulting to Mumbai.")
    source_city_Mumbai = 1

print('\nSelect Departure Time:')
print('1. Afternoon')
print('2. Early Morning')
print('3. Evening')
print('4. Late Night')
print('5. Morning')
print('6. Night')
departure_time = int(input("Enter Departure Time (1-6): "))
departure_time_Afternoon = departure_time_Early_Morning = departure_time_Evening = departure_time_Late_Night = departure_time_Morning = departure_time_Night = 0
if departure_time == 1:
    departure_time_Afternoon = 1
elif departure_time == 2:
    departure_time_Early_Morning = 1
elif departure_time == 3:
    departure_time_Evening = 1
elif departure_time == 4:
    departure_time_Late_Night = 1
elif departure_time == 5:
    departure_time_Morning = 1
elif departure_time == 6:
    departure_time_Night = 1
else:
    print("Invalid choice, defaulting to Morning.")
    departure_time_Morning = 1

print('\nSelect Arrival Time:')
print('1. Afternoon')
print('2. Early Morning')
print('3. Evening')
print('4. Late Night')
print('5. Morning')
print('6. Night')
arrival_time = int(input("Enter Arrival Time (1-6): "))
arrival_time_Afternoon = arrival_time_Early_Morning = arrival_time_Evening = arrival_time_Late_Night = arrival_time_Morning = arrival_time_Night = 0
if arrival_time == 1:
    arrival_time_Afternoon = 1
elif arrival_time == 2:
    arrival_time_Early_Morning = 1
elif arrival_time == 3:
    arrival_time_Evening = 1
elif arrival_time == 4:
    arrival_time_Late_Night = 1
elif arrival_time == 5:
    arrival_time_Morning = 1
elif arrival_time == 6:
    arrival_time_Night = 1
else:
    print("Invalid choice, defaulting to Morning.")
    arrival_time_Morning = 1

print('\nSelect Destination City:')
print('1. Bangalore')
print('2. Chennai')
print('3. Delhi')
print('4. Hyderabad')
print('5. Kolkata')
print('6. Mumbai')
destination = int(input("Enter Destination City (1-6): "))
destination_city_Bangalore = destination_city_Chennai = destination_city_Delhi = destination_city_Hyderabad = destination_city_Kolkata = destination_city_Mumbai = 0
if destination == 1:
    destination_city_Bangalore = 1
elif destination == 2:
    destination_city_Chennai = 1
elif destination == 3:
    destination_city_Delhi = 1
elif destination == 4:
    destination_city_Hyderabad = 1
elif destination == 5:
    destination_city_Kolkata = 1
elif destination == 6:
    destination_city_Mumbai = 1
else:
    print("Invalid choice, defaulting to Mumbai.")
    destination_city_Mumbai = 1

print('\nSelect Number of Stops:')
print('1. Zero Stops')
print('2. One Stop')
print('3. Two or More Stops')
stops = int(input("Enter Number of Stops (1-3): "))
stops_zero = stops_one = stops_two_or_more = 0
if stops == 1:
    stops_zero = 1
elif stops == 2:
    stops_one = 1
elif stops == 3:
    stops_two_or_more = 1
else:
    print("Invalid choice, defaulting to Zero Stops.")
    stops_zero = 1

print('\nSelect Class:')
print('1. Economy')
print('2. Business')
flight_class = int(input("Enter Class (1-2): "))
class_Economy = class_Business = 0
if flight_class == 1:
    class_Economy = 1
elif flight_class == 2:
    class_Business = 1
else:
    print("Invalid choice, defaulting to Economy.")
    class_Economy = 1

input = [duration, days_left, airline_AirAsia,
            airline_Air_India, airline_GO_FIRST, airline_Indigo,
            airline_SpiceJet, airline_Vistara, source_city_Bangalore,
            source_city_Chennai, source_city_Delhi, source_city_Hyderabad,
            source_city_Kolkata, source_city_Mumbai, departure_time_Afternoon,
            departure_time_Early_Morning, departure_time_Evening,
            departure_time_Late_Night, departure_time_Morning,
            departure_time_Night, stops_one, stops_two_or_more, stops_zero,
            arrival_time_Afternoon,arrival_time_Early_Morning,
            arrival_time_Evening, arrival_time_Late_Night,
            arrival_time_Morning, arrival_time_Night,
            destination_city_Bangalore, destination_city_Chennai,
            destination_city_Delhi, destination_city_Hyderabad,
            destination_city_Kolkata, destination_city_Mumbai, class_Business,
            class_Economy]

prediction = int(model.predict([input]))

print("\n\nThe Cost : ₹",prediction,"\n\n")
