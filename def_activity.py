# A 'def' function in Python is used to define a reusable block of code.
# It takes inputs from from users, then performs calculations or operations, 
# and returns or outputs results without repeating code.

def calculate_student_grade(subject_scores):
    """
    Calculates the average score from a list of numbers
    and determines the final status using if-else >_<.
    """
    total = sum(subject_scores)
    average = total / len(subject_scores)
    
    # Determine the grade based on average
    if average >= 90:
        status = "Excellent!"
    elif average >= 75:
        status = "Passed"
    else:
        status = "You Need Improvement! Ugh Study Harder!(Failed)"
        
    return average, status


# Main program 
print("=== Student Grade Evaluator ===")

scores = []
num_subjects = 3

# Collect scores  from user input
for i in range(1, num_subjects + 1):
    score = float(input(f"Enter score for Subject {i} (0-100): "))
    scores.append(score)

# Calling/invoking the def function with the collected scores
final_avg, performance = calculate_student_grade(scores)

# Output results formatted nicely kase ofc maarte tayo and dapat maganda presentation 
print("\n--- Evaluation Summary ---")
print(f"Scores Entered : {scores}")
print(f"Final Average  : {final_avg:.2f}%")
print(f"Academic Status: {performance}")
