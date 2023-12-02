class SingleChoiceQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def ask(self):
        print(self.question)
        valid_answers = []
        for i, answer in enumerate(self.answers):
            answer_letter = chr(i + 97)
            valid_answers.append(answer_letter)
            print(f'{answer_letter}) {answer}')
        while True:
            answer = input('Odpowiedź: ')
            if answer in valid_answers:
                print()
                return answer
            else:
                print('Niepoprawna odpowiedź!')


class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print(self.title)
        print()
        answers = {}
        for i, question in enumerate(self.questions):
            answers[i] = question.ask()
        print('Dziękuję!')
        return answers


questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?',
                          ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])
questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)
answers = questionnaire.run()
print(answers)