class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.q_list = q_list

    def still_has_question(self):
        return self.q_no < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.q_no]
        self.q_no += 1
        user_answer = input(f"Q.{self.q_no} {current_q.text} (True/False): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1;
            print('You got it right')
        else:
            print('Thats wrong')
        print(f"The correct answer was: {correct_answer}.")
        print(f"You  current score is: {self.score} / {self.q_no}")
        print("\n")