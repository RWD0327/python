from tkinter import *
from tkinter import messagebox
import pandas as pd
import os

main_window = Tk()
main_window.title("학생 성적 관리 프로그램")
main_window.resizable(False, False)
def add_student():
    # Create a new window for adding students
    add_window = Toplevel()
    add_window.title("학생 성적 추가")
    add_window.resizable(False, False)

    # Create entry fields for the student's name and grades
    name_label = Label(add_window, text="이름")
    name_label.grid(row=0, column=0)
    name_entry = Entry(add_window)
    name_entry.grid(row=0, column=1)

    korean_label = Label(add_window, text="국어")
    korean_label.grid(row=1, column=0)
    korean_entry = Entry(add_window)
    korean_entry.grid(row=1, column=1)

    math_label = Label(add_window, text="수학")
    math_label.grid(row=2, column=0)
    math_entry = Entry(add_window)
    math_entry.grid(row=2, column=1)

    english_label = Label(add_window, text="영어")
    english_label.grid(row=3, column=0)
    english_entry = Entry(add_window)
    english_entry.grid(row=3, column=1)

    # Function to save the student's grades to the CSV file
    def save_student():
        name = name_entry.get()
        korean = korean_entry.get()
        math = math_entry.get()
        english = english_entry.get()

        if any(value == '' for value in [name, korean, math, english]):
            messagebox.showwarning("경고", "학생 성적을 모두 입력해주세요.")
            return

        student_data = {'이름': [name], '국어': [korean], '수학': [math], '영어': [english]}
        df = pd.DataFrame(student_data)

        # Check if the file exists
        if not os.path.exists('students.csv') or len(pd.read_csv('students.csv')) < 5:
            # If not, create a new file or if less than 5 students, require 5 students
            if len(pd.read_csv('students.csv')) < 5:
                messagebox.showwarning("경고", "학생 5명을 필수로 입력해주세요.")
                return
            df.to_csv('students.csv', index=False)
        else:
            # If the file exists and has more than 5 students, append the new data without the header
            df.to_csv('students.csv', mode='a', header=False, index=False)

        messagebox.showinfo("성적 추가", "학생 성적이 추가되었습니다.")
        add_window.destroy()
        main_window.deiconify()  # Show the main window after adding a student

    # Create a button to save the student's grades
    save_button = Button(add_window, text="저장", command=save_student)
    save_button.grid(row=4, column=0, columnspan=2)

    back_button = Button(add_window, text="뒤로가기", command=add_window.destroy)
    back_button.grid(row=5, column=0, columnspan=2)

    add_window.mainloop()

def delete_student():
    def delete():
        nonlocal name_entry, delete_window

        name = name_entry.get()

        if name == '':
            messagebox.showwarning("경고", "학생 이름을 입력해주세요.")
            return

        if not os.path.exists('students.csv'):
            messagebox.showwarning("경고", "학생 데이터가 없습니다.")
            return

        df = pd.read_csv('students.csv')

        if name not in df['이름'].values:
            messagebox.showwarning("경고", "해당 학생이 존재하지 않습니다.")
            return

        df = df[df['이름'] != name]
        df.to_csv('students.csv', index=False)

        messagebox.showinfo("성적 삭제", "학생 성적이 삭제되었습니다.")
        delete_window.destroy()  # Close the delete_window

    main_window.withdraw()  # Hide the main window before deleting a student

    # Create a new window for deleting students
    delete_window = Toplevel()
    delete_window.title("학생 성적 삭제")
    delete_window.resizable(False, False)

    # Create entry field for the student's name
    name_label = Label(delete_window, text="이름")
    name_label.grid(row=0, column=0)
    name_entry = Entry(delete_window)
    name_entry.grid(row=0, column=1)

    # Create a button to delete the student's grades
    delete_button = Button(delete_window, text="삭제", command=delete)
    delete_button.grid(row=1, column=0, columnspan=2)

    delete_window.mainloop()


