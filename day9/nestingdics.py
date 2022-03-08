travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    }, 
    {
        "country" : "Germany", 
        "visits" : 14,
        "cities" : ["Berlin", "Hamburg", "Cologne"]
    }
]


def add_new_country(name, times_visited, cities):
    travel_log.append({"country" : name, 
                       "visits" : times_visited, 
                       "cities" : cities
                       })
    


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)