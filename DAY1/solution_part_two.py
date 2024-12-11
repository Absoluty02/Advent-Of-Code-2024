import sys
import re

regex = "^(\d+)\s+(\d+)$"
r = re.compile(regex)

def calculate_similarity(first_list, second_list):

    score: int = 0

    for e1 in first_list:
        count = dict()
        for e2 in second_list:
            if e1 == e2:
                if e1 not in count:
                    count[e1] = 1
                else:
                    count[e1] += 1
        for element in count.keys():
            score += (element * count[element])
            
    return score

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

    print(calculate_similarity(sorted(first), sorted(second)))
    

if __name__ == "__main__":
    main()