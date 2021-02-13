"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_record_texts = texts[0]
incoming_numb_text = first_record_texts[0]
answering_numb_text = first_record_texts[1]
time_text = first_record_texts[2]

print("First record of texts, {incoming_number} texts {answering_number} at time {time}".format(
    incoming_number=incoming_numb_text, answering_number=answering_numb_text, time=time_text))


last_call = calls[-1]
incoming_numb_call = last_call[0]
answering_numb_call = last_call[1]
time_call = last_call[2]
during_call = last_call[3]

print(
    f"Last record of calls, {incoming_numb_call} calls {answering_numb_call} at time {time_call}, lasting {during_call} seconds")
