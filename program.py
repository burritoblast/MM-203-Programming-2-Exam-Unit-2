from ansi import *
from httpUtils import *
import json


print(ANSICodes.Clear)
print("Starting Assignment 2")


myPersonalID = "d1e766a2df6cd2f4a718697b456455f51d987f03d14c1d7f957e4a3820fc941a"
baseURL = "https://mm-203-module-2-server.onrender.com/"
startEndpoint = "start/"
taskEndpoint = "task/"


startResponse = HttpUtils.Get(baseURL + startEndpoint + myPersonalID)
print(f"Start:\n{ANSICodes.Colors.Magenta}{startResponse.content}{ANSICodes.Reset}\n\n")
taskID = json.loads(startResponse.content).get('taskID')


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)

def roman_to_int(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            int_value -= value
        else:
            int_value += value
        prev_value = value
    return int_value


while taskID:
    taskResponse = HttpUtils.Get(baseURL + taskEndpoint + myPersonalID + "/" + taskID)
    taskDetails = json.loads(taskResponse.content)
    print(taskDetails)

    if taskDetails['title'] == 'Temprature converter':
        fahrenheit = float(taskDetails["parameters"])
        celsius_temp = fahrenheit_to_celsius(fahrenheit)
        result = f"{celsius_temp:.2f}"
        print(f"{fahrenheit}°F is {result}°C")


    elif taskDetails['title'] == 'Roman':
        roman_numeral = taskDetails["parameters"]
        integer_value = roman_to_int(roman_numeral)
        result = integer_value
        print(f"{roman_numeral} is {integer_value}")
        
    elif taskDetails['title'] == 'Unique words':
        words_string = taskDetails["parameters"]
        unique_words_list = sorted(set(words_string.split(',')))
        result = ','.join(unique_words_list)
        print(f"Unique words: {result}")

    elif taskDetails['title'] == 'Task Sum':
        numbers_list = [int(num) for num in taskDetails["parameters"].split(',')]
        total_sum = sum(numbers_list)
        result = total_sum
        print(f"Sum of numbers: {result}")

    else:
        print("Unknown task type.")
        break


    answerResponse = HttpUtils.Post(baseURL + taskEndpoint + myPersonalID + "/" + taskID, result)
    print(f"Answer Response: {answerResponse.content}")


    taskID = answerResponse.content.get('taskID')
    if not taskID:
        print("\nAll tasks completed.")
        break