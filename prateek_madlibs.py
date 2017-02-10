import sys
#below are the main questions and following each of them is their answers .
ques1="www stands for __1__. it is the basic protocol on which __2__ works.Without it you can't access any __3__ and __4__ online "
ans1=["world wide web","internet","websites","webpages"]
ques2="English is mainly categorised into two standards __1__ and __2__ . the only thing both differs is different __3__ with same meaning and a little bit of __4__."
ans2=["british","american","words","grammar"]
ques3="__1__ discovered america in the __2__ century . however he wasn't the first one to reach their as __3__ found it first in the __4__ century"
ans3=["christopher columbus","15th","vikings","11th"]
# behaviour-The age module allows the user to enter their name , choose age and asks for difficulty level according
# to their age group.
"""
input-it takes no inputs.
outputs-this function returns no values.
"""
def age():
    easy="level 1"
    medium="level 2"
    hard="level 3"
    #3 levels that are level 1,level 2,level 3.
    name=raw_input("Please enter your name:")
    #this variable asks the user to enter their name
    print "\nhi "+ name +"! "
    age=int(raw_input("Enter your age:"))
    #the age variable asks the user to enter their age so that it can process the levels using age and the game can move further.
    if age>=10  and age<=15:
        level(ques1,ans1,easy,medium,hard)
        #calling the level function to move the game further and passing some initial values of easy level.
    if age > 15 and age<=25:
        level(ques2,ans2,medium,easy,hard)
        #calling the level function and passing the values for medium level i.e- level 2.
    elif age>25:
        level(ques3,ans3,hard,easy,medium)
        #if age is greater than 25 than the hard level is set.
    elif age<10:
        print "This ain't a kids game!"
        sys.exit(0)
"""
the level function takes ques,answer and three level from the age function but returns nothing.
its behaviour is that it helps the user to choose either the preselected level or other level of questions.
"""
def level(ques,ans,level,level2,level3):
    print "your difficulty level is" + level + "do you accept it . type either yes or no"
    response=raw_input("type your response here:")
    #the response variable  takes a response from the user and process further.
    if response.lower()=="yes":
        print "thanks for choosing this level . here is your question \n you will only get 3 chances "
        game(ques,ans)
    elif response.lower()=="no":
        #if user chooses yes then the preselected ques will be asked. if no then he will be allowed to choose.
        print "choose level from" +level+ "or"+level2+"or"+level3+": \n"
        resp=raw_input()
        if resp=="level 1":
            game(ques1,ans1)
        elif resp=="level 2":
            game(ques2,ans2)
        elif resp=="level 3":
            game(ques3,ans3)
        #resp variable takes input from user and the ques of desired level is asked

#takes question and answer as input.If supplied answer and user input matches ,it goes for next blank .
def game(ques,ans):
    print ques
    chances = 3
    # length of answer list is stored in ans variable
    answ = len(ans)
    # counter variable to reach total number of blanks
    count = 0
    counter = 1
    while count < answ:
        print "enter the " + str(counter) + " Answer\n"
        u_answer = raw_input().lower()
        if u_answer == ans[count]:
          eg_string = "__" + str(counter) + "__"
          ques = ques.replace(eg_string, u_answer)
          print "\n", ques
          count = count+1
          counter = counter + 1
        else:
            chances = red_chance(chances)
    print "\nCongratulations you win!!"



# takes chance as input, reduce it by 1 and return the value back and if there no more chances it exits the game.
def red_chance(chances):
    chances=chances-1
    min_chance=0
    #min_chance stores the min number of chances given
    if chances==min_chance:
        print "\n you lose the game ."
        sys.exit(0)
    else:
        print "you have",chances,"left.enjoy!!"
        return chances


age()
