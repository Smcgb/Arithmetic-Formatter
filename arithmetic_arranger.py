def arithmetic_arranger(problems, answers=False):
  """
  Input - Prblems - string - list of arithmetic problems and a bool that defaults to false
  Output - Prints problems in an arithmetics style for better viewing. 
  Will not display answers unless input bool is set to true.
  
  Returns no values as it is for printing only. Other info can be found at:

  https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
  """

  # check for letters in the problems
  for problem in problems:
    problem = problem.lower()
    if problem.islower() == True:
        return("Error: Numbers must only contain digits.")
        

  # Check if there are more than 5 problems
  if len(problems) > 5:
        return("Error: Too many problems.")
          
  # Check if there are any problems
  elif len(problems) == 0:
        return("Error: No problems provided.")
          

  # Check operators, this function will only work with + and -
  for problem in problems:
    if "+" not in problem and "-" not in problem:
       return("Error: Operator must be '+' or '-'.")
       
    elif "*" in problem or "/" in problem:
       return("Error: Operator must be '+' or '-'.")
       

    # ensure that there are no more than 4 digits in each number
  for problem in problems:
    split = []
    if len(problem) > 7:
      split = problem.split()
      if len(split[0]) > 4 or len(split[2]) > 4:
        return("Error: Numbers cannot be more than four digits.")
        

  #create list of numbers and operators

  first_num = []
  second_num = []
  answer_list = []
  seplist = []

  for problem in problems:
    split = problem.split()
    op = split[1]

    # get answers if bool is true
    if answers:
        a = int(split[0])
        b = int(split[2])
        answer = a + b if op == "+" else a - b

    # get the width of the longer number
    width = len(max([split[0], split[2]], key=len))

    # dyanmic separator line
    separator = "-" * (width + 2)
    seplist.append(separator)

    # right align numbers
    first_num.append(split[0].rjust(width + 2))
    second_num.append(op + " " + split[2].rjust(width))

    # get answers if bool is true
    if answers:
        answer_list.append(str(answer).rjust(width + 2))

  top_line = "    ".join(first_num)
  bottom_line = "    ".join(second_num)
  separator = "    ".join(seplist)
  if answers:
    answer_line = "    ".join(answer_list)

  if answers:
    arranged_problems = f"{top_line}\n{bottom_line}\n{separator}\n{answer_line}"
  else:
    arranged_problems = f"{top_line}\n{bottom_line}\n{separator}"
      
  return arranged_problems