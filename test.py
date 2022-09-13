import datetime
import random

with open(r"C:\users\Me\desktop\random_dates.txt", "w", encoding="UTF-8") as file:
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2010, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    
    for i in range(20):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        file.writelines(str(random_date) + "\n")

print("done")
