#! /bin/python3
import pyautogui
from os import system as cmd

# CONFIG: Replace the axis with coordinates you want to type the files.
# Note: To find the coords, run the file named 'find_coords.py'. This will dump the coords on the mouse. Make sure to type a valid integer number, nor a float or string, etc. To see more, read README.md.

x_axis=444
y_axis=694

# END CONFIG

print()
print("Files:\n----------")
cmd("ls")
print()
filename = input("File to dump > ")

file = open(str(filename), "r")
file2 = open(str(filename), "r")

total = 0
for line in file2:
    total = total+1
del file2

count = 0

pyautogui.moveTo(x_axis, y_axis, 0.5)
pyautogui.click()
for i in file:
    i = i.rstrip()
    if len(i) > 0:
        i = i.split()
        for j in i:
            pyautogui.write(str(j))
            pyautogui.press('enter')

            cmd("clear")
            count = count+1
            print("Total:          " + str(total)+" lines")
            print("Current line:   " + str(count))
            print("Current status: " + str(int((count/total)*100))+"%"+" done")

cmd("clear")
count = count+1
print("Total:          " + str(total)+" lines")
print("Current line:   " + str(count))
print("Current status: " + "100% - DONE")