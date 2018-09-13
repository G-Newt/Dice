from random import randint

def main():
    min = int(input("What is the lowest number on your dice?  "))

    max = int(input("What is the highest number on your dice?  "))

    keepPlaying = "Yes";

    while (keepPlaying == "Yes"):
        print("Your dice rolled a: " + str(randint(min, max)))

        keepPlaying = input("Do you want to play again (type 'Yes' or 'No')?  ")

if __name__ == "__main__":
    main()