from functions import *


def test__firstquestion():
    counters = Counters()
    assert callable(first_question)
    first_question(counters, 'A')
    assert 1 == counters.hufflepuff
    assert 1 == counters.ravenclaw
   
    first_question(counters, 'B')
    assert 1 == counters.slytherin
    assert 2 == counters.ravenclaw
    
    first_question(counters, 'C')
    assert 1 == counters.gryffindor
    assert 3 == counters.ravenclaw 
    

def test__give_max_score():
    assert callable(give_max_score)
    assert isinstance(give_max_score([2, 1, 5, 2]), int)
    assert give_max_score([2, 1, 5, 2]) == 5
    assert give_max_score([2, 5, 5, 2]) == 5

    
def test__get_score():
    assert callable(get_score)
    assert get_score([0]) == " \nGRYFFINDOR!"
    assert get_score([1]) == " \nHUFFLEPUFF!"
    assert get_score([2]) == " \nRAVENCLAW!"
    assert get_score([3]) == " \nSLYTHERIN!"
    
