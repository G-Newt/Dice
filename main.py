from random import randint

min = input("What is the lowest number on your dice?")

max = input("What is the highest number on your dice?")

keepPlaying = True;

def main():
    while (keepPlaying == True):
        print("Your dice rolled a: " + randint(min, max))

        keepPlaying = input("Do you want to play again (Type 'Yes' or 'No'?")

if __name__ == "__main__":
    main()