def add_student():
    # Create a new window for adding students
    add_window = Toplevel()
    add_window.title("학생 성적 추가")
    add_window.resizable(False, False)

    # Create entry fields for the student's name and grades
    name_label = Label(add_window, text="이름")
    name_label.grid(row=0, column=0)
    name_entry = Entry(add_window)
    name_entry.grid(row=0, column=1)

    korean_label = Label(add_window, text="국어")
    korean_label.grid(row=1, column=0)
    korean_entry = Entry(add_window)
    korean_entry.grid(row=1, column=1)

    math_label = Label(add_window, text="수학")
    math_label.grid(row=2, column=0)
    math_entry = Entry(add_window)
    math_entry.grid(row=2, column=1)

    english_label = Label(add_window, text="영어")
    english_label.grid(row=3, column=0)
    english_entry = Entry(add_window)
    english_entry.grid(row=3, column=1)

    # Function to save the student's grades to the CSV file
    def save_student():
        name = name_entry.get()
        korean = korean_entry.get()
        math = math_entry.get()
        english = english_entry.get()

        if any(value == '' for value in [name, korean, math, english]):
            messagebox.showwarning("경고", "학생 성적을 모두 입력해주세요.")
            return

        student_data = {'이름': [name], '국어': [korean], '수학': [math], '영어': [english]}
        df = pd.DataFrame(student_data)

        # Check if the file exists
        if not os.path.exists('students.csv'):
            # If not, create a new file
            df.to_csv('students.csv', index=False)
        else:
            # If the file exists, append the new data without the header
            df.to_csv('students.csv', mode='a', header=False, index=False)

        messagebox.showinfo("성적 추가", "학생 성적이 추가되었습니다.")
        add_window.destroy()
        enter_window.deiconify()

    # Create a button to save the student's grades
    save_button = Button(add_window, text="저장", command=save_student)
    save_button.grid(row=4, column=0, columnspan=2)

    back_button = Button(add_window, text="뒤로가기", command=add_window.destroy)
    back_button.grid(row=5, column=0, columnspan=2)

    add_window.mainloop()
    def save_student():
        name = name_entry.get()
        korean = korean_entry.get()
        math = math_entry.get()
        english = english_entry.get()

        if any(value == '' for value in [name, korean, math, english]):
            messagebox.showwarning("경고", "학생 성적을 모두 입력해주세요.")
            return

        student_data = {'이름': [name], '국어': [korean], '수학': [math], '영어': [english]}
        df = pd.DataFrame(student_data)

        # Check if the file exists
        if not os.path.exists('students.csv') or len(pd.read_csv('students.csv')) < 5:
            # If not, create a new file or if less than 5 students, require 5 students
            if len(pd.read_csv('students.csv')) < 5:
                messagebox.showwarning("경고", "학생 5명을 필수로 입력해주세요.")
                return
            df.to_csv('students.csv', index=False)
        else:
            # If the file exists and has more than 5 students, append the new data without the header
            df.to_csv('students.csv', mode='a', header=False, index=False)

        messagebox.showinfo("성적 추가", "학생 성적이 추가되었습니다.")
        add_window.destroy()
        enter_window.deiconify()

    # Create a button to save the student's grades
    save_button = Button(add_window, text="저장", command=save_student)
    save_button.grid(row=4, column=0, columnspan=2)

    back_button = Button(add_window, text="뒤로가기", command=add_window.destroy)
    back_button.grid(row=5, column=0, columnspan=2)

    add_window.mainloop()

