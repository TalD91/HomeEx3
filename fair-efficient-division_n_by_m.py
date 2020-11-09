import cvxpy as cvx
import sys
from cvxpy import log

# helper function for better result display
def truncate(n):
    return int(n * 1000) / 1000

# helper function to sum all elements but the input index
def sum_all_but_index(resource_arr,index):
    sum_of_secondary_resources = 0
    resource_index = 0
    while resource_index < len(resource_arr):
        if index != resource_index:
            sum_of_secondary_resources += resource_arr[resource_index]
        resource_index +=1
    return sum_of_secondary_resources

# main function
def calculate_fair_dividing_n_by_m():
    input_matrix = input("Enter Matrix: ") # should be input of form '[[19,0,0,81],[0,20,0,80],[0,0,40,60]]'

    
    # Parsing string -> string lists -> int 2d lists
    input_matrix = input_matrix[2:len(input_matrix)-2]
    input_matrix = input_matrix.split("],[")
    after_parsing_matrix = []
    for element in input_matrix:
        str_list = element.split(",")
        int_list = []
        for str_part in str_list:
            int_list.append(int(str_part))
        after_parsing_matrix.append(int_list)

    input_matrix = after_parsing_matrix

    rows = len(input_matrix)
    cols = len(input_matrix[0])
    cols_index = 0

    player_chances_lines = []
    index = 0

    # Building the output
    while index < rows:
        line = "Agent #{} gets".format(index+1)
        player_chances_lines.append(line)
        index += 1

    # Building contrainsts and variables for each resource separately and concating output to one list 
    while cols_index < cols:
        cvx_variable_arr = []
        index = 0
        while index < rows:
            cvx_variable_arr.append(cvx.Variable())
            index += 1
    
        index = 0
        constraints = []
        equations = []

        # Building constraints ( 0 <= xi <= 1 ) and objective equations - (log(m*x + all resources))
        while index < len(input_matrix):
            constraints.append(cvx_variable_arr[index] >= 0)
            constraints.append(cvx_variable_arr[index] <= 1)
            equations.append(log(input_matrix[index][cols_index]*cvx_variable_arr[index] + sum_all_but_index(input_matrix[index],cols_index)))
            index += 1
    
        # adding the last constraint (x + y + z <= 1)
        constraints.append(cvx.sum(cvx_variable_arr) <= 1)

        # building the problem and solving it
        problem = cvx.Problem(
            objective = cvx.Maximize(cvx.sum(equations)),
            constraints = constraints
        )

        problem.solve()
        index = 0

        # appending output for this resources
        while index < len(input_matrix):
            player_chances_lines[index] += " {} of resource #{},".format(truncate(cvx_variable_arr[index].value),cols_index+1)
            index += 1

        cols_index += 1 # going to next resource
    
    # printing everything
    for element in player_chances_lines:
        print(element)

if __name__ == "__main__":
    calculate_fair_dividing_n_by_m()
