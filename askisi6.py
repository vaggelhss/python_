#ASKISI 6

import random

w = int(input("Enter width, the number must be greater than 1\n"))
h = int(input("Enter height, the number must be greater than 1\n"))
num = int(input("Enter number of bombs\n"))

if num > w * h:
    num = w * h

start = w
end = h

Matrix = [[0 for x in range(w)] for y in range(h)]

counter = 0

while counter < num:
    curr_w = random.randint(0, w-1)
    curr_h = random.randint(0, h-1)
    if(Matrix[curr_h][curr_w] == 0):
        Matrix[curr_h][curr_w] = 9
        counter += 1

bombs = 0

if Matrix[0][0] != 9:
    if Matrix[0][1] == 9:
        bombs += 1
    if Matrix[1][1] == 9:
        bombs += 1
    if Matrix[1][0] == 9:
        bombs += 1
    Matrix[0][0] = bombs
    bombs = 0

if Matrix[h-1][0] != 9:
    if Matrix[h-2][0] == 9:
        bombs += 1
    if Matrix[h-2][1] == 9:
        bombs += 1
    if Matrix[h-1][1] == 9:
        bombs += 1
    Matrix[h-1][0] = bombs
    bombs = 0

if Matrix[0][w-1] != 9:
    if Matrix[0][w-2] == 9:
        bombs += 1
    if Matrix[1][w-2] == 9:
        bombs += 1
    if Matrix[1][w-1] == 9:
        bombs += 1
    Matrix[0][w-1] = bombs
    bombs = 0

if Matrix[h-1][w-1] != 9:
    if Matrix[h-1][w-2] == 9:
        bombs += 1
    if Matrix[h-2][w-2] == 9:
        bombs += 1
    if Matrix[h-2][w-1] == 9:
        bombs += 1
    Matrix[h-1][w-1] = bombs
    bombs = 0

if w > 2:
    for i in range(1, w-1):
        if Matrix[0][i] != 9:
            if Matrix[1][i-1] == 9:
                bombs += 1
            if Matrix[1][i] == 9:
                bombs += 1
            if Matrix[1][i+1] == 9:
                bombs += 1
            if Matrix[0][i-1] == 9:
                bombs += 1
            if Matrix[0][i+1] == 9:
                bombs += 1
            Matrix[0][i] = bombs
            bombs = 0
        if Matrix[h-1][i] != 9:
            if Matrix[h-2][i-1] == 9:
                bombs += 1
            if Matrix[h-2][i] == 9:
                bombs += 1
            if Matrix[h-2][i+1] == 9:
                bombs += 1
            if Matrix[h-1][i-1] == 9:
                bombs += 1
            if Matrix[h-1][i+1] == 9:
                bombs += 1
            Matrix[h-1][i] = bombs
            bombs = 0

if h > 2:
    for i in range(1, h-1):
        if Matrix[i][0] != 9:
            if Matrix[i][1] == 9:
                bombs += 1
            if Matrix[i-1][1] == 9:
                bombs += 1
            if Matrix[i+1][1] == 9:
                bombs += 1
            if Matrix[i+1][0] == 9:
                bombs += 1
            if Matrix[i-1][0] == 9:
                bombs += 1
            Matrix[i][0] = bombs
            bombs = 0
        if Matrix[i][w-1] != 9:
            if Matrix[i+1][w-2] == 9:
                bombs += 1
            if Matrix[i-1][w-2] == 9:
                bombs += 1
            if Matrix[i][w-2] == 9:
                bombs += 1
            if Matrix[i+1][w-1] == 9:
                bombs += 1
            if Matrix[i-1][w-1] == 9:
                bombs += 1
            Matrix[i][w-1] = bombs
            bombs = 0

if h > 2 and w > 2:
    for i in range(1, h-1):
        for j in range(1, w-1):
            if Matrix[i][j] != 9:
                if Matrix[i+1][j] == 9:
                    bombs += 1
                if Matrix[i+1][j-1] == 9:
                    bombs += 1
                if Matrix[i+1][j+1] == 9:
                    bombs += 1
                if Matrix[i][j+1] == 9:
                    bombs += 1
                if Matrix[i][j-1] == 9:
                    bombs += 1
                if Matrix[i-1][j] == 9:
                    bombs += 1
                if Matrix[i-1][j+1] == 9:
                    bombs += 1
                if Matrix[i-1][j-1] == 9:
                    bombs += 1
                Matrix[i][j] = bombs
                bombs = 0

for i in Matrix:
    print(i)
