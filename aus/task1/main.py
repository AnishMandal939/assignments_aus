def calculate_average_marks(subject_code):
    file_name = subject_code + ".txt"
    output_file = subject_code + "_ave.txt"
    failed_file = subject_code + "_failed.txt"
    total_students = 0
    failed_students = 0
    total_assignment1_marks = 0
    total_assignment2_marks = 0
    total_final_exam_marks = 0

    with open(file_name, 'r') as file:
        lines = file.readlines()
        total_students = len(lines) - 1  # Exclude the header line
        for line in lines[1:]:
            parts = line.split()
            assignment1_mark = float(parts[0])
            assignment2_mark = float(parts[1])
            final_exam_mark = float(parts[2])
            total_assignment1_marks += assignment1_mark
            total_assignment2_marks += assignment2_mark
            total_final_exam_marks += final_exam_mark
            if (assignment1_mark < 50 or assignment2_mark < 50 or final_exam_mark < 50):
                failed_students += 1

    with open(output_file, 'w') as file:
        file.write("Average marks for each subject:\n")
        file.write("Assignment 1: " + str(total_assignment1_marks / total_students) + "\n")
        file.write("Assignment 2: " + str(total_assignment2_marks / total_students) + "\n")
        file.write("Final Exam: " + str(total_final_exam_marks / total_students) + "\n")

    with open(failed_file, 'w') as file:
        file.write("Number of failed students: " + str(failed_students))

# Example usage:
calculate_average_marks("ICT701")
calculate_average_marks("ICT711")