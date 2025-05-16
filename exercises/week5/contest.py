# The participants of a contest send in their solutions for tasks. The tasks are numbered 1,2,3,\dots, and a solution for each 
# task is worth 0–100 points.

# If a contestant submits multiple solutions to the same task, the score for the task is the maximum score of a single 
# solution. The total score of a contestant is the sum of scores over all tasks.

# Your task is to compile the score board of the contest containing the name and the total score of each contestant. The 
# contestants are sorted by their score from the highest to the lowest. If two contestants have the same score, the one that 
# achieved this score first is listed higher. If two or more participants have a score 0, they are listed in alphabetical order.

# In a file contest.py, implement a class Contest with the following methods:

# __init__: constructs an object of the class
# add_submission: processes the submission of a contestant
# create_scoreboard: creates the score board of the contest

# The following example illustrates the use of the class in detail.

class Contest:
    def __init__(self, names, task_count):
      self.names = names
      self.task_count = task_count
      self.scores = {name: [0] * task_count for name in names}

    def add_submission(self, name, task, score):
      if name in self.scores and task >= 0 and task < self.task_count:
         self.scores[name][task] = max(self.scores[name][task], score)

    def create_scoreboard(self):
      return sorted([(name, sum(tasks)) for name, tasks in self.scores.items()], key=lambda x:-x[1]) # list of tuples (name, score)

names = ["anna", "pekka", "kalle", "tiina", "eeva"]
contest = Contest(names, 3)

contest.add_submission("tiina", 2, 30)
contest.add_submission("pekka", 1, 40)
contest.add_submission("tiina", 1, 20)
contest.add_submission("pekka", 1, 50)
contest.add_submission("pekka", 2, 0)
contest.add_submission("eeva", 3, 100)
contest.add_submission("anna", 1, 0)
contest.add_submission("eeva", 3, 80)
contest.add_submission("tiina", 2, 30)

scoreboard = contest.create_scoreboard()
print(scoreboard)
# [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]

#Tiina is before Pekka on the score board because she reached the score 50 earlier. Anna is before Kalle on the score board, 
# because both have 0 points and Anna is earlier in alphabetical order.