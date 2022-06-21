from question import Question

question_prompts = [
    "what is the color of apple?\n a: Red/Green\n b: Pruple/Pink\n c: Orange/Blue\n\n",
    "what is the color of banana?\n a: Yellow\n b: Black\n c: White\n\n",
    "what is teh color of strawberry?\n a: Red\n b: Pink\n c: white\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
        else:
            score = 0

    print (" You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)