import sqlite3
conn = sqlite3.connect("userdata.db")

create_table_query = """
create table userecord (age integer,flight_distance integer,inflight_entertainment integer,baggage_handling integer,cleanliness integer,
                        departure_delay integer,arrival_delay integer,gender integer,customer_type integer,travel_type integer,class_eco integer,class_eco_plus integer,predictation integer)
"""

cur = conn.cursor() # temprory memory
cur.execute(create_table_query)
print("Table created !")
cur.close()
conn.close()