def delete_student():
    def delete():
        name = name_entry.get()

        if name == '':
            messagebox.showwarning("경고", "학생 이름을 입력해주세요.")
            return

        if not os.path.exists('students.csv'):
            messagebox.showwarning("경고", "학생 데이터가 없습니다.")
            return

        df = pd.read_csv('students.csv')

        if name not in df['이름'].values:
            messagebox.showwarning("경고", "해당 학생이 존재하지 않습니다.")
            return

        df = df[df['이름'] != name]
        df.to_csv('students.csv', index=False)

        messagebox.showinfo("성적 삭제", "학생 성적이 삭제되었습니다.")
        delete_window.destroy()  # Close the delete_window

    enter_window.withdraw()
    delete_window = Toplevel()
    delete_window.title("학생 성적 삭제")
    delete_window.resizable(False, False)

    name_label = Label(delete_window, text="이름:", font=("맑은 고딕", 15))
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(delete_window, font=("맑은 고딕", 15))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button = Button(delete_window, text="삭제", font=("맑은 고딕", 15), command=delete)
    delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def search_student():
    def search():
        name = name_entry.get()

        if name == '':
            messagebox.showwarning("경고", "학생 이름을 입력해주세요.")
            return

        if not os.path.exists('students.csv'):
            messagebox.showwarning("경고", "학생 데이터가 없습니다.")
            return

        df = pd.read_csv('students.csv')

        if name not in df['이름'].values:
            messagebox.showwarning("경고", "해당 학생이 존재하지 않습니다.")
            return

        student = df[df['이름'] == name].iloc[0]
        grades = {'국어': student['국어'], '수학': student['수학'], '영어': student['영어']}
        grades = {subject: grade_to_letter(grade) for subject, grade in grades.items()}

        messagebox.showinfo("성적 검색", f"{name} 학생의 성적은 {grades}입니다.")
        search_window.destroy()  # Close the search_window

    def grade_to_letter(grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        else:
            return 'F'

    enter_window.withdraw()
    search_window = Toplevel()
    search_window.title("학생 성적 검색")
    search_window.resizable(False, False)

    name_label = Label(search_window, text="이름:", font=("맑은 고딕", 15))
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(search_window, font=("맑은 고딕", 15))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button = Button(search_window, text="검색", font=("맑은 고딕", 15), command=search)
    search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
def update_student():
    # Create a new window
    update_window = Tk()
    update_window.title("학생 성적 수정")
    update_window.resizable(False, False)

    # Create entry fields for the student's name and new grades
    name_label = Label(update_window, text="이름")
    name_label.grid(row=0, column=0)
    name_entry = Entry(update_window)
    name_entry.grid(row=0, column=1)

    korean_label = Label(update_window, text="국어")
    korean_label.grid(row=1, column=0)
    korean_entry = Entry(update_window)
    korean_entry.grid(row=1, column=1)

    math_label = Label(update_window, text="수학")
    math_label.grid(row=2, column=0)
    math_entry = Entry(update_window)
    math_entry.grid(row=2, column=1)

    english_label = Label(update_window, text="영어")
    english_label.grid(row=3, column=0)
    english_entry = Entry(update_window)
    english_entry.grid(row=3, column=1)

    # Function to update the student's grades in the CSV file
    def save_updated_student():
        name = name_entry.get()
        korean = korean_entry.get()
        math = math_entry.get()
        english = english_entry.get()

        df = pd.read_csv('students.csv')
        df.loc[df['이름'] == name, '국어'] = korean
        df.loc[df['이름'] == name, '수학'] = math
        df.loc[df['이름'] == name, '영어'] = english
        df.to_csv('students.csv', index=False)

        messagebox.showinfo("성적 수정", "학생 성적이 수정되었습니다.")
        update_window.destroy()

    # Create a button to save the updated grades
    save_button = Button(update_window, text="저장", command=save_updated_student)
    save_button.grid(row=4, column=0, columnspan=2)

    update_window.mainloop()    

def print_grades():
    if not os.path.exists('students.csv'):
        messagebox.showwarning("경고", "학생 데이터가 없습니다.")
        return

    df = pd.read_csv('students.csv')

    max_grades = df[['국어', '수학', '영어']].max()
    student_averages = df[['국어', '수학', '영어']].mean(axis=1)
    standard_deviation = df[['국어', '수학', '영어']].std().mean()

    messagebox.showinfo("성적 출력", f"각 과목의 최고점: {max_grades.to_dict()}\n"
                                    f"각 학생의 평균: {student_averages.to_dict()}\n"
                                    f"전체 학생의 표준편차: {standard_deviation}")


def create_button(window, text, font, command, row, column):
    button = Button(window, text=text, font=font, command=command)
    button.grid(row=row, column=column, padx=10, pady=10)
    return button

def enter():
    global enter_window
    main_window.withdraw()

    enter_window = Tk()
    enter_window.title("학생 성적 관리 프로그램")
    enter_window.resizable(False, False)

    # 학생 성적 추가 버튼
    add_button = create_button(enter_window, "학생 성적 추가", ("맑은 고딕", 15), add_student, 0, 0)

    # 학생 성적 검색 버튼
    search_button = create_button(enter_window, "학생 성적 검색", ("맑은 고딕", 15), search_student, 1, 0)

    # 학생 성적 삭제 버튼
    delete_button = create_button(enter_window, "학생 성적 삭제", ("맑은 고딕", 15), delete_student, 2, 0)

    # 학생 성적 출력 버튼
    print_button = create_button(enter_window, "학생 성적 출력", ("맑은 고딕", 15), print_grades, 3, 0)

    enter_window.mainloop()

title = Label(main_window, text="학생 성적 관리 프로그램", font=("맑은 고딕", 20))
title.grid()

Enter = Button(main_window, text="접속하기", font=("맑은 고딕", 15), command=enter)
Enter.grid()

Exit = Button(main_window, text="종료하기", font=("맑은 고딕", 15), command=main_window.quit)
Exit.grid()

main_window.mainloop()