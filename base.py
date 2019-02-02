from pprint import pprint
from math import floor

def get_line_ass_array(line):
    result = line.split(' ')
    # print(line)

    return list(map(int, result))

data = []
with(open('data_sets/Connector.txt', 'r')) as f:
    for line in f:
        data.append(line)



params = data[0].split(' ')
params = list(map(int, params))
header = {
    'days' : params[0],
    'timeslots' : params[1],
    'exams' : params[2],
    'max_exams' : params[3],
    'students' : params[4],
    'penalty' : params[5],
}

students = {}
student_id = 0
for i in range(1, header['students'] + 1):
    students.update({student_id: get_line_ass_array(data[i])[1:]})
    student_id += 1

rewards = {}
reward_index = 0
for r in get_line_ass_array(data[len(data) - 1]):
    rewards.update({reward_index: r})
    reward_index += 1
print(header)
print(rewards)
print(students)

exams = {}
for student, student_exams in students.items():
    for exam in student_exams:
        if exam not in exams.keys():
            exams.update({exam: []})
        exams[exam].append(student)
print("Exams------------------------------")
pprint(exams)

def get_init_timeslots():
    timeslots = {}
    for i in range(header['days'] * header['timeslots']):
        timeslots.update({i: []})
    print("Timeslots exam student------------------------------")
    pprint(timeslots)
    return timeslots

def get_students_timeslots(timeslots):
    students_timeslots = {}
    for i in range(header['students']):
        students_timeslots.update({i: []})

    for timeslot_id, exams in timeslots.items():
        for exam in exams:
            for exam_id, students in exam.items():
                for student_id in students:
                    students_timeslots[student_id].append(timeslot_id)
    return students_timeslots

timeslots = get_init_timeslots()
student_timeslots = get_students_timeslots(timeslots)

print("Students timeslots-----------------------------")
pprint(student_timeslots)

def calculate_reward(t1, t2):
    return rewards[floor((t2 - t1)/header['timeslots'])] - header['penalty'] * (t2 == t1)

reward = 0

for student_id, timeslots in student_timeslots.items():
    for i in range(len(timeslots) - 1):
        first = timeslots[i]
        second = timeslots[i+1]
        reward += calculate_reward(first, second)
print(reward)

