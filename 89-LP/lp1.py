#Topic: Linear Programming in Python
#-----------------------------
#https://realpython.com/linear-programming-python/
#libraries

from scipy.optimize import linprog
obj = [-1, -2]
#   ─┬  ─┬
#    │   └┤ Coefficient for y
#    └────┤ Coefficient for x

#lhs_ineq = [[ 2,  1],  # Red constraint left side
#            [-4,  5],  # Blue constraint left side
#            [ 1, -2]]  # Yellow constraint left side
# obj holds the coefficients from the objective function.
# lhs_ineq holds the left-side coefficients from the inequality (red, blue, and yellow) constraints.
# rhs_ineq holds the right-side coefficients from the inequality (red, blue, and yellow) constraints.
# lhs_eq holds the left-side coefficients from the equality (green) constraint.
# rhs_eq holds the right-side coefficients from the equality (green) constraint.

lhs_ineq = [[ 2,  1],[-4,  5],  [ 1, -2]]
lhs_ineq
# rhs_ineq = [20,  # Red constraint right side
#             10,  # Blue constraint right side
#             2]  # Yellow constraint right side
rhs_ineq = [20, 10,2]
rhs_ineq

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constraint right side

# Please, be careful with the order of rows and columns!
# The order of the rows for the left and right sides of the constraints must be the same. Each row represents one constraint.
# The order of the coefficients from the objective function and left sides of the constraints must match. Each column corresponds to a single decision variable.

bnd = [(0, float('inf')), (0, float('inf')) ] #bounds for x and y
#solve the problem
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq = rhs_eq, bounds = bnd, method ='revised simplex')
opt

#values 
opt.fun
opt.success
opt.x

#%%
#if equality(green) constraint has to be excluded, drop parameters of A_ea and b_eq
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method='revised simplex')
opt


#%% Resource Allocation Problem
#Factory produces 4 different products
#daily produced items is x1, x2,... 
#goal : Determin profit max daily production amount for each product with conditions
#Profit per unit resp - 20, 12, 40, 25
#total daily units produced < 50
#raw material A & B type
#each unit of : x1 needs 2 * A ; x2 needs 2*A + 1*B; x3 needs 1*A + 2*B; x4 needs 3*B
#factory can take max of 100 units of A and 90 units of B

#max 20x1 + 12x2 + 40x3 + 25x4  (profit)- Objective Function
#st : x1  + x2  + x3  + x4  <= 50  (manpower constraint)
#     3x1 + 2x2 + x3        <= 100 (Material A Constraint)
#            x2 + 2x3 + 2x4 <= 90  (Material B Constraint)
#      x1,x2, x3, x4        >= 0
#install packages if not done
#pip install scipy
#pip install pulp
from scipy.optimise import linprog




#%%
pip install pulp
from pulp import GLPK
model = LpProblem(name="resource-allocation", sense=LpMaximize)

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 5)}
y = {i: LpVariable(name=f"y{i}", cat="Binary") for i in (1, 3)}

# Add constraints
model += (lpSum(x.values()) <= 50, "manpower")
model += (3 * x[1] + 2 * x[2] + x[3] <= 100, "material_a")
model += (x[2] + 2 * x[3] + 3 * x[4] <= 90, "material_b")

M = 100
model += (x[1] <= y[1] * M, "x1_constraint")
model += (x[3] <= y[3] * M, "x3_constraint")
model += (y[1] + y[3] <= 1, "y_constraint")

# Set objective
model += 20 * x[1] + 12 * x[2] + 40 * x[3] + 25 * x[4]

# Solve the optimization problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}") 