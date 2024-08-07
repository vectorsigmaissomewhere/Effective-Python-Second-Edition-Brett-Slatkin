===========================Program Number one ==================================
```text
storing the data in dictionary instead of predefined attributes for each student
this program stores student name and with related to name it stoes the value in list
```
 
```python
class SimpleGradebook:
    def __init__(self):
        self._grades = {}
    
    # adding the name key and in value it is an empty list 
    def add_student(self, name):
        self._grades[name] = []
    
    # addding value in empty list related to the dictionary key
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    # getting all the list data in grades and finding the average 
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Issac Newton')
book.report_grade('Issac Newton',90)
book.report_grade('Issac Newton',95)
book.report_grade('Issac Newton', 85)
print(book.average_grade('Issac Newton'))
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein',90)
print(book.average_grade('Albert Einstein'))
print(book._grades) # {'Issac Newton': [90, 95, 85], 'Albert Einstein': [90]}
```


==========================Program Number Two =================================
```text
Extending dictionary to map not only marks but also map subject 
inner dictionary, map subjects to a list of grades 
using defaultdict instance for the inner dictionary to handle missing subjects
```

```python
from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):  # outer dict 
        self._grades = {}
    
    def add_student(self, name): # inner dict 
        self._grades[name] = defaultdict(list)
    
    # first map the name, map subject , add grade in that subject
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name] # this gives the inner dict related to that name means subject dictionary i.e instance
        grade_list = by_subject[subject] # input subject and this will give all the grades related to the subject i.e instance
        grade_list.append(grade) # this adds the grades in that inner dictionary 

    # this function returns the average_grade
    def average_grade(self, name):
        by_subject = self._grades[name] # get all the subjects of the related name, inner dictionary instance
        total, count = 0, 0 
        for grades in by_subject.values(): # get all the grades value 
            total += sum(grades) # find the sum 
            count += len(grades) # get the total lenght of the list
        return total / count 
    

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein')) # 81.25
```
```text
Program number one and program number 2 is the almost same # we just created one inner dictionary 
````

=========================Program three================================
```text
what to do where there is one more value that relates to the value means subject
using tuple of (score, weight) in the values list
this program takes weight which is like measure the student performance in each term in weight
```

```python
from collections import defaultdict

class WeightedGradebook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject] # this will created an inner dictionary instance of the subject
        grade_list.append((score, weight)) # this will append the subject score with its weight , storing the score and weight in tuple instance

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
        
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count
    
book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 70, 0.05)
book.report_grade('Albert Einstein', 'Math', 65, 0.15)
book.report_grade('Albert Einstein', 'Math', 70, 0.80)
book.report_grade('Albert Einstein', 'Gym', 100, 0.40)
book.report_grade('Albert Einstein', 'Gym', 85, 0.60)
print(book.average_grade('Albert Einstein')) #80.125
```

===================================Program Four=====================================

more inner dictionary creates more complexity so using classes and interfaces to decrease the complexity 
```python

from collections import defaultdict


class Subject:
    def __init__(self):
        self._grades = []
    
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
    
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight
    
class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)
    
    def get_student(self, name):
        return self._subjects[name]
    
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
    
    def get_student(self, name):
        return self._students[name]

book = Gradebook()
albert = book.get_student('Albert Einstein')
math = albert.get_subject('Math')
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade()) # 80.25
```

```text
use namedtuple for lightweight, immutable data containers 
create multiple classes when your internal state dictionaries get complicated
```
