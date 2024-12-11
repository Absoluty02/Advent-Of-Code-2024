import re


def find_and_calculate(input):

    result = 0
    regex = r'mul\((\d+)\,(\d+)\)'
    r = re.compile(regex)

    for element in re.findall(r, input):
        result += (int(element[0])*int(element[1]))
    
    return result

def find_allowed_parts(input):
    regex1 = r'(.*?)do'
    regex2 = r"do\(\)(.*?)don't"

    
    substrings = re.findall(regex2, input)
    substrings.append(re.match(regex1, input).group(1))

    result = 0
    for element in substrings:
        result += find_and_calculate(element)
    return result


def main():
    memory = ""
    with open("input.txt", "r") as file:
        for riga in file:
            memory += riga.strip()
                
    print(find_allowed_parts(memory))

if __name__ == '__main__':
    main()