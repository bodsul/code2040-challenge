#import library for making HTTP requests
import requests

#import library for converting python objects to JSON format
import json

#import object from library to convert ISO date to python date format
import dateutil.parser as parser

#import object from library to add dates in python format
from datetime import timedelta


#initialize  parameters
email = "sule1@illinois.edu"
github = "https://github.com/bodsul/code2040-challenge"
url = "http://challenge.code2040.org/api/register"
input = {"email": email, "github": github}

#convert input to JSON format
json_input = json.dumps(input)

#use post method of request library to make request
value = requests.post(url, data = json_input)

#print and save returned object
print "returned value is: ", value.text
my_return = value.json()

#extract string from returned dict
my_token = my_return.values()[0]
json_token = json.dumps({"token": my_token})

#I.Reverse a string

#initialize url to get string 
url = "http://challenge.code2040.org/api/getstring"

value = requests.post(url, data = json_token)
my_string = value.json()
my_string_value = my_string.values()[0]

#reverse string using standard python method
my_string_reversed = my_string_value[::-1]

#return reversed string
json_answer = json.dumps({"token": my_token, "string": my_string_reversed})

url = "http://challenge.code2040.org/api/validatestring"

value = requests.post(url, data = json_answer)

#print result
print value.text

#II. needle in a haystack

url = "http://challenge.code2040.org/api/haystack"

value = requests.post(url, data = json_token)
my_dict = value.json()
my_dict_value = my_dict.values()[0]
my_needle = my_dict_value['needle']
my_array = my_dict_value['haystack']

#initilize counter for position
j = 0
#for loop to find position of needle in haystack
for j in range(0, len(my_array)):
    if(my_array[j] == my_needle):
        break
    j+=1

#return answer
json_answer = json.dumps({"token": my_token, "needle": j})

url = "http://challenge.code2040.org/api/validateneedle"
value = requests.post(url, data = json_answer)

#print result
print value.text

#III. Prefix problem
url = "http://challenge.code2040.org/api/prefix"
value = requests.post(url, data = json_token)
my_dict = value.json()
my_dict_value = my_dict.values()[0]
my_string = my_dict_value['prefix']
my_array = my_dict_value['array']
my_array_answer =[]

for entry in my_array:
    #append entry that doesnot start with my_string to my_array_answer
    if not entry.startswith(my_string):
        my_array_answer.append(entry)

url = "http://challenge.code2040.org/api/validateprefix"
json_answer = json.dumps({"token": my_token, "array": my_array_answer})
value = requests.post(url, data = json_answer)

#print result
print value.text

#IV. The dating game

url = "http://challenge.code2040.org/api/time"
value = requests.post(url, data = json_token)

my_dict = value.json()
my_dict_value = my_dict.values()[0]
my_isodate = my_dict_value["datestamp"]
my_interval = my_dict_value["interval"]

#convert date to python format
my_pdate = parser.parse(my_isodate)

#add date to interval in seconds
my_pdate += timedelta(seconds = my_interval)

#convert date to iso format
my_newdate = my_pdate.isoformat()


json_answer = json.dumps({"token": my_token, "datestamp": my_newdate})
url = "http://challenge.code2040.org/api/validatetime"
value = requests.post(url, data = json_answer)

#print result
print value.text

