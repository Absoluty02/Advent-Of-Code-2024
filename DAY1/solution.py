import sys
import re

regex = "^(\d+)\s+(\d+)$"
r = re.compile(regex)

def calculate_distance(first_list, second_list) -> int:
    
    distance: int = 0

    for i in range(len(first_list)):
        if first_list[i] > second_list[i]:
            distance += (first_list[i] - second_list[i])
        elif first_list[i] < second_list[i]:
            distance += (second_list[i]- first_list[i])   
        else:
            continue

    return distance


def main():
    first = []
    second = []
    with open("input.txt", "r") as file:
        for riga in file:
            search = re.search(r, riga)
            first.append(int(search.group(1)))
            second.append(int(search.group(2)))
            #print(f"primo gruppo: {int(search.group(1))}")
            #print(f"secondo gruppo: {int(search.group(2))}")

    print(calculate_distance(sorted(first), sorted(second)))
    

if __name__ == "__main__":
    main()
