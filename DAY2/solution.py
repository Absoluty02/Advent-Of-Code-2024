#!/usr/bin/env python3

def is_safe(input) -> bool:
    ascending = True if input[0] < input[1] else False 
    descending = True if input[0] > input[1] else False
    for i in range(len(input)-1):
        difference = input[i] - input[i+1]
        if (abs(difference) < 1 or abs(difference) > 3):
            return False
        elif (int(input[i]) < int(input[i+1]) and ascending == False and descending == True):
            return False
        elif (int(input[i]) > int(input[i+1]) and descending == False and ascending == True):
            return False
    return True
    

def main():

    print("ciao")
    safe_count: int = 0
    with open("input.txt", "r") as file:
        for riga in file:
            levels = [int(num) for num in riga.split(" ")]
            print(levels)
            if is_safe(levels):
               safe_count += 1
            else:
                dampened = False
                for i in range(0,len(levels)):
                    if is_safe(levels[:i]+levels[i+1:]):
                        dampened = True
                if dampened:
                    safe_count += 1
    
    print(safe_count)

if __name__ == "__main__":
    main()