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

    students = parse_studens(data)
    params = parse_header(data[0])

    for key, item in students.items():
        print(item, "x", key)

    print("Exams:", params["exams_tot"])
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
    THRESHOLD = 7

    students = defaultdict(int)

    exam_list = [item.split(" ")[1:] for item in data[1:-1]]
    exam_list.sort(key=len, reverse=True)

    for i, exams in enumerate(exam_list):
        a = set(exams)

        found = False
        for key, value in students.items():
            b = set(key.split(" "))
            if (len(a) - len(a.intersection(b))) <= THRESHOLD:
                students[key] += 1
                found = True
                break

        if not found:
            students[" ".join(exams)] += 1

    return students


if __name__ == "__main__":
    main()
