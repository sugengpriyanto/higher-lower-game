from replit import clear
import random
from game_data import data

#Generate a random account from the game
def get_question():
  return random.choice(data)

#Format the account data to printable
def format_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description} from {country}"

#check if the answer is correct
def check(answer, followers_a, followers_b):
  if followers_a > followers_b:
    return answer == 'a'
  elif followers_b > followers_a:
    return answer == "b"

def play():
  score = 0
  game_flow = True
  question_a = get_question()
  question_b = get_question()

  while game_flow:
    question_a = question_b
    question_b = get_question()

    while question_a == question_b:
      question_b = get_question()

    print(f"Compare A: {format_data(question_a)}")
    print("vs")
    print(f"Against B: {format_data(question_b)}")
    #ask user for a guess
    answer = input("Who has more followers? Type 'a' or 'b': ")
    fol_a = question_a['follower_count']
    fol_b = question_b['follower_count']
    is_correct = check(answer, fol_a, fol_b)

    clear()
    if is_correct:
      score + 1
      print(f"You right. Your score is {score}")
    else:
      game_flow = False
      print(f"You wrong. Your final score is {score}")
play()
##get follower count


##compare

#Give user feedback
#score keeping


#make game repeatable
#making account position in B to A

#clear screen between round 





