import cvxpy as cvx
import sys
from cvxpy import log

def calculateFairAndSquare():
    #input_matrix = input("Enter Matrix: ")
    input_matrix = [[19,0,0,81],[0,20,0,80],[0,0,40,60]]
    rows = len(input_matrix)

    cvx_variable_arr = []
    index = 0
    while index < rows:
        cvx_variable_arr.append(cvx.Variable())
        index += 1
    
    index = 0
    constraints = []
    equations = []
    while index < len(input_matrix):
        constraints.append(cvx_variable_arr[index] >= 0)
        constraints.append(cvx_variable_arr[index] <= 1)
        equations.append(log(max(input_matrix[index])*cvx_variable_arr[index] + sum(input_matrix[index])-max(input_matrix[index])))
        index += 1
    
    constraints.append(cvx.sum(cvx_variable_arr) <= 1)

    problem = cvx.Problem(
        objective = cvx.Maximize(cvx.sum(equations)),
        constraints = constraints
    )

    problem.solve()
    print ("optimal value", problem.value)
    index = 0
    while index < len(input_matrix):
        print("optimal variable #{}: {}".format(index+1,cvx_variable_arr[index].value))
        index += 1

if __name__ == "__main__":
    calculateFairAndSquare()
