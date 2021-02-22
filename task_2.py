"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

totals = dict()
for call in calls:
    phone_caller = call[0]
    phone_reciever = call[1]
    duration_call = int(call[3])

    if phone_caller in totals:
        totals[phone_caller] += int(duration_call)
    else:
        totals[phone_caller] = int(duration_call)

    if phone_reciever in totals:
        totals[phone_reciever] += duration_call
    else:
        totals[phone_reciever] = duration_call

lngst_time_phone = max(totals.items(), key=lambda x: int(x[1]))

print(f"{lngst_time_phone [0]} spent the longest time, {lngst_time_phone [1]} \
seconds, on the phone during September 2016.")
