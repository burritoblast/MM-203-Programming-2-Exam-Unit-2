
from ansi import *
from httpUtils import *

print(ANSICodes.Clear)
print("Starting Assignment 2")

# SETUP 
myPersonalID = "" # GET YOUR PERSONAL ID FROM THE ASSIGNMENT PAGE https://mm-203-module-2-server.onrender.com/
baseURL = "https://mm-203-module-2-server.onrender.com/"
startEndpoint = "start/" # baseURl + startEndpoint + myPersonalID
taskEndpoint = "task/"   # baseURl + taskEndpoint + myPersonalID + "/" + taskID

##### REGISTRATION
# We start by registering and getting the first task
startRespons = HttpUtils.Get(baseURL + startEndpoint + myPersonalID)
print(f"Start:\n{ANSICodes.Colors.Magenta}{startRespons.content}{ANSICodes.Reset}\n\n") # Print the response from the server to the console
taskID = "" # We get the taskID from the previous response and use it to get the task (look at the console output to find the taskID)

##### FIRST TASK 
# Fetch the details of the task from the server.
task1Response = HttpUtils.Get(baseURL + taskEndpoint + myPersonalID + "/" + taskID) # Get the task from the server
print(task1Response)
