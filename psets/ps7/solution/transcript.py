class Course():
    def __init__(self, name, percent, year):
        self.name = name
        self.percent = percent
        self.year = year

    def __str__(self):
        num_spaces = 16
        leftover_spaces = num_spaces - len(self.name)
        return self.name + (' '*leftover_spaces) + self.letter_grade()

    def letter_grade(self):
        ranges = {'A+': 97, 'A': 94, 'A-': 90,
                  'B+': 87, 'B': 84, 'B-': 80,
                  'C+': 77, 'C': 74, 'C-': 70,
                  'D+': 67, 'D': 64, 'D-': 60,
                  'F': 0}
        for g, p in ranges.items():
            if self.percent >= p:
                return g

    def grade_point(self):
        unweighted_conversion = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0, 'D-': 0.7,
            'F': 0.0}
        grade = self.letter_grade()
        return unweighted_conversion[grade]


class Honors(Course):
    def grade_point(self):
        return 0.5 + super().grade_point()


class AP(Course):
    def grade_point(self):
        return 1.0 + super().grade_point()


def total_gpa(transcript):
    total = 0.0
    for course in transcript:
        total += course.grade_point()
    return round(total / len(transcript), 2)


def partial_transcript(transcript, years, types):
    for year in years:
        print('Year '+str(year)+':')
        for typ in types:
            print(f'    {str(typ.__name__)}:')
            for course in transcript:
                if course.year == year and isinstance(course, typ):
                    print(f'        {course}')
        print()


if __name__ == '__main__':
    transcript = [Honors('Biology', 88, 9), Course('Algebra', 91, 9), Honors('English', 76, 9),
                  Course('Spanish 1', 95, 9), Honors('Chemistry', 68, 10), Course('Trigonometry', 89, 10),
                  Course('Geography', 73, 10), Course('Spanish 2', 93, 10), Course('History', 90, 11),
                  AP('Calculus', 85, 11), AP('Language', 99, 11), Honors('Spanish 3', 92, 11),
                  AP('Physics', 72, 12), AP('Statistics', 86, 12), AP('Literature', 91, 12),
                  Honors('Spanish 4', 94, 12)]

    partial_transcript(transcript, [11, 12], [Honors, AP])

    print("My GPA is", total_gpa(transcript))
