import numpy as np
import sys 
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("\n==== TASK ====")
print("1. SCIENTIFIC CALCULATOR")
print("2. MATHS TOOLKIT")
print("3. FUNCTION PLOTTER")
print("4. CALCULUS TOOLKIT")
print("5. GRADIENT DECENT")
print("6. GRADIENT DECENT VISUALIZER")

try:
    task = int(input("Enter your task between 1 and 6: "))
except Exception:
    print("Please enter numeric values only!!!")
    sys.exit()

if task < 1 or task > 6:
    print("Please enter a valid task between 1 to 6!!!")
    sys.exit()

# =================================================================================================================================================================
if task == 1:
# =================================================================================================================================================================

    print("\n==== SCIENTIFIC CALCULATOR ====")
    print("1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION")
    print("5. POWER\n6. SQUARE ROOT\n7. LOGARITHM\n8. LOGARITHM WITH BASE 10")
    print("9. SIN\n10. COS\n11. TAN\n12. ARCSIN\n13. ARCCOS\n14. ARCTAN")

    try:
        choice = int(input("Enter the choice between 1 to 14: "))
        
        if choice < 1 or choice > 14:
            print("Please enter a valid choice between 1 to 14.")
            sys.exit()

        if choice == 1:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("SUM: ", np.add(a, b))

        elif choice == 2:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("DIFFERENCE: ", np.subtract(a, b))

        elif choice == 3:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("PRODUCT: ", np.multiply(a, b))  

        elif choice == 4:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            if b == 0:
                print("Cannot divide by zero!")
            else:
                print("QUOTIENT: ", np.divide(a, b)) 

        elif choice == 5:
            a = float(input("Enter the base: "))
            b = float(input("Enter the power: "))
            print("POWER: ", np.power(a, b)) 

        elif choice == 6:
            a = float(input("Enter the number: "))
            if a < 0:
                print("ERROR: Cannot calculate real square root of a negative number!")
            else:
                print("SQUARE ROOT: ", np.sqrt(a))

        elif choice == 7:
            a = float(input("Enter the number: "))
            if a <= 0:
                print("ERROR: Logarithm is only defined for numbers greater than 0!")
            else:
                print("log(x): ", np.log(a))

        elif choice == 8:
            a = float(input("Enter the number: "))
            if a <= 0:
                print("ERROR: Logarithm is only defined for numbers greater than 0!")
            else:
                print("log10(x): ", np.log10(a))

        elif choice in [9, 10, 11]:
            degree = float(input("Enter the angle in degree: "))
            angle = np.deg2rad(degree)
            if choice == 9:
                print("SIN: ", np.sin(angle))
            elif choice == 10:
                print("COS: ", np.cos(angle))
            elif choice == 11:
                print("TAN: ", np.tan(angle))

        elif choice in [12, 13]:
            a = float(input("Enter the number (between -1 and 1): "))
            if -1 <= a <= 1:
                if choice == 12:
                    print("ANGLE: ", np.rad2deg(np.arcsin(a)))
                elif choice == 13:
                    print("ANGLE: ", np.rad2deg(np.arccos(a)))
            else:
                print("ERROR: Value must be between -1 and 1!")

        elif choice == 14:
            a = float(input("Enter the number: "))
            print("ANGLE: ", np.rad2deg(np.arctan(a)))

    except ValueError:
        print("INVALID INPUT! Please enter numeric values only!!!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# =================================================================================================================================================================
elif task == 2:
# =================================================================================================================================================================

    # =========================================================
    # MATRIX INPUT FUNCTION
    # =========================================================

    def input_matrix():
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        matrix = []

        for i in range(rows):
            while True:
                row = list(map(int,input(f"Enter row {i + 1} (space separated): ").split()))
                if len(row) == cols:
                    matrix.append(row)
                    break
                print(f"Please enter exactly {cols} numbers.")

        return np.array(matrix)


    # =========================================================
    # MATRIX CALCULATOR
    # =========================================================

    def matrix_calculator():
        print("\n===== MATRIX CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose of A")
        print("5. Transpose of B")
        print("6. Determinant of A")
        print("7. Determinant of B")
        print("8. Inverse of A")
        print("9. Inverse of B")
        print("10. Scalar multiplication of A")
        print("11. Scalar multiplication of B")
        print("12. Rank of A")
        print("13. Rank of B")
        print("14. Eigenvalues and Eigenvectors of A")
        print("15. Power of A")
        print("16. Power of B")

        try:
            choice = int(input("Enter the choice between 1 to 16: "))
        except Exception:
            print("Please enter a valid numeric value!!!")
            sys.exit()

        if choice < 1 or choice > 16:
            print("Please enter a valid choice between 1 to 16!!!")
            sys.exit()

        # ADDITION
        if choice == 1:
            print("\nEnter Matrix A:")
            A = input_matrix()
            print("\nEnter Matrix B:")
            B = input_matrix()
            if A.shape == B.shape:
                print("\nSum:\n", A + B)
            else:
                print("Error: Both matrices must have the same dimensions.")

        # SUBTRACTION
        elif choice == 2:
            print("\nEnter Matrix A:")
            A = input_matrix()
            print("\nEnter Matrix B:")
            B = input_matrix()
            if A.shape == B.shape:
                print("\nDifference:\n", A - B)
            else:
                print("Error: Both matrices must have the same dimensions.")

        # MULTIPLICATION
        elif choice == 3:
            print("\nEnter Matrix A:")
            A = input_matrix()
            print("\nEnter Matrix B:")
            B = input_matrix()
            if A.shape[1] == B.shape[0]:
                print("\nProduct:\n", A @ B)
            else:
                print("Error: Number of columns of A must be equal to number of rows of B.")

        # TRANSPOSE A
        elif choice == 4:
            print("\nEnter Matrix A:")
            A = input_matrix()
            print("\nTranspose of A:\n", A.T)

        # TRANSPOSE B
        elif choice == 5:
            print("\nEnter Matrix B:")
            B = input_matrix()
            print("\nTranspose of B:\n", B.T)

        # DETERMINANT A
        elif choice == 6:
            print("\nEnter Matrix A:")
            A = input_matrix()
            if A.shape[0] == A.shape[1]:
                print("\nDeterminant of A:\n", np.linalg.det(A))
            else:
                print("Error: Determinant requires a square matrix.")

        # DETERMINANT B
        elif choice == 7:
            print("\nEnter Matrix B:")
            B = input_matrix()
            if B.shape[0] == B.shape[1]:
                print("\nDeterminant of B:\n", np.linalg.det(B))
            else:
                print("Error: Determinant requires a square matrix.")

        # INVERSE A
        elif choice == 8:
            print("\nEnter Matrix A:")
            A = input_matrix()
            if A.shape[0] != A.shape[1]:
                print("Error: Inverse requires a square matrix.")
            elif np.isclose(np.linalg.det(A), 0):
                print("Error: Please enter a non-singular matrix (Determinant shouldn't be 0).")
            else:
                print("\nInverse of A:\n", np.linalg.inv(A))

        # INVERSE B
        elif choice == 9:
            print("\nEnter Matrix B:")
            B = input_matrix()
            if B.shape[0] != B.shape[1]:
                print("Error: Inverse requires a square matrix.")
            elif np.isclose(np.linalg.det(B), 0):
                print("Error: Please enter a non-singular matrix (Determinant shouldn't be 0).")
            else:
                print("\nInverse of B:\n", np.linalg.inv(B))

        # SCALAR MULTIPLICATION A
        elif choice == 10:
            print("\nEnter Matrix A:")
            A = input_matrix()
            n = float(input("Enter the number to be multiplied with A: "))
            print("\nResult:\n", A * n)

        # SCALAR MULTIPLICATION B
        elif choice == 11:
            print("\nEnter Matrix B:")
            B = input_matrix()
            n = float(input("Enter the number to be multiplied with B: "))
            print("\nResult:\n", B * n)

        # RANK A
        elif choice == 12:
            print("\nEnter Matrix A:")
            A = input_matrix()
            print("The rank of Matrix A is:\n", np.linalg.matrix_rank(A))

        # RANK B
        elif choice == 13:
            print("\nEnter Matrix B:")
            B = input_matrix()
            print("The rank of Matrix B is:\n", np.linalg.matrix_rank(B))

        # EIGENVALUES AND EIGENVECTORS
        elif choice == 14:
            print("\nEnter Matrix A:")
            A = input_matrix()
            if A.shape[0] != A.shape[1]:
                print("Error: Eigenvalues and eigenvectors require a square matrix.")
            else:
                eigenvalues, eigenvectors = np.linalg.eig(A)
                print("\nEigenvalues:\n", eigenvalues)
                print("\nEigenvectors:\n", eigenvectors)

        # POWER OF A
        elif choice == 15:
            print("\nEnter Matrix A:")
            A = input_matrix()
            if A.shape[0] != A.shape[1]:
                print("Matrix power requires a square matrix!!")
            else:
                n = int(input("Enter the power: "))
                print("Result:\n", np.linalg.matrix_power(A, n))

        # POWER OF B
        elif choice == 16:
            print("\nEnter Matrix B:")
            B = input_matrix()
            if B.shape[0] != B.shape[1]:
                print("Matrix power requires a square matrix!!")
            else:
                n = int(input("Enter the power: "))
                print("Result:\n", np.linalg.matrix_power(B, n))


    # =========================================================
    # POLYNOMIAL SOLVER
    # =========================================================

    def polynomial_solver():
        degree = int(input("Enter the degree: "))
        if degree == 0:
            constant = float(input("Enter the constant: "))
            if constant == 0:
                print("Infinite solutions")
            else:
                print("No solutions")
            return

        coefficients = list(map(float,input(f"Enter {degree + 1} coefficients separated by space: ").split()))
        
        if len(coefficients) != degree + 1:
            print(f"Please enter exactly {degree + 1} coefficients.")
            return

        if coefficients[0] == 0:
            print("Leading coefficient cannot be zero.")
            return

        roots = np.roots(coefficients)
        print("\nROOTS ARE:")
        for i, root in enumerate(roots, start=1):
            print(f"x{i} = {root}")


    # =========================================================
    # STATISTICS SOLVER
    # =========================================================

    def statistics():
        print("\n===== STATISTICAL OPERATIONS =====")
        print("1. Max\n2. Min\n3. Standard deviation\n4. Variance")
        print("5. Mean\n6. Sum\n7. Mode\n8. Median")

        choice = input("Enter the choice: ").strip()
        
        if choice not in [str(i) for i in range(1, 9)]:
            print("Invalid choice!")
            return

        try:
            a = np.array(list(map(float, input("Enter numbers separated by space: ").split()))) 
            print("\nArray:", a)
        except ValueError:
            print("Please enter valid numbers only.")
            return

        if choice == "1": 
            print("MAXIMUM: ", np.max(a))
        elif choice == "2":
            print("MINIMUM: ", np.min(a))
        elif choice == "3":
            print("STANDARD DEVIATION: ", np.std(a))
        elif choice == "4":
            print("VARIANCE: ", np.var(a))
        elif choice == "5":
            print("MEAN: ", np.mean(a))
        elif choice == "6":
            print("SUM: ", np.sum(a))
        elif choice == "7":
            vals, counts = np.unique(a, return_counts=True)
            mode_val = vals[np.argmax(counts)]
            print("MODE: ", mode_val)
        elif choice == "8":
            print("MEDIAN: ", np.median(a))


    # =========================================================
    # MAIN MENU
    # =========================================================

    def main_menu():
        while True:
            print("\n===== MATHS TOOLKIT =====")
            print("1. Matrix solver")
            print("2. Polynomial solver")
            print("3. Statistics solver")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except Exception: 
                print("Please enter numeric values only!!!")
                sys.exit()

            if choice < 1 or choice > 3:
                print("Please enter a valid choice between 1 and 3: ")

            if choice == 1:
                matrix_calculator()
            elif choice == 2:
                polynomial_solver()
            elif choice == 3:
                statistics()
            else:
                print("\nSomething went wrong! Please enter a number between 1 and 4.")


    # =========================================================
    # START PROGRAM
    # =========================================================

    main_menu()

# =================================================================================================================================================================
elif task == 3:
# =================================================================================================================================================================

    try:
        dimension = int(input("Enter the dimension btween 1 and 3: "))
    except Exception:
        print("Please enter a valid numeric value between 1 and 3!!!")
        sys.exit()

    if dimension < 1 or dimension > 3:
        print("Please enter a valid dimension between 1 and 3: ")
        sys.exit()

    if dimension == 1:

        expression = input("Enter the function f(x): ").replace("^", "**")

        try:
            x_min = float(input("Enter the minimum value for x: "))
            x_max = float(input("Enter the maximum value for x: "))
        except ValueError:
            print("Please enter valid numeric value for x!!!")
            sys.exit()

        if x_min >= x_max:
            print("INVALID RANGE!!! \nMinimum x cannot be greater than maximum x!!!")
            sys.exit()

        try:
            resolution = int(input("Enter the number of resolutions for x: "))
        except Exception:
            print("Resolution must be an integer!!!")
            sys.exit()

        if resolution <= 0:
            print("Number of resolutions must be greater than zero!!!")
            sys.exit()

        allowed = {
            "x" : None, 
            "sin" : np.sin,
            "cos" : np.cos,
            "tan" : np.tan,
            "sqrt" : np.sqrt,
            "arcsin" : np.arcsin,
            "arccos" : np.arccos,
            "arctan" : np.arctan,
            "log" : np.log,
            "exp" : np.exp,
            "pi" : np.pi,
            "e" : np.e, 
            "sinh" : np.sinh, 
            "cosh" : np.cosh, 
            "tanh" : np.tanh,
            "log10" : np.log10, 
            "abs" : np.abs, 
            "floor" : np.floor, 
            "ceil" : np.ceil
        }

        def f(x):
            values = allowed.copy()
            values["x"] = x

            with np.errstate(all = "ignore"):
                y = eval(expression, {"__builtins__": {}}, values)
                if isinstance(y, (int, float)):
                    y = y*np.ones_like(x)

            valid = np.isfinite(y)

            if not np.any(valid):
                print("Function produced no valid values in the given range!!!")
                sys.exit()

            y[~valid] = np.nan

            difference = np.abs(np.diff(y))

            finite_difference = difference[np.isfinite(difference)]

            if len(finite_difference) > 0:
                median_difference = np.median(finite_difference)
            else:
                median_difference = 0

            if median_difference > 0:
                threshold = 100*median_difference

                jump = difference > threshold
                y[:-1][jump] = np.nan
                y[1:][jump] = np.nan

            return y

        x = np.linspace(x_min, x_max, resolution)

        try: 
            y = f(x)
        except Exception:
            print("Please enter a valid function!!!")
            sys.exit()

        plt.plot(x, y, label = f"function: {expression}")

        plt.axhline(0, color = "black")
        plt.axvline(0, color = "black")

        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("FUNCTIONS PLOTTER", color = "maroon")

        plt.legend()
        plt.grid()
        plt.show()

    elif dimension == 2:

        expression = input("Enter the function f(x, y): ").replace("^", "**")

        try:
            x_min = float(input("Enter the minimum value for x: "))
            x_max = float(input("Enter the maximum value for x: "))

        except ValueError:
            print("Please enter valid numeric values for x!!!")
            sys.exit()


        try:
            y_min = float(input("Enter the minimum value of y: "))
            y_max = float(input("Enter the maximum value of y: "))
        except ValueError:
            print("Please enter a valid numeric value for y!!!")
            sys.exit()

        if x_min >= x_max:
            print("INVALID RANGE!!! \nMinimum x cannot be greater than maximum x!!!")
            sys.exit()

        if y_min >= y_max:
            print("INVALID RANGE!!! \nMinimum y cannot be greater than maximum y!!!")
            sys.exit()

        try:
            resolution = int(input("Enter the number of resolutions for both x and y: "))
        except ValueError:
            print("Resolution must be an integer!!!")
            sys.exit()

        if resolution <= 0:
            print("Number of resolutions must be greater than zero!!!")
            sys.exit()

        if resolution < 50 or resolution > 2000:
            print("Resolution must be between 50 and 2000!!!")
            sys.exit()

        allowed = {
            "x" : None, 
            "y" : None,
            "sin" : np.sin,
            "cos" : np.cos,
            "tan" : np.tan,
            "sqrt" : np.sqrt,
            "arcsin" : np.arcsin,
            "arccos" : np.arccos,
            "arctan" : np.arctan,
            "log" : np.log,
            "exp" : np.exp,
            "pi" : np.pi,
            "e" : np.e, 
            "sinh" : np.sinh, 
            "cosh" : np.cosh, 
            "tanh" : np.tanh,
            "log10" : np.log10, 
            "abs" : np.abs, 
            "floor" : np.floor, 
            "ceil" : np.ceil
        }

        def f(x, y):
            values = allowed.copy()
            values["x"] = x
            values["y"] = y

            with np.errstate(all = "ignore"):
                result = eval(expression, {"__builtins__": {}}, values)
                if isinstance(result, (int, float)):
                    result = result*np.ones_like(x)


            return result

        x = np.linspace(x_min, x_max, resolution)
        y = np.linspace(y_min, y_max, resolution)

        X, Y = np.meshgrid(x, y)

        try:
            F = f(X, Y)
        except Exception:
            print("Please enter a valid function!!!")
            sys.exit()

        valid = np.isfinite(F)
        if not np.any(valid):
            print("Function produced no valid values in the given range!!!")
            sys.exit()

        F[~valid] = np.nan

        if np.nanmin(F) > 0 or np.nanmax(F) < 0:
            print("No real curve is found in the given range!!!")
            sys.exit()

        contour = plt.contour(X, Y, F, levels = [0], colors = "blue")

        plt.axis("equal")

        plt.axhline(0, color = "black")
        plt.axvline(0, color = "black")

        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title(f"f(x, y) = {expression}", color = "maroon")

        plt.grid(linestyle = "--")
        plt.show()

    else:

        fig = plt.figure()
        ax = fig.add_subplot(111, projection = "3d")

        expression = input("Enter the function f(x, y, z): ").replace("^", "**")

        try:
            x_min = float(input("Enter the minimum value for x: "))
            x_max = float(input("Enter the maximum value for x: "))

        except ValueError:
            print("Please enter valid numeric values for x!!!")
            sys.exit()


        try:
            y_min = float(input("Enter the minimum value of y: "))
            y_max = float(input("Enter the maximum value of y: "))
        except ValueError:
            print("Please enter a valid numeric value for y!!!")
            sys.exit()

        try:
            z_min = float(input("Enter the minimum value of z: "))
            z_max = float(input("Enter the maximum value of z: "))
        except ValueError:
            print("Please enter a valid numeric value for z!!!")
            sys.exit()

        if x_min >= x_max:
            print("INVALID RANGE!!! \nMinimum x cannot be greater than maximum x!!!")
            sys.exit()

        if y_min >= y_max:
            print("INVALID RANGE!!! \nMinimum y cannot be greater than maximum y!!!")
            sys.exit()

        if z_min >= z_max:
            print("INVALID RANGE!!! \nMinimum z cannot be greater than maximum z!!!")
            sys.exit()

        try:
            resolution = int(input("Enter the number of resolutions for both x, y and z: "))
        except ValueError:
            print("Resolution must be an integer!!!")
            sys.exit()

        if resolution <= 0:
            print("Number of resolutions must be greater than zero!!!")
            sys.exit()

        if resolution < 50 or resolution > 150:
            print("Resolution must be between 50 and 150!!!")
            sys.exit()

        allowed = {
            "x" : None, 
            "y" : None,
            "z" : None,
            "sin" : np.sin,
            "cos" : np.cos,
            "tan" : np.tan,
            "sqrt" : np.sqrt,
            "arcsin" : np.arcsin,
            "arccos" : np.arccos,
            "arctan" : np.arctan,
            "log" : np.log,
            "exp" : np.exp,
            "pi" : np.pi,
            "e" : np.e, 
            "sinh" : np.sinh, 
            "cosh" : np.cosh, 
            "tanh" : np.tanh,
            "log10" : np.log10, 
            "abs" : np.abs, 
            "floor" : np.floor, 
            "ceil" : np.ceil
        }

        def f(x, y, z):
            values = allowed.copy()
            values["x"] = x
            values["y"] = y
            values["z"] = z

            with np.errstate(all = "ignore"):
                result = eval(expression, {"__builtins__": {}}, values)
                if isinstance(result, (int, float)):
                    result = result*np.ones_like(x)

            return result

        x = np.linspace(x_min, x_max, resolution)
        y = np.linspace(y_min, y_max, resolution)
        z = np.linspace(z_min, z_max, resolution)

        X, Y, Z = np.meshgrid(x, y, z, indexing = "ij")

        try:
            F = f(X, Y, Z)
        except Exception:
            print('''
        Invalid Function!!!
        Please check: 
        - Variable names: x, y, z
        - Mathematical syntax
        - Supported functions
        ''')
            sys.exit()

        valid = np.isfinite(F)

        if not np.any(valid):
            print("Function produced no valid value in the given range!!!")
            sys.exit()

        if not np.all(valid):
            print("Function produced undefined values in the given range!!!")
            print("Please choose a different range or modify the given function!!!")
            sys.exit()

        if np.min(F) > 0 or np.max(F) < 0:
            print("No real surface is found in the given range!!!")
            sys.exit()

        try:
            from skimage.measure import marching_cubes
        except ImportError:
            print("scikit-image is required for 3D implicit plotting!!!")
            print("\nInstall it using:")
            print("\npip install scikit-image")
            sys.exit()

        try:
            vertices, faces, normals, values = marching_cubes(F, level = 0)
        except RuntimeError:
            print("No surface found for f(x, y, z) = 0 in the given range!!!")
            sys.exit()

        vertices[:, 0] = np.interp(vertices[:, 0], np.arange(resolution), x)
        vertices[:, 1] = np.interp(vertices[:, 1], np.arange(resolution), y)
        vertices[:, 2] = np.interp(vertices[:, 2], np.arange(resolution), z)

        ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], alpha = 0.7)

        ax.set_title(f"3D FUNCTIONS PLOTTER\nf(x, y, z) = {expression}", color = "maroon", weight = "bold")

        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.set_zlabel("z-axis")

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_zlim(z_min, z_max)

        ax.view_init(elev = 25, azim = 45)

        ax.set_box_aspect((1, 1, 1))

        plt.tight_layout()

        plt.grid(linestyle = "--")
        plt.show()

