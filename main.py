#Place to test all the functions

import datetime
from functions.cheapest_dates import all_dates_rt, cheapest_dates
from functions.best_airport_to_fly import (best_airport_to_fly_from, best_airport_to_fly_from_rt,
                                            best_airport_to_fly_to, best_airport_to_fly_to_rt)



the_date = datetime.date(2026, 1, 18 )

#best_airport_to_fly_from (['Bucharest', 'Warsaw', 'Krakow', 'Budapest', 'Prague'],'JFK',the_date)

best_airport_to_fly_from (['Bucharest', 'Krakow', 'Warsaw', 'Viena', 'Budapest', 'prague'], 'BOS', the_date)


