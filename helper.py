import time

#helper functions

#print one letter at the time
def tprint(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

#print ascii art from file
def aprint(fname):
    file = open(fname,"r")

    print("".join([line for line in file]))