# =================================================================================================================================================================
elif task == 4:
# =================================================================================================================================================================

    print("\n==== CHOOSE CALCULUS TOPIC ====")
    print("1. Differentiation")
    print("2. Integration")

    topic = int(input("Choose the topic between 1 and 2: "))

    if topic < 1 or topic > 2:
        print("Please enter a valid topic between 1 and 2: ")
        sys.exit()

    # ===============================================================================================================================================================
    if topic == 1:
    # ===============================================================================================================================================================

        dimension = int(input("Enter the dimension from 1D to 3D: "))

        if dimension < 1 or dimension > 3:
            print("Please enter a valid choice of dimensions between 1 to 3!!!")
            sys.exit()

        def DerivativeApproximation(f, x, y, z, h):

            if dimension == 1:

                print("\n==== CHOOSE APPROXIMATION METHOD ====")
                print("1. Forward")
                print("2. Backward")
                print("3. Central")

                choice = int(input("Enter your choice between 1 to 3: "))

                if choice == 1:
                    return (f(x+h) - f(x))/h
                elif choice == 2:
                    return (f(x) - f(x-h))/h
                elif choice == 3:
                    return (f(x+h) - f(x-h))/(h*2)
                else:
                    print("Please enter a valid choice between 0 to 3!!! ")
                    sys.exit()


            if dimension == 2:
                print("\n==== CHOOSE DIFFERENTIATION METHOD ====")
                print("1. Differentiate with respect to x")
                print("2. Differentiate with respect to y")

                choice = int(input("Enter your choice between 1 to 2: "))

                if choice == 1:
                    return (f(x+h, y) - f(x-h, y))/(2*h)
                elif choice == 2:
                    return (f(x, y+h) - f(x, y-h))/(2*h)
                else:
                    print("Please enter a valid choice between 1 to 2!!! ")
                    sys.exit()

            if dimension == 3:

                print("\n==== CHOOSE DIFFERENTIATION METHOD ====")
                print("1. Differentiate with respect to x")
                print("2. Differentiate with respect to y")
                print("3. Differentiate with respect to z")

                choice = int(input("Enter your choice between 1 to 3: "))

                if choice == 1:
                    return (f(x+h, y, z) - f(x-h, y, z))/(2*h)
                elif choice == 2:
                    return (f(x, y+h, z) - f(x, y-h, z))/(2*h)
                elif choice == 3:
                    return (f(x, y, z+h) - f(x, y, z-h))/(2*h)
                else:
                    print("Please enter a valid choice between 1 to 3!!! ")
                    sys.exit()

        if dimension == 1:
            expression = input("Enter the function f(x): ")
        elif dimension == 2:
            expression = input("Enter the function f(x, y): ")
        else:
            expression = input("Enter the function f(x, y, z): ")

        allowed = {
            "x" : None, 
            "y" : None,
            "z" : None,
            "sin" : math.sin,
            "cos" : math.cos,
            "tan" : math.tan,
            "sqrt" : math.sqrt,
            "asin" : math.asin,
            "acos" : math.acos,
            "atan" : math.atan,
            "log" : math.log,
            "exp" : math.exp,
            "pi" : math.pi,
            "e" : math.e
        }

        if dimension == 1:

            def f(x):
                values = allowed.copy()
                values["x"] = x
                return eval(expression, {"__builtins__": {}}, values)

        elif dimension == 2:

            def f(x, y):
                values = allowed.copy()
                values["x"] = x
                values["y"] = y
                return eval(expression, {"__builtins__": {}}, values)

        else:

            def f(x, y, z):
                values = allowed.copy()
                values["x"] = x
                values["y"] = y
                values["z"] = z  
                return eval(expression, {"__builtins__": {}}, values)

        x = float(input("Enter the value of x: "))

        if dimension >= 2:
            y = float(input("Enter the value of y: "))
        else:
            y = 0

        if dimension == 3:
            z = float(input("Enter the value of z: "))
        else:
            z = 0 

        h = float(input("Enter the value of h: "))
        if h ==0:
            raise ZeroDivisionError

        result = DerivativeApproximation(f, x, y, z, h)
        print(result)

    # ===============================================================================================================================================================
    if topic == 2:
    # ===============================================================================================================================================================

        dimension = int(input("Enter the dimension between 1 to 3: "))

        if dimension < 1 or dimension > 3:
            print("Please enter a valid dimension between 1 and 3!!! ")
            sys.exit()

        print("\n==== CHOOSE APPROXIMATION METHOD ====")
        print("1. Midpoint Rule")
        print("2. Trapezoidal Rule")
        print("3. Simpson's 1/3 Rule")

        choice = int(input("Enter your choice between 1 to 3: "))

        if choice < 1 or choice > 3:
            print("Please enter a valid choice between 1 and 3!!!")
            sys.exit()

        def  NumericalIntegration(f, a, b, c, d, p, q, m, n, o):

            if dimension == 1 and choice == 1:

                h = (b-a)/m

                total = 0

                for i in range(m):
                    left = a + i*h
                    right = left + h
                    midpoint = (left + right)/2

                    total += f(midpoint)*h
                return total

            if dimension == 1 and choice == 2:

                h = (b-a)/m

                total = 0

                for i in range(1, m):
                    x = a + i*h
                    total += f(x)

                total = h*(0.5*(f(a)) + 0.5*(f(b)) + total)
                return total

            if dimension == 1 and choice == 3:

                h = (b-a)/m

                total = 0
                total1 = 0
                total2 = 0

                for i in range(1, m):
                    x = a + i*h
                    if  i % 2 == 0:
                        total1 += 2*(f(x))

                    if i % 2 != 0:
                        total2 += 4*(f(x))

                total = h*(1/3)*(f(a) + f(b) + total1 + total2)

                return total

            if dimension == 2 and choice == 1:

                g = (b-a)/m
                h = (d-c)/n

                total = 0

                for i in range(m):
                    left_x = a + i*g
                    right_x = left_x + g
                    midpoint_x = (left_x + right_x)/2

                    for j in range(n):
                        left_y = c + j*h
                        right_y = left_y + h
                        midpoint_y = (left_y + right_y)/2

                        total += f(midpoint_x, midpoint_y)

                return total*g*h

            if dimension == 2 and choice == 2:

                g = (b-a)/m
                h = (d-c)/n

                corner = 0
                edge = 0
                interior = 0

                for i in range(m+1):
                    x = a + i*g
                    for j in range(n+1):
                        y = c + j*h
                        if (i == 0 or i == m) and (j == 0 or j == n):
                            corner += f(x, y)*0.25
                        elif i == 0 or i == m or j == 0 or j == n:
                            edge += f(x, y)*0.5
                        else:
                            interior += f(x, y)

                return (corner + edge + interior)*g*h

            if dimension == 2 and choice == 3:

                g = (b-a)/m
                h = (d-c)/n

                total = 0

                for i in range(m+1):
                    x = a + i*g
                    if i == 0 or i == m:
                        wx = 1
                    elif (i % 2 == 1):
                        wx = 4
                    else:
                        wx = 2

                    for j in range(n+1):
                        y = c + j*h
                        if j == 0 or j == n:
                            wy = 1
                        elif (j % 2 == 1):
                            wy = 4
                        else:
                            wy = 2

                        total += (wx)*(wy)*f(x, y)

                return (total)*(g*h)/9

            if dimension == 3 and choice == 1:

                g = (b-a)/m
                h = (d-c)/n
                s = (q-p)/o

                total = 0

                for i in range(m):
                    left_x = a + i*g
                    right_x = left_x + g
                    midpoint_x = (left_x + right_x)/2

                    for j in range(n):
                        left_y = c + j*h
                        right_y = left_y + h
                        midpoint_y = (left_y + right_y)/2

                        for k in range(o):
                            left_z = p + k*s
                            right_z = left_z + s
                            midpoint_z = (left_z + right_z)/2

                            total += f(midpoint_x, midpoint_y, midpoint_z)

                return total*g*h*s

            if dimension == 3 and choice == 2:

                g = (b-a)/m
                h = (d-c)/n
                s = (q-p)/o

                corner = 0
                edge = 0
                face = 0
                interior = 0

                for i in range(m+1):
                    x = a + i*g
                    for j in range(n+1):
                        y = c + j*h
                        for k in range(o+1):
                            z = p + k*s

                            boundary_count = (
                                int(i == 0 or i == m) + 
                                int(j == 0 or j == n) + 
                                int(k == 0 or k == o)
                            )

                            if boundary_count == 3:
                                corner += f(x, y, z)*0.125
                            elif boundary_count == 2:
                                edge += f(x, y, z)*0.25
                            elif boundary_count == 1:
                                face += f(x, y, z)*0.5
                            else:
                                interior += f(x, y, z)

                return (corner + edge + face + interior)*g*h*s

            if dimension == 3 and choice == 3:

                g = (b-a)/m
                h = (d-c)/n
                s = (q-p)/o

                total = 0

                for i in range(m+1):
                    x = a + i*g
                    if i == 0 or i == m:
                        wx = 1
                    elif (i % 2 == 1):
                        wx = 4
                    else:
                        wx = 2

                    for j in range(n+1):
                        y = c + j*h
                        if j == 0 or j == n:
                            wy = 1
                        elif (j % 2 == 1):
                            wy = 4
                        else:
                            wy = 2

                        for k in range(o+1):
                            z = p + k*s 
                            if k == 0 or k == o:
                                wz = 1
                            elif (k % 2 == 1):
                                wz = 4
                            else:
                                wz = 2

                            total += (wx)*(wy)*(wz)*f(x, y, z)

                return (total*g*h*s)/27

        if dimension == 1:
            expression = input("Enter the function f(x): ")

        elif dimension == 2:
            expression = input("Enter the function f(x, y): ")

        else:
            expression = input("Enter the function f(x, y, z): ")

        allowed = {
            "x" : None, 
            "y" : None,
            "z" : None,
            "sin" : math.sin,
            "cos" : math.cos,
            "tan" : math.tan,
            "sqrt" : math.sqrt,
            "asin" : math.asin,
            "acos" : math.acos,
            "atan" : math.atan,
            "log" : math.log,
            "exp" : math.exp,
            "pi" : math.pi,
            "e" : math.e
        }

        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        m = int(input("Enter the value of m: "))

        c = d = p = q = 0.0
        n = o = 1

        if m <= 0:
            print("value of m must be greater than zero!!!")
            sys.exit()

        if dimension >= 2:

            c = float(input("Enter the value of c: "))
            d = float(input("Enter the value of d: "))
            n = int(input("Enter the value of n: "))

            if m <= 0 or n <= 0 :
                print("values of m and n must be greater than zero!!!")
                sys.exit()

        if dimension == 3:

            p = float(input("Enter the value of p: "))
            q = float(input("Enter the value of q: "))

            o = int(input("Enter the value of o: "))

            if m <= 0 or n <= 0 or o<= 0:
                print("values of m, n and o must be greater than zero!!!")
                sys.exit()

        if choice == 3:
            if dimension >= 1 and m % 2 != 0:
                print("Error: Value of m must be even for Simpson's Rule!!!")
                sys.exit()
            if dimension >= 2 and n % 2 != 0:
                print("Error: Value of n must be even for Simpson's Rule!!!")
                sys.exit()
            if dimension == 3 and o % 2 != 0:
                print("Error: Value of o must be even for Simpson's Rule!!!")
                sys.exit()

        if dimension == 1:

            def f(x):
                values = allowed.copy()
                values["x"] = x
                return eval(expression, {"__builtins__": {}}, values)

        elif dimension == 2:

            def f(x, y):
                values = allowed.copy()
                values["x"] = x
                values["y"] = y
                return eval(expression, {"__builtins__": {}}, values)

        else:

            def f(x, y, z):
                values = allowed.copy()
                values["x"] = x
                values["y"] = y
                values["z"] = z  
                return eval(expression, {"__builtins__": {}}, values)

        result = NumericalIntegration(f, a, b, c, d, p, q, m, n, o)

        print(result)

