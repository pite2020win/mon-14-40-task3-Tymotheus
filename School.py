from dataclasses import dataclass
from typing import List
from statistics import mean
import logging
import json


@dataclass
class Student:
    name: str
    grades: List[float]
    class_name: str = None
    school_name: str = None

    def get_average(self) -> float:
        return round(mean(self.grades), 2)

    def get_short_info(self) -> str:
        return "{}, grades: {}".format(self.name, self.grades)

    def get_full_info(self) -> str:
        return "{}, class: {}, school: {}".format(self.get_short_info(), self.class_name, self.school_name)

    def __str__(self):
        return self.name


@dataclass
class Class:
    name: str
    students: List[Student]
    school_name: str = None

    def __post_init__(self):
        for s in self.students:
            s.class_name = self.name

    def class_average(self) -> float:
        if len(self.students) == 0:
            logging.info("No students in a class")
        else:
            return round(mean(map(lambda stud: stud.get_average(), self.students)), 2)

    def print_students(self):
        logging.info("Class {}".format(self.name))
        for i in range(len(self.students)):
            logging.info("{}. {}".format(i + 1, self.students[i].get_short_info()))


@dataclass
class School:
    name: str
    classes: List[Class]

    def __post_init__(self):
        for c in self.classes:
            c.school_name = self.name
            for s in c.students:
                s.school_name = self.name

    def total_average(self) -> float:
        return round(mean([student.get_average() for c in self.classes for student in c.students]), 2)

    def get_student_average(self, class_name: str, students_name: str) -> float:
        try:
            checked_class = self.classes[[c.name for c in self.classes].index(class_name)]
            checked_student = checked_class.students[[s.name for s in checked_class.students].index(students_name)]
            return round(checked_student.get_average(), 2)
        except ValueError:
            logging.info("No such student or class in the school.")
            return None

    def print_all_students(self):
        logging.info("School {}".format(self.name))
        for c in self.classes:
            c.print_students()

    def save_school_to_json(self):
        with open("{}_info.json".format(self.name), "w") as file:
            json_dict = {c.name: {s.name: s.grades for s in c.students} for c in self.classes}
            file.write(json.dumps(json_dict, indent=4))
