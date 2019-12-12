class Counters:
    """ class of counters for each house that 
    will increment depending on which answer 
    the user picks for each question 
    """
    
    def __init__(self):
        self.gryffindor = 0
        self.hufflepuff = 0
        self.ravenclaw = 0
        self.slytherin = 0

        
def first_question(counters, answer = ''):
    """ printing the first question
        asking about material of wand core
        
        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printing the question
    print("1. The wand chooses you at Ollivander's." \
          " What material is your wand core made of?")
    
    print("\n A) Unicorn Hair" 
          "\n B) Dragon Heartstring" 
          "\n C) Phoenix Feather")
    
    # inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.hufflepuff += 1
        counters.ravenclaw += 1
    elif answer == "B":
        counters.slytherin += 1
        counters.ravenclaw += 1
    elif answer == "C":
        counters.gryffindor += 1
        counters.ravenclaw += 1

        
def second_question(counters, answer = ''):
    """ printing the second question
        asking about favorite class at Hogwarts

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """
    
    # printing the question
    print("\n2. It's leviOsa, not levioSA!" \
              " Your favorite class at Hogwarts is:")
    
    print("\n A) Charms" 
          "\n B) Herbology" 
          "\n C) Transfiguration" 
          "\n D) Potions")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.ravenclaw += 1
    elif answer == "B":
        counters.hufflepuff += 1
    elif answer == "C":
        counters.gryffindor += 1
    elif answer == "D":
        counters.slytherin += 1
        
        
def third_question(counters, answer = ''):
    """ printing the third question
        asking about character traits

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printing the question
    print("\n3. You would hate if someone called you:")
    
    print("\n A) Oblivious" 
          "\n B) Self-Centered"
          "\n C) Insignificant"
          "\n D) Weak")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.ravenclaw += 1
    elif answer == "B":
        counters.hufflepuff += 1
    elif answer == "C":
        counters.gryffindor += 1
    elif answer == "D":
        counters.slytherin += 1


def fourth_question(counters, answer = ''):
    """ printing the fourth question
        asking about making potions

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printing the question
    print("\n4. What potion do you choose to make in Potions class?")
    
    print("\n A) Veritaserum"
          "\n B) Essence of Dittany"
          "\n C) Invisiblity Potion"
          "\n D) Felix Felicis / Liquid Luck")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.slytherin += 1
    elif answer == "B":
        counters.hufflepuff += 1
    elif answer == "C":
        counters.ravenclaw += 1
    elif answer == "D":
        counters.gryffindor += 1

        
def fifth_question(counters, answer = ''):
    """ printing the fifth question
        asking about relationship with friends

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printing the question
    print("\n5. How would you describe your relationship with friends?")
    
    print("\n A) I only have a few close friends that I really trust"
          "\n B) I love making new friends! I love surrounding myself with people"
          "\n C) I find myself making friends who I can gain something from"
          "\n D) I prefer the company of books over people," \
          " but I am still fiercely loyal")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.gryffindor += 1
    elif answer == "B":
        counters.hufflepuff += 1
    elif answer == "C":
        counters.slytherin += 1
    elif answer == "D":
        counters.ravenclaw += 1

        
def sixth_question(counters, answer = ''):
    """ printing the sixth question
        asking about zodiac sign

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """
    
    # printing the question
    print("\n6. What's your zodiac sign?")
    
    print("\n A) Gemini/Sagittarius/Scorpio"
          "\n B) Virgo/Aquarius/Pisces"
          "\n C) Taurus/Libra/Cancer"
          "\n D) Aries/Leo/Capricorn")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.slytherin += 1
    elif answer == "B":
        counters.ravenclaw += 1
    elif answer == "C":
        counters.hufflepuff += 1
    elif answer == "D":
        counters.gryffindor += 1

        
def seventh_question(counters, answer = ''):
    """ printing the seventh question
        asking about patronus

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printing the question
    print("\n7. What's your patronus?")
    
    print("\n A) Hedgehog"
          "\n B) St. Bernard Dog"
          "\n C) Fox"
          "\n D) Dolphin")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.ravenclaw += 1
    elif answer == "B":
        counters.gryffindor += 1
    elif answer == "C":
        counters.slytherin += 1
    elif answer == "D":
        counters.hufflepuff += 1

        
def eighth_question(counters, answer = ''):
    """ printing the eighth question
        asking the obstacle from Sorcerer's Stone

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printting the question
    print("\n8. Which obstacle from the Sorcerer's Stone" \
          " would you be most successful in completing?")
    
    print("\n A) Mirror of Erised"
          "\n B) Logic and Potions"
          "\n C) Fighting the Mountain troll"
          "\n D) Wizard Chess")

    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.hufflepuff += 1
    elif answer == "B":
        counters.slytherin += 1
    elif answer == "C":
        counters.gryffindor += 1
    elif answer == "D":
        counters.ravenclaw += 1


