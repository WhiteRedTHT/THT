class Exam(object):
    def __init__(self,true,false):
    	self.score = []
		for sayi in range(sayi):
		self.score.append(sayi)
    def score(self):
        puanlar = 100/(true + false)*true
        self.score.append(puanlar)


class Student(Exam):
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def student(self):
		return self.student

	def avg_score(self):
    	return sum(self.score) / len(self.score)
   
class Sinif(Student):
    def __init__(self,sinif,ort):
        self.sinif = sinif
        self.ort = ort
    
    def class_avg(self):
    	return sum(self.score) / len(self.score)





