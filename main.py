import time
def main(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    print('')

main("you just lost the game.")
time.sleep(1)
main("nerd")
time.sleep(1)
main("now go program something already, you're boring me.")
time.sleep(10)
main("still here?")
time.sleep(1)
main("man, like please. i'm begging you. go code something already.")
main("I hear the internet loves when you can comment on things.")
