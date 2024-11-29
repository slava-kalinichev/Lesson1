import csv
import sys


def process_input(input_lines):
    unique_trolls = {}
    results = []
    num = 1
    for i, line in enumerate(input_lines, start=1):
        print(num, line)
        line = line.strip()
        parts = line.split(",")
        who = parts[0]
        where = parts[1]
        following = parts[2]

        if who not in unique_trolls:
            unique_trolls[who] = True
            control_number = len(who) + len(where) + len(following) - 2
            results.append((num, where.strip(), who, following.strip(), control_number))
            num += 1

    return results


def to_csv(results):
    with open('path.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow(['no', 'where', 'who', 'following', 'control'])
        for i in results:
            csvwriter.writerow(i)


input_lines = sys.stdin.readlines()
results = process_input(input_lines)
to_csv(results)
