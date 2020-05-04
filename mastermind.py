import copy
import random
import itertools  
# 6 colors
# 10 tries?

class Mastermind:
    def __init__(self, solution=None):
        if solution is None:
            self.solution = self.get_random_solution()
        else:
            self.solution = solution
        print(solution)

    def get_random_solution(self):
        solution = []
        for i in range(4):
            solution.append(random.randrange(0,6))

        return solution

    def check_guess(self, guess):
        correct = self.get_correct_colors(guess)
        misplaced = self.get_misplaced_colors(guess, correct)

        print("correct: {}, misplaced: {}".format(correct.count(True), misplaced.count(True)))
        print(correct)
        print(self.solution)

        return correct.count(True), misplaced.count(True)

    def is_won(self, guess):
        for g, s in zip(guess, self.solution):
            if g != s:
                return False
        return True

    def get_correct_colors(self, guess):
        correct_list = []
        for g, s in zip(guess, self.solution):
            if g == s:
                correct_list.append(True)
            else:
                correct_list.append(False)
        return correct_list

    def get_misplaced_colors(self, guess, correct_list):
        mock_solution = copy.copy(self.solution)
        misplaced_list = []
        for index, (status, g, s) in enumerate(zip(correct_list, guess, mock_solution)):
            if status == True:
                guess[index] = 0
                mock_solution[index] = 0
            print(guess)
        
        for color in guess:
            if color is 0:
                misplaced_list.append(False)
            elif color in mock_solution:
                misplaced_list.append(True)
                mock_solution.remove(color)
            else:
                misplaced_list.append(False)
            
        return misplaced_list