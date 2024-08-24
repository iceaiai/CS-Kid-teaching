class auto_grader_01:
    def __init__(self):
        self.total_grade = 0
        self.auto_grader_01 = 0
        self.auto_grader_02 = 0
        self.auto_grader_03 = 0
        self.auto_grader_04 = 0
        self.auto_grader_05 = 0
        self.auto_grader_06 = 0
        self.auto_grader_07 = 0
        self.auto_grader_08 = 0
        self.auto_grader_09 = 0
        self.auto_grader_10_a = 0
        self.auto_grader_10_b = 0
        self.auto_grader_10_c = 0
        self.answer_1 = 6 * 6 / (6 / 6)
        self.answer_2 = 3 * 2 ** 2
        self.answer_3 = 104 // 10
        self.answer_4 = 11 * 2 // 7
        self.answer_5 = 11 - 2 // 7
        self.answer_6 = 11 - 2 % 7
        self.answer_7 = 10 - 5
        self.answer_8 = 10 + 1*8
        self.name = ''
        a = 18
        a = a - 14
        a = a - 2
        a = a * 15
        a = a / 6 
        self.answer_9 = a
        self.a = 5
        self.b = 4
        self.c = 24
    def check(self, your_name):
        if your_name == '':
            print('Please type your name')
        else:
            self.name = your_name
            print(your_name)
    def Q1(self, a1):
        if a1 == self.answer_1:
            print('You obtained 10 points in question 1')
            self.auto_grader_01 = 10
        else:
            print('Wrong answer for question 1, try again!')
            self.auto_grader_01 = 0
    def Q2(self, a2):
        if a2 == self.answer_2:
            print('You obtained 10 points in question 2')
            self.auto_grader_02 = 10
        else:
            print('Wrong answer for question 2, try again!')
            self.auto_grader_02 = 0
    def Q3(self, a3):
        if a3 == self.answer_3:
            print('You obtained 10 points in question 3')
            self.auto_grader_03 = 10
        else:
            print('Wrong answer for question 3, try again!')
            self.auto_grader_03 = 0
    def Q4(self, a4):
        if a4 == self.answer_4:
            print('You obtained 10 points in question 4')
            self.auto_grader_04 = 10
        else:
            print('Wrong answer for question 4, try again!')
            self.auto_grader_04 = 0
    def Q5(self, a5):
        if a5 == self.answer_5:
            print('You obtained 10 points in question 5')
            self.auto_grader_05 = 10
        else:
            print('Wrong answer for question 5, try again!')
            self.auto_grader_05 = 0
    def Q6(self, a6):
        if a6 == self.answer_6:
            print('You obtained 10 points in question 6')
            self.auto_grader_06 = 10
        else:
            print('Wrong answer for question 6, try again!')
            self.auto_grader_06 = 0
    def Q7(self, a7):
        if a7 == self.answer_7:
            print('You obtained 5 points in question 7')
            self.auto_grader_07 = 5
        else:
            print('Wrong answer for question 7, try again!')
            self.auto_grader_07 = 0
    def Q8(self, a):
        if a == self.answer_8:
            print('You obtained 5 points in question 8')
            self.auto_grader_08 = 5
        else:
            print('Wrong answer for question 8, try again!')
            self.auto_grader_08 = 0
    def Q9(self, a):
        if a == self.answer_9:
            print('You obtained 10 points in question 9')
            self.auto_grader_09 = 10
        else:
            print('Wrong answer for question 9, try again!')
            self.auto_grader_09 = 0
    def Q10(self, a,b,c):
        if a == self.a:
            print('You obtained 5 points in question 10 because a is right')
            self.auto_grader_10_a = 5
        else:
            print('Wrong answer for a, try again!')
            self.auto_grader_10_a = 0
        if b == self.b:
            print('You obtained 5 points in question 10 because b is right')
            self.auto_grader_10_b = 5
        else:
            print('Wrong answer for b, try again!')
            self.auto_grader_10_b = 0
        if c == self.c:
            print('You obtained 10 points in question 10 because c is right')
            self.auto_grader_10_c = 10
        else:
            print('Wrong answer for c, try again!')
            self.auto_grader_10_c = 0
    def total_score(self):
        self.total_grade = sum([self.auto_grader_01, self.auto_grader_02, self.auto_grader_03, 
                                self.auto_grader_04, self.auto_grader_05, self.auto_grader_06, 
                                self.auto_grader_07, self.auto_grader_08, self.auto_grader_09, 
                                self.auto_grader_10_a,self.auto_grader_10_b,self.auto_grader_10_c])
        print(self.your_name, f' total grade is: {self.total_grade}')
