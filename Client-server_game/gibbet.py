import random
import turtle
import sys
import time


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)


def draw_head(x, y, r):
    gotoxy(x, y)
    turtle.circle(r)



def lastik(x, y):
    gotoxy(x, y)
    turtle.color("white")
    turtle.begin_fill()
    turtle.begin_poly()
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.end_poly()
    turtle.end_fill()


funcs = [draw_line, draw_line, draw_line, draw_line, draw_head, draw_line, draw_line, draw_line, draw_line, draw_line, ]


def draw_gibbet(step, coord):
    turtle.color('black')
    funcs[step](*coord_list[step])


x = random.randint(1, 100)

# print(x)

turtle.speed(0)

coord_list = []
coord = open('coords.txt')

for line in coord:
    line = line.strip().split(',')
    nums = []
    for n in line:
        nums.append(int(n))

    coord_list.append(nums)

print(coord_list)

# time.sleep() #время таймаута в секундах

# from tkinter import SimpleDialog
# SimpleDialog.textinput()

answer = turtle.textinput("Поиграем?", "y/n")

if answer == 'n':
    sys.exit()

hints = False
answer2 = turtle.textinput("Играем с подсказками или по-взрослому =) ?", "y/n")
if answer2 == 'y':
    hints = True

try_count = 0

while True:
    number = turtle.numinput("Угадайте число", "Число", 0, 0, 100)

    if number == x:
        lastik(-150, 100)
        turtle.color("green")
        gotoxy(-150, 200)
        turtle.write("Вы выиграли!!!", font=("Arial", 28, "normal"))
        break

    else:
        # lastik(-150, 200)
        turtle.color("red")
        gotoxy(-150, 200)
        turtle.write("Неверно!", font=("Arial", 28, "normal"))

        if hints:
            gotoxy(100, 100 - try_count * 15)
            turtle.color("blue")
            if x < number:
                turtle.write(str(number) + " Загаданное число меньше", font=("Arial", 10, "normal"))
            else:
                turtle.write(str(number) + " Загаданное число больше", font=("Arial", 10, "normal"))

        draw_gibbet(try_count, coord_list)
        try_count += 1

        if try_count == 10:
            draw_line(*coord_list[9])
            # lastik()
            gotoxy(-150, 200)
            turtle.write("Вы проиграли!", font=("Arial", 28, "normal"))
            break

input("Press any key to close turtle: ")
