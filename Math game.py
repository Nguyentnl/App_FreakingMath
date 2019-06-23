""""
    This is a game based on Freaking Math game on android where the player have to say "right"/YES or "wrong"/NO
    for each given equation
"""

from random import randint


print "Write Y when the result is right or N with wrong result, and press ENTER"

class no_enter(object):
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


class FreakingMath(object):
    def __init__(self, first_number, second_number, real_result, print_result):
        self.first_number = first_number
        self.second_number = second_number
        self.user_answer = None
        self.real_result = real_result
        self.print_result = print_result

    def generate_equation(self):
        """Print the math problem"""
        print '%s + %s = %s' % (first_number, second_number, print_result)

    def set_user_answer(self):
        """Ask the user to input the answer"""
        while True:
            try:
                self.user_answer = raw_input('Y/N: ')
                """Assertion for user_answer"""
                assert self.user_answer.lower() == "y" or self.user_answer.lower() == "n"
                break
            except AssertionError:
                print 'Please enter a valid answer'
        return self.user_answer

    def is_answer_correctly_true(self):
        return real_result == print_result and self.user_answer.lower() == 'y'

    def is_answer_correctly_false(self):
        return real_result != print_result and self.user_answer.lower() == 'n'

    def game_result(self):
        """To check if the user answers correctly"""
        if self.is_answer_correctly_true() or self.is_answer_correctly_false():
            print 'Your answer is correct!',
            print 'Next one: '
            return True
        else:
            print 'Your answer is wrong! Game over'
            return False


last_result = True
count = 0
while last_result:
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    real_result = first_number + second_number
    print_result = randint(real_result - 1, real_result + 1)

    get = no_enter()
    game = FreakingMath(first_number, second_number, real_result, print_result)
    game.generate_equation()
    game.set_user_answer()
    last_result = game.game_result()
    count += 1
else:
    print 'You answered correctly', count, 'times'
