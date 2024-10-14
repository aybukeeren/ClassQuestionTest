from Question import Question

questionPrompt = [
    "What color are apples?\na)red\nb)blue\nc)purple\n\n",
    "What color are bananas?\na)green\nb)pink\nc)yellow\n\n",
    "What color are strawberries?\na)red\nb)blue\nc)black\n\n",
]

questions = [
    Question(questionPrompt[0], "a"),
    Question(questionPrompt[1], "c"),
    Question(questionPrompt[2], "a"),
]

def runTest (questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=  1
    print("You got", score, "correct answer!!")
    
runTest(questions)