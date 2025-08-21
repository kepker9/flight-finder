import datetime
from functions.cheapest_dates import all_dates_rt, cheapest_dates
from functions.best_airport_to_fly import (best_airport_to_fly_from, best_airport_to_fly_from_rt,
                                            best_airport_to_fly_to, best_airport_to_fly_to_rt)



the_date = datetime.date(2025, 11, 1 )

#best_airport_to_fly_from (['Bucharest', 'Warsaw', 'Krakow', 'Budapest', 'Prague'],'JFK',the_date)

cheapest_dates('Bucharest',
                             'New York',
                             the_date,
                             25)


