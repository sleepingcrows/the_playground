import time
def main(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    print('')

string = "you just lost the game."
main(string)
string = "nerd."
time.sleep(1)
main(string)
time.sleep(1)
main("now go program something already, you're boring me.")
