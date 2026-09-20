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

# Ask user how many subjects they have, tapos bagsak ka pala djk
total_subjects = int(input("How many subjects do you have? "))

# Loop for as many subjects as specified para one by one ma calculate yung grades (complicated neto jusmiyo)
for i in range(1, total_subjects + 1):
    score = float(input(f"Enter score for Subject {i} (0-100): "))
    scores.append(score)

# Calling/invoking the def function with the collected list of scores
final_avg, performance = calculate_student_grade(scores)

# Output results formatted nicely ofc kase maarte tayo :p
print("\n--- Evaluation Summary ---")
print(f"Total Subjects : {len(scores)}")
print(f"Scores Entered : {scores}")
print(f"Final Average  : {final_avg:.2f}%")
print(f"Academic Status: {performance}")
