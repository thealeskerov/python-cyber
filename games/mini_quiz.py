# Simple 3-question quiz

score = 0

q1 = input("What is the capital of France? ")
if q1.lower() == "paris":
    score += 1

q2 = input("What is 5 * 3? ")
if q2 == "15":
    score += 1

q3 = input("What programming language are we using? ")
if q3.lower() == "python":
    score += 1

print("You got", score, "out of 3 correct.")