# =================================================================================================================================================================
elif task == 5:
# =================================================================================================================================================================

    dimension = int(input("Enter the dimension: "))

    if dimension < 1 or dimension > 3:
        print("Please enter a valid dimension between 1 to 3!!!")
        sys.exit()

    if dimension == 1:
        expression = input("Enter the function f(x): ")

    elif dimension == 2:
        expression = input("Enter the function f(x, y): ")

    else:
        expression = input("Enter the function f(x, y, z): ")

    allowed = {
        "x" : None, 
        "y" : None, 
        "z" : None,
        "sin" : math.sin,
        "cos" : math.cos,
        "tan" : math.tan,
        "sqrt" : math.sqrt,
        "asin" : math.asin,
        "acos" : math.acos,
        "atan" : math.atan,
        "log" : math.log,
        "exp" : math.exp,
        "pi" : math.pi,
        "e" : math.e
    }


    # ==============================================================================================================================================================
    if dimension == 1:
    # ==============================================================================================================================================================

        def GRADIENT_DESCENT_in_1D(f, x, h, alpha):

            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance = float(input("Enter the value of tolerance: "))
            if tolerance <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            value = f(x)
            converged = False

            print("\n==== GRADIENT DESCENT ====")
            print(f"Initial x : {x} ")
            print(f"Initial f(x) : {value} ")

            for i in range(n):
                gradient = (f(x+h) - f(x-h))/(h*2)

                if abs(gradient) < tolerance:
                    converged = True
                    print("==== Convergence Achieved ====")
                    break

                x_new = x - alpha*gradient

                value_new = f(x_new)

                print("\n ==== ITERATION DETAILS ====")
                print(f"Iteration: {i+1}")
                print(f"Current x: {x} ")
                print(f"Gradient: {gradient}")
                print(f"New x: {x_new}")
                print(f"New f(x): {value_new}")

                x = x_new
                value = value_new

            if not converged:
                final_gradient = (f(x + h) - f(x - h)) / (2 * h)

                if abs(final_gradient) < tolerance:
                    converged = True

            print("\n========== FINAL RESULT ==========")
            print(f"Minimum point (approx): {x}")
            print(f"Minimum value (approx): {value}")
            print(f"Converged: {converged}")

            print("\n")

            if not converged:
                print("Maximum iterations reached or convergence not achieved.")

            return {
            "minimum_point": x,
            "minimum_value": value,
            "converged": converged
            }

        def f(x):
            values = allowed.copy()
            values["x"] = x

            return eval(expression, {"__builtins__": {}}, values)

        x = float(input("Enter the value of x: "))
        h = float(input("Enter the value of h: "))
        if h <= 0:
            print("Value of h must be greater than zero!!!")
            sys.exit()

        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()

        result = GRADIENT_DESCENT_in_1D(f, x, h, alpha)
        print(result)

    # ==============================================================================================================================================================
    elif dimension == 2:
    # ==============================================================================================================================================================

        def GRADIENT_DESCENT_in_2D(f, x, y, h, alpha):

            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance_x = float(input("Enter the value of tolerance of x: "))
            if tolerance_x <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            tolerance_y = float(input("Enter the value of tolerance of y: "))
            if tolerance_y <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            value = f(x, y)
            converged = False

            print("\n==== GRADIENT DESCENT ====")
            print(f"Initial x : {x} ")
            print(f"Initial y : {y} ")
            print(f"Initial f(x, y) : {value} ")

            for i in range(n):
                gradient_x = (f(x+h, y) - f(x-h, y))/(2*h)
                gradient_y = (f(x, y+h) - f(x, y-h))/(2*h)

                if abs(gradient_x) < tolerance_x and abs(gradient_y) < tolerance_y:
                    converged = True
                    print("==== Convergence Achieved ====")
                    break

                x_new = x - alpha*gradient_x
                y_new = y - alpha*gradient_y    

                value_new = f(x_new, y_new)

                print("\n ==== ITERATION DETAILS ====")
                print(f"Iteration: {i+1}")
                print(f"Current x: {x} ")
                print(f"Current y: {y} " )
                print(f"Gradient w.r.t x: {gradient_x}")
                print(f"Gradient w.r.t y: {gradient_y}")
                print(f"New x: {x_new}")
                print(f"New y: {y_new}")
                print(f"New f(x, y): {value_new}")

                x = x_new
                y = y_new
                value = value_new

            if not converged:
                final_gradient_x = (f(x+h, y) - f(x-h, y))/(2*h)
                final_gradient_y = (f(x, y+h) - f(x, y-h))/(2*h)

                if abs(final_gradient_x) < tolerance_x and abs(final_gradient_y) < tolerance_y:
                    converged = True

            print("\n========== FINAL RESULT ==========")
            print(f"Approximate final point: ({x}, {y})")
            print(f"Function value at final point: {value}")
            print(f"Converged: {converged}")

            print("\n")

            if not converged:
                print("Maximum iterations reached or convergence not achieved.")

            return {
            "minimum_point": (x, y),
            "minimum_value": value,
            "converged": converged
            }

        def f(x ,y):
            values = allowed.copy()
            values["x"] = x
            values["y"] = y

            return eval(expression, {"__builtins__": {}}, values)

        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
        h = float(input("Enter the value of h: "))
        if h <= 0:
            print("Value of h must be greater than zero!!!")
            sys.exit()

        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()

        result = GRADIENT_DESCENT_in_2D(f, x, y, h, alpha)
        print(result)

    # ==============================================================================================================================================================
    else: 
    # ==============================================================================================================================================================

        def GRADIENT_DESCENT_in_3D(f, x, y, z, h, alpha):

            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance_x = float(input("Enter the value of tolerance of x: "))
            if tolerance_x <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            tolerance_y = float(input("Enter the value of tolerance of y: "))
            if tolerance_y <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            tolerance_z = float(input("Enter the value of tolerance of z: "))
            if tolerance_z <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            value = f(x, y, z)
            converged = False

            print("\n==== GRADIENT DESCENT ====")
            print(f"Initial x : {x} ")
            print(f"Initial y : {y} ")
            print(f"initial z : {z} ")
            print(f"Initial f(x, y, z) : {value} ")

            for i in range(n):
                gradient_x = (f(x+h, y, z) - f(x-h, y, z))/(2*h)
                gradient_y = (f(x, y+h, z) - f(x, y-h, z))/(2*h)
                gradient_z = (f(x, y, z+h) - f(x, y, z-h))/(2*h)

                if abs(gradient_x) < tolerance_x and abs(gradient_y) < tolerance_y and abs(gradient_z) < tolerance_z:
                    converged = True
                    print("==== Convergence Achieved ====")
                    break

                x_new = x - alpha*gradient_x
                y_new = y - alpha*gradient_y    
                z_new = z - alpha*gradient_z

                value_new = f(x_new, y_new, z_new)

                print("\n ==== ITERATION DETAILS ====")
                print(f"Iteration: {i+1}")
                print(f"Current x: {x} ")
                print(f"Current y: {y} ")
                print(f"Current z: {z} ")
                print(f"Gradient w.r.t x: {gradient_x}")
                print(f"Gradient w.r.t y: {gradient_y}")
                print(f"Gradient w.r.t z: {gradient_z}")
                print(f"New x: {x_new}")
                print(f"New y: {y_new}")
                print(f"New z: {z_new}")
                print(f"New f(x, y, z): {value_new}")

                x = x_new
                y = y_new
                z = z_new
                value = value_new

            if not converged:
                final_gradient_x = (f(x+h, y, z) - f(x-h, y, z))/(2*h)
                final_gradient_y = (f(x, y+h, z) - f(x, y-h, z))/(2*h)
                final_gradient_z = (f(x, y, z+h) - f(x, y, z-h))/(2*h)

                if abs(final_gradient_x) < tolerance_x and abs(final_gradient_y) < tolerance_y and abs(final_gradient_z) < tolerance_z:
                    converged = True

            print("\n========== FINAL RESULT ==========")
            print(f"Approximate final point: ({x}, {y}, {z})")
            print(f"Function value at final point: {value}")
            print(f"Converged: {converged}")

            print("\n")

            if not converged:
                print("Maximum iterations reached or convergence not achieved.")

            return {
            "minimum_point": (x, y, z),
            "minimum_value": value,
            "converged": converged
            }

        def f(x ,y, z):
            values = allowed.copy()
            values["x"] = x
            values["y"] = y
            values["z"] = z

            return eval(expression, {"__builtins__": {}}, values)

        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
        z = float(input("Enter the value of z: "))
        h = float(input("Enter the value of h: "))
        if h <= 0:
            print("Value of h must be greater than zero!!!")
            sys.exit()

        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()

        result = GRADIENT_DESCENT_in_3D(f, x, y, z, h, alpha)
        print(result)

