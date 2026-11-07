# Advanced Mathematics Toolkit ♾️

A comprehensive, all-in-one Python Command-Line Interface (CLI) application that consolidates six core mathematical and data science modules into a single execution environment.
Built entirely with pure Python and fundamental numerical libraries, this toolkit serves as a robust engine for scientific computing, calculus, and machine learning optimization visualization.

## 🚀 Key Features & Modules

*This application features an interactive main menu that branches into six distinct tools:*

1. **Scientific Calculator:** Evaluates fundamental arithmetic, exponential, logarithmic (natural and base-10), and trigonometric functions (including inverse functions with strict domain validation).

2. **Maths Toolkit (Linear Algebra & Stats):**

   - Evaluates 16 advanced matrix operations (Determinant, Inverse, Rank, Eigenvalues/Eigenvectors).
  
   - Calculates exact roots for $n$-degree polynomials.
  
   - Computes core 1D statistical metrics (Variance, Standard Deviation, Mode, etc.).

3. **Function Plotter:**
   Evaluates mathematical expressions dynamically and plots them across 1D curves, 2D contours, and interactive 3D surfaces using Matplotlib and scikit-image (Marching Cubes).
   Includes protection against invalid domains and asymptotic jumps.

4. **Calculus Toolkit:**
   
   - **Differentiation:** Computes Forward, Backward, and Central approximations across 1D, 2D, and 3D dimensions.
  
   - **Numerical Integration:** Evaluates definite integrals using the Midpoint, Trapezoidal, and Simpson's 1/3 rules for single, double, and triple integrals.

5. **Gradient Descent Optimizer:**

   Dynamically parses 1D, 2D, and 3D mathematical expressions and applies the Gradient Descent algorithm iteratively to find local minima, utilizing user-defined learning rates (alpha) and strict tolerance thresholds.

6. **Gradient Descent Visualizer:**

   Combines the optimizer with Matplotlib's FuncAnimation to visually animate the step-by-step optimization trajectory of a point descending across a 1D line, 2D contour map, or 3D surface mesh.

## 🛠️ Tech Stack

- **Language:** Python 3

- **Core Libraries:** `numpy` (Numerical operations), math (Core functions)

- **Visualization Engine:** `matplotlib` (Plotting and Animations), `scikit-image` (Marching Cubes for 3D implicit surface extraction)

## 💻 How to Run (Installation & Execution)

*Follow these steps to run the toolkit on your local machine:*

1. **Clone the repository:**

   git clone https://github.com/amit39underworld93-bot/ADVANCED_MATHEMATICS_TOOLKIT.git cd ADVANCED_MATHEMATICS_TOOLKIT

2. **Install dependencies**

   *This project requires NumPy, Matplotlib, and scikit-image for calculations and 3D surface rendering.*

   `pip install numpy matplotlib scikit-image`

3. **Execute the engine:**

   `python3 main.py`

## 📸 Usage Overview

*When you launch the application, you will be presented with the primary gateway menu:*

==== TASK ====
1. SCIENTIFIC CALCULATOR
2. MATHS TOOLKIT
3. FUNCTION PLOTTER
4. CALCULUS TOOLKIT
5. GRADIENT DECENT
6. GRADIENT DECENT VISUALIZER
Enter your task between 1 and 6:

*Select the corresponding number to enter the dedicated sub-menu for that specific module.*

## 🛡️ Robust Architecture & Safety Checks

*The engine is built to handle edge cases and prevent catastrophic crashes during invalid mathematical operations:*

- Prevents ZeroDivisionError during numerical differentiation (h=0) and matrix inversion (determinant = 0).

- Manages OverflowError and domain constraint errors during heavy polynomial and logarithmic evaluations.

- Uses NumPy's np.nan and np.isfinite logic to suppress undefined data points from breaking visual plots.