def ninth_question(counters, answer = ''):
    """ printing the ninth question
        asking about main goal at Hogwarts

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """

    # printing the question
    print("\n9. What is your main goal while attending Hogwarts?")
    
    print("\n A) To learn as much as I can and get the top marks"
          "\n B) To just have a good time"
          "\n C) To be known by all the witches and wizards"
          "\n D) To do whatever it takes to become rich and glorious")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
        counters.ravenclaw += 1
    elif answer == "B":
        counters.hufflepuff += 1
    elif answer == "C":
        counters.gryffindor += 1
    elif answer == "D":
        counters.slytherin += 1

        
def tenth_question(counters, answer = ''):
    """ printing the last question
        asking for their opinion

        Parameters
        ----------
        
        counters: class instance
            an instance of the class Counters
        answer = '': string
            string that will contain an answer choice
            only used during tests to disallow for input
    """
    
    # printing the question
    print("\n10. Lastly, the sorting hat always takes" \
          " your opinion into consideration." \
          " What Hogwarts house do you believe you most closely identify with?")
    
    print("\n A) Gryffindor"
          "\n B) Hufflepuff"
          "\n C) Ravenclaw"
          "\n D) Slytherin")

    #inputting the answer
    if not answer:
        answer = input("Enter your answer: ")

    while answer not in ["A","B","C","D"]:
        print("Not an answer! Are you a muggle?")
        answer = input("Enter your answer: ")

    # calculating score
    if answer == "A":
          counters.gryffindor += 1
    elif answer == "B":
          counters.hufflepuff += 1
    elif answer == "C":
          counters.ravenclaw += 1
    elif answer == "D":
          counters.slytherin += 1

            
# Received this function from A3
def give_max_score(results):
    """ finding the maximum scores of the results list

    Parameters
    ----------

    results: list
        list of all of the user's scores for each house

    Returns
    -------

    final_score: int
        integer containing the maximum score(s)
    """

    final_score = 0

    # uses a for loop to determine if final_score is the maximum value
    for counter in results:
        if counter > final_score:
            final_score = counter

    return final_score


def index_positions_of_results(results, max_score):
    """ finding the indexes of the maximum scores

    Parameters
    ----------

    results: list
        list of all of the user's scores for each house
    max_score: int
        variable assigned to give_max_score function
        integer containing the maximum score(s)

    Results
    -------

    max_score_list: list
        list of all of the user's maximum scores
   """

    max_score_pos = 0
    max_score_list = []

    while True:

        try:
            #Search for the indexes of the max_score to the end of the results list
            max_score_pos = results.index(max_score, max_score_pos)

            #Add the index position in max_score_list
            max_score_list.append(max_score_pos)
            max_score_pos += 1

        except ValueError as error:
            break

    return max_score_list


def get_score(max_score_list):
    """ obtaining the house/houses that correlate with the max score
    
    Parameters
    ----------

    max_score_list: list
        list of all of the user's maximum scores

    Returns
    -------

    output: string
        string containing house(s) of user
    """

    output = " "
    for house in max_score_list:

        if house == 0:
            output += "\nGRYFFINDOR!"
        if house == 1:
            output += "\nHUFFLEPUFF!"
        if house == 2:
            output += "\nRAVENCLAW!"
        if house == 3:
            output += "\nSLYTHERIN!"
           
    return output


def print_score(max_score_list):
    """ printing out the house/houses that correlate with the max score
    
    Parameters
    ----------

    max_score_list: list
        list of all of the user's maximum scores

    Returns
    -------
    
        string that prints out house(s) of user
    """
    
    print(get_score(max_score_list))
    

def sorting_hat_quiz():
    """ Main function to run Sorting Hat Quiz """
    
    # creating an instance of the class Counters
    counters = Counters()

    # asking each question
    first_question(counters)
    second_question(counters)
    third_question(counters)
    fourth_question(counters)
    fifth_question(counters)
    sixth_question(counters)
    seventh_question(counters)
    eighth_question(counters)
    ninth_question(counters)
    tenth_question(counters)

    # list of all of the user's scores for each house
    results = [counters.gryffindor,
               counters.hufflepuff,
               counters.ravenclaw,
               counters.slytherin]
    
    # using give_max_score and index_positions_of_results functions
    max_score = give_max_score(results)
    position = index_positions_of_results(results, max_score)

    # printing the user's house(s)
    print('\nTHE SORTING HAT SAYS:')
    print_score(position)
