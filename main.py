import datetime
from functions.cheapest_dates import all_dates_rt, all_dates
from functions.best_airport_to_fly import (best_airport_to_fly_from, best_airport_to_fly_from_rt,
                                            best_airport_to_fly_to, best_airport_to_fly_to_rt)



the_date = datetime.date(2025, 11, 16)

all_dates_rt('WAW',
             'Kigali',
                             the_date,
                             5,
             3)




