#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from pprint import pprint
from collections import defaultdict


def read_file(input_file):
    with open(input_file, "r") as f:
        return f.read()


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        sys.exit(1)

    data = read_file(input_file).strip().split("\n")

    students, exam_count, exam_position = parse_studens(data)
    params = parse_header(data[0])

    for key, item in students.items():
        print(item, "x", key)

    print("\nFrequencies")
    for exam, frequency in sorted(list(exam_count.items()), key=lambda x: x[1]):
        print("{:>3}: {:>3}".format(exam, frequency))

    print("\nPositions:")
    for exam, positions in sorted(list(exam_position.items()), key=lambda x: x[0]):
        print("{:>3}: {}".format(exam, positions))

    print("\nExams:", params["exams_tot"])
    print("Students:", params["students"])
    print("Days:", params["days"])
    print("Students:", params["students"])
    print("Total slots:", int(params["slots"]) * int(params["days"]))


def parse_header(header):
    items = header.split(" ")

    params = {}
    params["days"] = items[0]
    params["slots"] = items[1]
    params["exams_tot"] = items[2]
    params["exams_max"] = items[3]
    params["students"] = items[4]
    params["penalty"] = items[5]

    return params


def parse_studens(data):
    THRESHOLD = 0

    student_sets = defaultdict(int)
    exam_count = defaultdict(int)
    exam_position = defaultdict(lambda: [0, 0, 0])

    exam_list = [item.split(" ")[1:] for item in data[1:-1]]
    exam_list.sort(key=len, reverse=True)

    for i, exams in enumerate(exam_list):
        a = set(exams)

        for i, exam in enumerate(exams):
            exam_count[exam] += 1
            if i == 0:
                exam_position[exam][0] += 1
            elif i == len(exams) - 1:
                exam_position[exam][2] += 1
            else:
                exam_position[exam][1] += 1

        found = False
        for key, value in student_sets.items():
            b = set(key.split(" "))
            if (len(a) - len(a.intersection(b))) <= THRESHOLD:
                student_sets[key] += 1
                found = True
                break

        if not found:
            student_sets[" ".join(exams)] += 1

    return student_sets, exam_count, exam_position


if __name__ == "__main__":
    main()
