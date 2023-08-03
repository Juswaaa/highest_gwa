def find_highest_gwa(filename):
    try:
        students_data = []  

        # Open the file and read each line
        with open(filename, 'r') as file:
            # Process each line in the file
            for line in file:
                student_info = line.strip().split() 
                if len(student_info) >= 2:
                    student_name = ' '.join(student_info[:-1])  
                    gwa = float(student_info[-1])
                    students_data.append((student_name, gwa))  

        if students_data:
            # Find the student with the highest GWA
            highest_gwa_student = min(students_data, key=lambda x: x[1])
            print(f"The student with the highest GWA is: {highest_gwa_student[0]} (GWA: {highest_gwa_student[1]:.2f})")
        else:
            print("No students found in the file or invalid data format.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")

def main():
    filename = "C:/Users/gabep/OneDrive/Desktop/Gabe/2nd Sem/OOP/Assignments/No.4/4.2/students_gwa.txt"  

    find_highest_gwa(filename)

if __name__ == "__main__":
    main()

