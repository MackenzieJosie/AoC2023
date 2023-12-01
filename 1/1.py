def part1():
    input = open("input.txt", "r").read().split("\n")

    sum = 0

    for line in input:
        line = line.strip("abcdefghijklmnopqrstuvwxyz")
        current = int(line[0]) * 10 + int(line[len(line)-1])
        sum += current

    return sum

# def translate()

def part2():
    input = open("input.txt", "r").read()
    input = input.replace("one", "o1e")
    input = input.replace("two", "t2o")
    input = input.replace("three", "t3e")
    input = input.replace("four", "f4r")
    input = input.replace("five", "f5e")
    input = input.replace("six", "s6x")
    input = input.replace("seven", "s7n")
    input = input.replace("eight", "e8t")
    input = input.replace("nine", "n9e")
    input = input.split("\n")


    sum = 0

    for line in input:
        line = line.strip("abcdefghijklmnopqrstuvwxyz")
        current = int(line[0]) * 10 + int(line[len(line)-1])
        # print(line, current)
        sum += current

    return sum

print(part1())
print(part2())