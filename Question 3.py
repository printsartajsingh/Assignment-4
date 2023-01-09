import random
QuestionNo = 10
def main():
    random.seed()
    count = 0
    while count < QuestionNo:
        FirstNumber = random.randint(1, 10)
        SecondNumber = random.randint(1, 10)
        count += 1
        Response = int(input("What is " + str(FirstNumber) + "x" + str(SecondNumber) + "="))
        CorrectAnswer = int(FirstNumber*SecondNumber)
        if Response == CorrectAnswer :
            print("Correct!")
        else :
            print("Your answer is Wrong!!!!!,the answer is",Response, ".")
main()