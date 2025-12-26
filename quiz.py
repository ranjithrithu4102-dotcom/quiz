qustions=[
    {
    "question":"what is the capital of france?",
    "options":["a.paris","b.london","c.berlin","d.rome"],
    "answer":"a"

    },
  {
        "question": "Which language is used for web apps?",
        "options": ["a. Python", "b. JavaScript", "c. C++", "d. Java"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["a. 10", "b. 11", "c. 12", "d. 13"],
        "answer": "C"
    }
]


# -------- Functions -------- #
def take_quiz():
    score=0


    for i ,q in enumerate(qustions,start=1):
        print(f"{i} :{q['question']}")
        for option in q['options']:
            print(option)
        answer=input("enter answer(a/b/c/d): ")    

        if answer==q['answer']:
            print("correct !")
            score+=1
        else :
            print(f"wrong answer , correct answer is {q['answer']}")    

    print(f"your score is {score}/{len(qustions)}")        



def add_question():
    question_text=input("enetr your question:")
    options=[]
    for option in ["a","b","c","d"]:
        opt_txt=input(f"option {option}: ")
        options.append(f"{option}.{opt_txt}")
    answer=input("correct answer(a/b/c/d): ")  

    qustions.append({
        "question":question_text,
        "options":options,
        "answer":answer
    })  


    print("qustion added successfully !")   


# -------- Menu -------- #
while True:
        print("=== Quiz System ===")
        print("1. Take Quiz")
        print("2. Add Question")
        print("3. Exit")  

        choice=input("enter an option: ")  


        if choice=="1":
             take_quiz()
        elif choice=="2":
             add_question()
        elif choice=="3":
            print("thank you !")
            break 
        else:
             print("invaild choice")         