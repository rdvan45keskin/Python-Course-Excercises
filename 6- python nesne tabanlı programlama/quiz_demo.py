# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer

# Quiz
class Quiz:
    # Sorular listesi, başlangıç puanı (score), ve şu an hangi soruda olunduğunu belirten questionIndex atanır.
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    # getQuestion(self): O anki soruyu (index'e göre) döner.
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    # displayQuestion(self): Mevcut soruyu ve şıkları ekrana yazdırır, kullanıcıdan cevap alır, ve bu cevabı kontrol eder (guess metodunu çağırır). Daha sonra bir sonraki soruya geçer (loadQuestion).
    def displayQuestion(self,):
        questionX = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {questionX.text}")
        for q in questionX.choices:
            print("-" + q)
        answer = input("cevap : ")
        self.guess(answer)
        self.loadQuestion()

    # guess(self, answer): Kullanıcının verdiği cevabı kontrol eder (checkAnswer ile). Cevap doğruysa puan (score) artırılır. Daha sonra questionIndex artırılarak bir sonraki soruya geçilir.
    def guess(self,answer):
        questionX = self.getQuestion()

        if questionX.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    # loadQuestion(self): Eğer sınav bitti (tüm sorular soruldu), showScore ile puanı gösterir. Eğer sınav bitmediyse, bir sonraki soruyu gösterir (displayQuestion metodunu çağırır).
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    # showScore(self): Kullanıcının toplam puanını ekrana yazdırır.
    def showScore(self):
        print("score :",self.score)

    # displayProgress(self): Sınavın ne kadarının tamamlandığını ekrana yazdırır (örneğin "Soru 2 of 3" gibi).
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("quiz bitti")
        else:
            print(f" Question {questionNumber} of {totalQuestion} ".center(100,"*"))



q1 = Question("en iyi programlama dili hangisidir?",["c#","python","javascript","java"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","javascript","c#","java"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["c#","javascript","java","python"],"python")
sorular = [q1,q2,q3]
# print(q1.checkAnswer("python"))
# print(q2.checkAnswer("c#"))

# quiz = Quiz(sorular)
# question = quiz.questions[quiz.questionIndex]    #question değerini quiz.questions yani sorular dizisindeki tüm değerlere atar
#                                                  #ve quiz.questionIndex ile quiz classında belirtilen değeri seçer
#                                                  #bu kodda question değeri sorular dizisindeki ilk elemanı seçer çümkü quiz.questionIndex=0 dır                                                 
# bu
# question = Quiz(sorular).getQuestion()
#yada
quiz = Quiz(sorular)
quiz.loadQuestion()

# Quiz Nesnesi ve İşleyiş:

# sorular: Question nesnelerinden oluşan bir liste.
# quiz = Quiz(sorular): Quiz sınıfından bir nesne oluşturulur ve bu sınav soruları Quiz nesnesine atanır.
# quiz.loadQuestion(): Sınav başlatılır ve sorular teker teker kullanıcıya sorulmaya başlanır.
# Kodun İşleyişi:

# quiz.loadQuestion() ile sınav başlar.
# İlk soru ekrana yazdırılır (displayQuestion çağrılır).
# Kullanıcı bir cevap girer.
# Cevap doğruysa puan artırılır, yanlışsa puan artırılmaz (guess ile).
# Bir sonraki soruya geçilir (loadQuestion ile).
# Tüm sorular sorulup sınav bitince showScore ile kullanıcıya puanı gösterilir.
# Bu basit quiz uygulaması, kullanıcıya sırayla sorular sorar ve doğru cevaplarına göre puanlar verir. Sınav sonunda toplam puan ekrana yazdırılır.
