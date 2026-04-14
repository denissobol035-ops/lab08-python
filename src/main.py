from typing import List, Iterator, Optional, Type


# =========================
# Descriptor for grade validation
# =========================

class GradeDescriptor:
    def __set_name__(self, owner: Type, name: str) -> None:
        self.name = name

    def __get__(self, instance: Optional["Student"], owner: Type) -> float:
        if instance is None:
            return self  # type: ignore
        return instance.__dict__[self.name]

    def __set__(self, instance: "Student", value: float) -> None:
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        instance.__dict__[self.name] = value


# =========================
# Student class
# =========================

class Student:
    grade = GradeDescriptor()

    def __init__(self, name: str, group: str, grade: float) -> None:
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.name} ({self.group}) - grade: {self.grade}"


# =========================
# Iterator class
# =========================

class StudentIterator:
    def __init__(self, students: List[Student]) -> None:
        self._students = students
        self._index = 0

    def __iter__(self) -> "StudentIterator":
        return self

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        result = self._students[self._index]
        self._index += 1
        return result


# =========================
# Collection with context manager
# =========================

class StudentCollection:
    def __init__(self, students: List[Student]) -> None:
        self._students = students

    def __iter__(self) -> Iterator[Student]:
        return StudentIterator(self._students)

    def __enter__(self) -> "StudentCollection":
        print("Entering context: starting work with collection")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        print("Exiting context: cleaning up resources")


# =========================
# Task A — Iteration
# =========================

print("--- Task A ---")
students: List[Student] = [
    Student("Denis", "CS-124", 90),
    Student("Anna", "CS-124", 85),
    Student("Ivan", "CS-124", 70),
]

collection = StudentCollection(students)

print("Iterating over collection:")
for s in collection:
    print(s)

print("Explanation: collection implements iterator protocol")


# =========================
# Task B — Context Manager
# =========================

print()
print("--- Task B ---")

with StudentCollection(students) as col:
    print("Inside context block")
    for s in col:
        print(s)

print("Explanation: __enter__ and __exit__ control execution")


# =========================
# Task C — Descriptor
# =========================

print()
print("--- Task C ---")

student_test = Student("Test", "CS-124", 50)
print("Valid grade:", student_test.grade)

print("Trying invalid grade:")
try:
    student_test.grade = 150
except ValueError as e:
    print("Error:", e)

print("Explanation: descriptor validates attribute")


# =========================
# Task D — Integration
# =========================

print()
print("--- Task D ---")

with StudentCollection(students) as col:
    for s in col:
        print("Student grade:", s.grade)

print("Explanation: all protocols work together")
