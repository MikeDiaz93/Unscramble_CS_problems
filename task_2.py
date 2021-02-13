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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


list_numb = []
for i in range(0, len(texts)):
    list_numb.append(texts[i][0])
    list_numb.append(texts[i][1])

for i in range(0, len(calls)):
    list_numb.append(calls[i][0])
    list_numb.append(calls[i][1])

count = len(set(list_numb))

print(f"There are {count} different telephone numbers in the records.")
