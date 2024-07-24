# Program: habitsilvania
# Author : Samuel Stermer and Shelby Fluhr
# Date   : July 24, 2024
# Summary: A habit and todo tracker with a spooky vibe

import django
import sqlite3

class habit:
    def __init__(self, title, description, interval):
        """interval is a ?2-ple? connecting a number and a time length 
        examples: 
            (2, 'day') means twice daily"""
        self.title = title              # title of habit
        self.description = description  # allows extra space for desciption of habit
        self.interval = interval        # how long task remains done for
        self.done = False               # when clicked, is done until interval time passes

    def print_habit(self):
        print()
        print(f"title: {self.title}")
        print(f"description: \n\t{self.description}")
        print(f"interval: {self.interval} days")
        print(f"currently done: {self.done}")
        print()

class todo:
    pass

class goal:
    pass

habit_list = []
todo_list = []
goal_list = []


print("Welcome to habitsilvania!")
while(True):
    print("Would you like to see...")
    print("1. habits")
    print("2. todos")
    print("3. goals")
    print("4. exit program")
    
    # maybe try-except?
    in_str = int(input("please enter integer from 1 - 4: ")) # this throws error if float entered
    
    if type(in_str) != int or in_str < 1 or in_str > 4:
        print("invalid input.")

    match in_str:
        # habits
        case 1:
            print("habits:")
            if(len(habit_list) == 0):
                print("- no habits -")
            else:
                for i in range(len(habit_list)):
                    print(f"{i+1}. {habit_list[i].title} - {habit_list[i].done}")
            
            print()

            while(True):
                print("would you like to...")
                print("1. mark habit as done")
                print("2. habit details")
                print("3. make new habit")
                print("4. delete habit")
                print("5. return to main menu")

                in_habit = int(input("please enter integer from 1 - 4: "))
                # validate

                match in_habit:
                    # mark habit as done
                    case 1:
                        print("habits:")
                        if(len(habit_list) == 0):
                            print("- no habits -")
                            print("no habits to mark as done")
                        else:
                            for i in range(len(habit_list)):
                                print(f"{i+1}. {habit_list[i].title} - {habit_list[i].done}")
                            in_x = int(input("please select habit to mark as done: "))
                            # verify between 1 and i

                            if habit_list[in_x-1].done:
                                print("Task is already completed")
                            else:
                                print("Habit completed (praise user)")
                                habit_list[in_x-1].done = True
                    case 2:
                        print("habits:")
                        if(len(habit_list) == 0):
                            print("- no habits -")
                            print("no habits to mark as done")
                        else:
                            for i in range(len(habit_list)):
                                print(f"{i+1}. {habit_list[i].title} - {habit_list[i].done}")
                            in_x = int(input("please select habit to see details: "))

                            habit_list[in_x-1].print_habit()

                    # make new habit
                    case 3:
                        temp_habit_title = input("please enter habit title:\n")
                        temp_habit_desc = input("please enter habit description:\n")
                        temp_habit_inter = input("please enter habit interval in days:\n")
                        habit_list.append(habit(temp_habit_title, temp_habit_desc, temp_habit_inter))
                    # delete habit
                    case 4:
                        print("habits:")
                        if(len(habit_list) == 0):
                            print("- no habits -")
                            print("no habits to delete")
                        else:
                            for i in range(len(habit_list)):
                                print(f"{i+1}. {habit_list[i].title} - {habit_list[i].done}")
                            in_x = int(input("please select habit to delete: "))
                            habit_list.remove(habit_list[in_x-1])
                        pass
                    # return to main menu
                    case 5:
                        break
                    case _:
                        print("INPUT ERROR")
                        pass
                print()
        # todos
        case 2:
            print("under construction")
            pass

        # goals
        case 3:
            print("under construction")
            pass

        # exit program
        case 4:
            print("under construction")
            pass
        case _:
            print("INPUT ERROR")
            pass
    print()

