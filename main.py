import time
def main(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    print('')

string = "you just lost the game."
main(string)