# =================================================================================================================================================================
else:
# =================================================================================================================================================================

    allowed = {
        "x" : None, 
        "y" : None, 
        "z" : None,
        "sin" : np.sin,
        "cos" : np.cos,
        "tan" : np.tan,
        "sqrt" : np.sqrt,
        "arcsin" : np.arcsin,
        "arccos" : np.arccos,
        "arctan" : np.arctan,
        "log" : np.log,
        "exp" : np.exp,
        "pi" : np.pi,
        "e" : np.e
    }

    try:
        dimension = int(input("Enter the dimension: "))
    except Exception:
        print("Please enter a valid numeric value of dimension!!!")
        sys.exit()

    if dimension < 0 or dimension > 3:
        print("Please enter a valid dimensions between 1 and 3!!!")
        sys.exit()

    if dimension == 1:

        def GRADIENT_DESCENT_in_1D(f, x, h, alpha):

            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance = float(input("Enter the value of tolerance: "))
            if tolerance <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            value = f(x)
            converged = False

            x_history = [x]

            print("\n==== GRADIENT DESCENT ====")
            print(f"Initial x : {x} ")
            print(f"Initial f(x) : {value} ")

            for i in range(n):
                try:
                    gradient = (f(x+h) - f(x-h))/(h*2)
                except (ValueError, OverflowError, ZeroDivisionError):
                    print("\n==== GRADIENT DESCENT STOPPED ====")
                    print("Function is not defined around the current x value!!!")
                    break

                if abs(gradient) < tolerance:
                    converged = True
                    print("==== Convergence Achieved ====")
                    break

                x_new = x - alpha*gradient

                if x_new < x_min:
                    x_new = x_min
                elif x_new > x_max:
                    x_new = x_max

                try:
                    value_new = f(x_new)
                except (ValueError, OverflowError, ZeroDivisionError):
                    print("\n==== GRADIENT DESCENT STOPPED ====")
                    print(f"x_new = {x_new} is outside the valid domain of the function.")
                    break

                print("\n ==== ITERATION DETAILS ====")
                print(f"Iteration: {i+1}")
                print(f"Current x: {x} ")
                print(f"Gradient: {gradient}")
                print(f"New x: {x_new}")
                print(f"New f(x): {value_new}")

                x = x_new
                value = value_new

                x_history.append(x)

            if not converged:
                final_gradient = (f(x + h) - f(x - h)) / (2 * h)

                if abs(final_gradient) < tolerance:
                    converged = True

            print("\n========== FINAL RESULT ==========")
            print(f"Minimum point (approx): {x}")
            print(f"Minimum value (approx): {value}")
            print(f"Converged: {converged}")

            print("\n")

            if not converged:
                print("Maximum iterations reached or convergence not achieved.")

            return {
            "minimum_point" : x,
            "minimum_value" : value,
            "converged" : converged, 
            "x_history" : x_history
            }


        # ===============================================================================================================================================================
        # FUNCTION INPUT
        # ===============================================================================================================================================================

        expression = input("Enter the function f(x): ")

        def f(x):
            values = allowed.copy()
            values["x"] = x

            return eval(expression, {"__builtins__": {}}, values)

        # ===============================================================================================================================================================
        # RANGE VALIDATION
        # ===============================================================================================================================================================

        try:
            x_min = float(input("Enter the minimum value for x: "))
            x_max = float(input("Enter the maximum value for x: "))
        except ValueError:
            print("Please enter a valid numeric value for x!!!")
            sys.exit()

        if x_min >= x_max:
            print("x_min must be smaller than x-max!!!")
            sys.exit()

        x = float(input("Enter the value of x: "))

        if x < x_min or x > x_max:
            print("Initial x must lie within the given x range!!!")
            sys.exit()

        h = float(input("Enter the value of h: "))
        if h <= 0:
            print("Value of h must be greater then zero!!!")
            sys.exit()

        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater then zero!!!")
            sys.exit()

        result = GRADIENT_DESCENT_in_1D(f, x, h, alpha)
        print(result)

        x_history = result["x_history"]

        x_values = np.linspace(x_min, x_max, 2000)
        y_values = []

        for value in x_values:
            try:
                y = f(value)
                if not np.isfinite(y):
                    y = np.nan

            except (ValueError, OverflowError, ZeroDivisionError):
                y = np.nan

            y_values.append(y)

        y_values = np.array(y_values, dtype=float)

        difference = np.abs(np.diff(y_values))

        finite_difference = difference[np.isfinite(difference)]

        if len(finite_difference) > 0:
            median_difference = np.median(finite_difference)
        else:
            median_difference = 0

        if median_difference > 0:
            threshold = 100*median_difference

            jump = difference > threshold

            jump_indices = np.where(jump)[0]

            y_values[jump_indices] = np.nan
            y_values[jump_indices + 1] = np.nan

        # ===============================================================================================================================================================
        # 1D FIGURE
        # ===============================================================================================================================================================

        fig, ax = plt.subplots()

        ax.plot(x_values, y_values, label = f"{expression}")

        ax.axhline(0, color = "black")
        ax.axvline(0, color = "black")

        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.set_title(f"GRADIENT DESCENT VISUALIZER OF f(x) = {expression}")

        ax.legend()
        ax.grid(linestyle = "--")

        point = ax.scatter([x_history[0]], [f(x_history[0])], color = "red")

        # ===============================================================================================================================================================
        # ANIMATION
        # ===============================================================================================================================================================

        def update(frame):

            current_x = x_history[frame]
            current_y = f(current_x)

            point.set_offsets([[current_x, current_y]])
            return point, 

        animation = FuncAnimation(fig, update, frames = len(x_history), interval = 300, repeat = False)

        plt.show()

    elif dimension == 2:

        def GRADIENT_DESCENT_in_2D(f, x, y, h, alpha):

            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance_x = float(input("Enter the value of tolerance of x: "))
            if tolerance_x <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            tolerance_y = float(input("Enter the value of tolerance of y: "))
            if tolerance_y <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            value = f(x, y)
            converged = False

            x_history = [x]
            y_history = [y]

            print("\n==== GRADIENT DESCENT ====")
            print(f"Initial x : {x} ")
            print(f"Initial y : {y} ")
            print(f"Initial f(x, y) : {value} ")

            for i in range(n):
                gradient_x = (f(x+h, y) - f(x-h, y))/(2*h)
                gradient_y = (f(x, y+h) - f(x, y-h))/(2*h)

                if abs(gradient_x) < tolerance_x and abs(gradient_y) < tolerance_y:
                    converged = True
                    print("==== Convergence Achieved ====")
                    break

                x_new = x - alpha*gradient_x
                y_new = y - alpha*gradient_y    

                if x_new < x_min:
                    x_new = x_min
                elif x_new > x_max:
                    x_new = x_max

                if y_new < y_min:
                    y_new = y_min
                elif y_new > y_max:
                    y_new = y_max

                try:
                    value_new = f(x_new, y_new)
                except (ValueError, OverflowError, ZeroDivisionError):
                    print("==== GRADIENT DESCENT STOPPED ====")
                    print(f"x_new = {x_new} is outside the valid domain of the function.")
                    sys.exit()

                print("\n ==== ITERATION DETAILS ====")
                print(f"Iteration: {i+1}")
                print(f"Current x: {x} ")
                print(f"Current y: {y} " )
                print(f"Gradient w.r.t x: {gradient_x}")
                print(f"Gradient w.r.t y: {gradient_y}")
                print(f"New x: {x_new}")
                print(f"New y: {y_new}")
                print(f"New f(x, y): {value_new}")

                x = x_new
                y = y_new
                value = value_new

                x_history.append(x)
                y_history.append(y)

            if not converged:
                final_gradient_x = (f(x+h, y) - f(x-h, y))/(2*h)
                final_gradient_y = (f(x, y+h) - f(x, y-h))/(2*h)

                if abs(final_gradient_x) < tolerance_x and abs(final_gradient_y) < tolerance_y:
                    converged = True

            print("\n========== FINAL RESULT ==========")
            print(f"Approximate final point: ({x}, {y})")
            print(f"Function value at final point: {value}")
            print(f"Converged: {converged}")

            print("\n")

            if not converged:
                print("Maximum iterations reached or convergence not achieved.")

            return {
            "minimum_point" : (x, y),
            "minimum_value" : value,
            "converged" : converged, 
            "x_history" : x_history, 
            "y_history" : y_history
            }


        # ===============================================================================================================================================================
        # FUNCTION INPUT
        # ===============================================================================================================================================================

        expression = input("Enter the function f(x, y): ")

        def f(x ,y):
            values = allowed.copy()
            values["x"] = x
            values["y"] = y

            with np.errstate(all="ignore"):
                result =  eval(expression, {"__builtins__": {}}, values)
                if isinstance(result, (int, float)):
                    result = result*np.ones_like(x)

            return result

        # ===============================================================================================================================================================
        # RANGE VALIDATION
        # ===============================================================================================================================================================

        try:
            x_min = float(input("Enter the minimum value for x: "))
            x_max = float(input("Enter the maximum value for x: "))
        except ValueError:
            print("Please enter a valid numeric value for x!!!")
            sys.exit()

        if x_min >= x_max:
            print("x_min must be smaller than x-max!!!")
            sys.exit()

        try:
            y_min = float(input("Enter the minimum value for y: "))
            y_max = float(input("Enter the maximum value for y: "))
        except ValueError:
            print("Please enter a valid numeric value for y!!!")
            sys.exit()

        if y_min >= y_max:
            print("y_min must be smaller than y_max!!!")
            sys.exit()

        x = float(input("Enter the value of x: "))

        if x < x_min or x > x_max:
            print("Initial x must lie within the given x range!!!")
            sys.exit()

        y = float(input("Enter the value of y: "))

        if y < y_min or y > y_max:
            print("Initial y must lie within the given y range!!!")
            sys.exit()

        h = float(input("Enter the value of h: "))
        if h <= 0:
            print("Value of h must be greater than zero!!!")
            sys.exit()

        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()

        result = GRADIENT_DESCENT_in_2D(f, x, y, h, alpha)
        print(result)

        x_history = result["x_history"]
        y_history = result["y_history"]

        x_values = np.linspace(x_min, x_max, 400)
        y_values = np.linspace(y_min, y_max, 400)

        X, Y = np.meshgrid(x_values, y_values)

        try:
            F = f(X, Y)
        except Exception:
            print("Please enter a valid function!!!")
            sys.exit()

        # ===============================================================================================================================================================
        # 2D FIGURE  
        # ===============================================================================================================================================================

        fig, ax = plt.subplots()

        contour = ax.contour(X, Y, F, levels = 20, cmap = "viridis")
        ax.axis("equal")

        ax.axvline(0, color = "black")
        ax.axhline(0, color = "black")

        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.set_title(f"GRADIENT DESCENT VISUALIZER OF f(x, y) = {expression}")

        ax.grid(linestyle = "--")

        point = ax.scatter([x_history[0]], [y_history[0]], color = "red")

        # ===============================================================================================================================================================
        # ANIMATION
        # ===============================================================================================================================================================

        def update(frame):
            current_x = x_history[frame]
            current_y = y_history[frame]

            point.set_offsets([[current_x, current_y]])
            return point, 

        animation = FuncAnimation(fig, update, frames = len(x_history), interval = 100, repeat = False)

        plt.show()

    else: 

        def GRADIENT_DESCENT_in_3D(f, x, y, z, h, alpha):

            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance_x = float(input("Enter the value of tolerance of x: "))
            if tolerance_x <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            tolerance_y = float(input("Enter the value of tolerance of y: "))
            if tolerance_y <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            tolerance_z = float(input("Enter the value of tolerance of z: "))
            if tolerance_z <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()

            value = f(x, y, z)
            converged = False

            x_history = [x]
            y_history = [y]
            z_history = [z]

            print("\n==== GRADIENT DESCENT ====")
            print(f"Initial x : {x} ")
            print(f"Initial y : {y} ")
            print(f"initial z : {z} ")
            print(f"Initial f(x, y, z) : {value} ")

            for i in range(n):
                gradient_x = (f(x+h, y, z) - f(x-h, y, z))/(2*h)
                gradient_y = (f(x, y+h, z) - f(x, y-h, z))/(2*h)
                gradient_z = (f(x, y, z+h) - f(x, y, z-h))/(2*h)

                if abs(gradient_x) < tolerance_x and abs(gradient_y) < tolerance_y and abs(gradient_z) < tolerance_z:
                    converged = True
                    print("==== Convergence Achieved ====")
                    break

                x_new = x - alpha*gradient_x
                y_new = y - alpha*gradient_y    
                z_new = z - alpha*gradient_z

                if x_new < x_min:
                    x_new = x_min
                elif x_new > x_max:
                    x_new = x_max

                if y_new < y_min:
                    y_new = y_min
                elif y_new > y_max:
                    y_new = y_max

                if z_new < z_min:
                    z_new = z_min
                elif z_new > z_max:
                    z_new = z_max

                try:
                    value_new = f(x_new, y_new, z_new)
                except (ValueError, ZeroDivisionError ,OverflowError):
                    print("==== GRADIENT DESCENT STOPPED ====")
                    print(f"New point ({x_new}, {y_new}, {z_new}) is outside the valid domain of the given function!!!")
                    sys.exit()

                print("\n ==== ITERATION DETAILS ====")
                print(f"Iteration: {i+1}")
                print(f"Current x: {x} ")
                print(f"Current y: {y} ")
                print(f"Current z: {z} ")
                print(f"Gradient w.r.t x: {gradient_x}")
                print(f"Gradient w.r.t y: {gradient_y}")
                print(f"Gradient w.r.t z: {gradient_z}")
                print(f"New x: {x_new}")
                print(f"New y: {y_new}")
                print(f"New z: {z_new}")
                print(f"New f(x, y, z): {value_new}")

                x = x_new
                y = y_new
                z = z_new
                value = value_new

                x_history.append(x)
                y_history.append(y)
                z_history.append(z)

            if not converged:
                final_gradient_x = (f(x+h, y, z) - f(x-h, y, z))/(2*h)
                final_gradient_y = (f(x, y+h, z) - f(x, y-h, z))/(2*h)
                final_gradient_z = (f(x, y, z+h) - f(x, y, z-h))/(2*h)

                if abs(final_gradient_x) < tolerance_x and abs(final_gradient_y) < tolerance_y and abs(final_gradient_z) < tolerance_z:
                    converged = True

            print("\n========== FINAL RESULT ==========")
            print(f"Approximate final point: ({x}, {y}, {z})")
            print(f"Function value at final point: {value}")
            print(f"Converged: {converged}")

            print("\n")

            if not converged:
                print("Maximum iterations reached or convergence not achieved.")

            return {
            "minimum_point": (x, y, z),
            "minimum_value": value,
            "x_history" : x_history, 
            "y_history" : y_history,
            "z_history" : z_history,
            "converged": converged
            }


        # ===============================================================================================================================================================
        # FUNCTION INPUT
        # ===============================================================================================================================================================

        expression = input("Enter the function f(x, y, z): ")

        def f(x ,y, z):
            values = allowed.copy()
            values["x"] = x
            values["y"] = y
            values["z"] = z

            with np.errstate(all="ignore"):
                result =  eval(expression, {"__builtins__": {}}, values)
                if isinstance(result, (int, float)):
                    result = result*np.ones_like(x)

            return result

        # ===============================================================================================================================================================
        # RANGE VALIDATION
        # ===============================================================================================================================================================

        try:
            x_min = float(input("Enter the minimum value for x: "))
            x_max = float(input("Enter the maximum value for x: "))
        except ValueError:
            print("Please enter a valid numeric value for x!!!")
            sys.exit()

        if x_min >= x_max:
            print("x_min must be smaller than x-max!!!")
            sys.exit()

        try:
            y_min = float(input("Enter the minimum value for y: "))
            y_max = float(input("Enter the maximum value for y: "))
        except ValueError:
            print("Please enter a valid numeric value for y!!!")
            sys.exit()

        if y_min >= y_max:
            print("y_min must be smaller than y_max!!!")
            sys.exit()

        try:
            z_min = float(input("Enter the minimum value for z: "))
            z_max = float(input("Enter the maximum value for z: "))
        except ValueError:
            print("Please enter a valid numeric value for z!!!")
            sys.exit()

        if z_min >= z_max:
            print("z_min must be smaller than z_max!!!")
            sys.exit()

        x = float(input("Enter the value of x: "))

        if x < x_min or x > x_max:
            print("Initial x must lie within the given x range!!!")
            sys.exit()

        y = float(input("Enter the value of y: "))

        if y < y_min or y > y_max:
            print("Initial y must lie within the given y range!!!")
            sys.exit()

        z = float(input("Enter the value of z: "))
        if z < z_min or z > z_max:
            print("Initial z must lie within the given z range!!!")
            sys.exit()

        h = float(input("Enter the value of h: "))
        if h <= 0:
            print("Value of h must be greater than zero!!!")
            sys.exit()

        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()

        result = GRADIENT_DESCENT_in_3D(f, x, y, z, h, alpha)
        print(result)

        x_history = result["x_history"]
        y_history = result["y_history"]
        z_history = result["z_history"]

        x_values = np.linspace(x_min, x_max, 100)
        y_values = np.linspace(y_min, y_max, 100)
        z_values = np.linspace(z_min, z_max, 100)

        X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing = "ij")

        try:
            F = f(X, Y, Z)
        except Exception:
            print('''
        Invalid Function!!!
        Please check: 
        - Variable names: x, y, z
        - Mathematical syntax
        - Supported functions
        ''')
            sys.exit()

        if np.isscalar(F):
            np.full(X.shape, F, dtype = float)

        F = np.asarray(F, dtype = float)

        # ===============================================================================================================================================================
        # 3D FIGURE
        # ===============================================================================================================================================================

        fig = plt.figure(figsize = (10, 8))
        ax = fig.add_subplot(111, projection = "3d")

        # ===============================================================================================================================================================
        # VALIDITY CHECK
        # ===============================================================================================================================================================

        valid = np.isfinite(F)

        if not np.any(valid):
            print("Function produced no valid values in the given range!!!")
            sys.exit()

        if not np.all(valid):
            print("Function produced undefined values in the given range!!!")
            print("Please choose a different range or modify the given function!!!")
            sys.exit()

        # ===============================================================================================================================================================
        # CHECK WEATHER f(x, y, z) = 0 SURFACE EXISTS 
        # ===============================================================================================================================================================

        if np.min(F) > 0 or np.max(F) < 0:
            print("No real surface is found in the given range!!!")
            sys.exit()

        # ===============================================================================================================================================================
        # MARCHING CUBES 
        # ===============================================================================================================================================================

        try:
            from skimage.measure import marching_cubes
        except ImportError:
            print("scikit-image is required for 3D implicit plotting!!!")
            print("\nInstall it using:")
            print("\npip install scikit-image")
            sys.exit()

        try:
            vertices, faces, normals, values = marching_cubes(F, level = 0)
        except RuntimeError:
            print("No surface found for f(x, y, z) = 0 in the given range!!!")
            sys.exit()

        # ===============================================================================================================================================================
        # CONVERT MARCHING-CUBES INDEX COORDINATES TO ACTUAL x, y, z COORDINATES
        # ===============================================================================================================================================================

        vertices[:, 0] = np.interp(vertices[:, 0], np.arange(len(x_values)), x_values)
        vertices[:, 1] = np.interp(vertices[:, 1], np.arange(len(y_values)), y_values)
        vertices[:, 2] = np.interp(vertices[:, 2], np.arange(len(z_values)), z_values)

        # ===============================================================================================================================================================
        # DRAW 3D SURFACE
        # ===============================================================================================================================================================

        ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], alpha = 0.7)

        ax.set_title(f"GRADIENT DESCENT VISUALIZER OF f(x, y, z) = {expression}", color = "maroon", weight = "bold")

        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.set_zlabel("z-axis")

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_zlim(z_min, z_max)

        ax.view_init(elev = 25, azim = 45)

        point = ax.scatter([x_history[0]], [y_history[0]], [z_history[0]], color = "red", s = 50, depthshade = False)

        plt.grid(linestyle = "--")

        # ===============================================================================================================================================================
        # ANIAMTION
        # ===============================================================================================================================================================

        def update(frame):
            current_x = x_history[frame]
            current_y = y_history[frame]
            current_z = z_history[frame]

            point._offsets3d = ([current_x], [current_y], [current_z])
            return point, 

        animation = FuncAnimation(fig, update, frames = len(x_history), interval = 300, repeat = False)

        plt.show()