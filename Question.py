class Question:
    
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def run_test(quests):
        score = 0;

        for q in quests:
            answer = input(q.prompt)
            if answer == q.answer:
                score += 1
        print("Score: " + str(score) + "/" + str(len(quests)))