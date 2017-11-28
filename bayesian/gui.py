'''
NAME : Lakshit Bhutani
ID : 2014A&PS0095P
'''
from query import *
from turtle import *

clickq = {}
clickc = {}
bwidth = 0
width = 0
num = 0
vars = []

'''
Event listener for click
'''
def click(x, y):
    if x >= -280 and x <= -150 and y <= -300 and y >= -360:        
            q = []
            c = []
            s = "Query : P("
            flag = False
            for i in range(0, num):
                if clickq[i] == 1:
                    s += (vars[i] + ", ")
                    q.append(vars[i])
                    flag = True
                elif clickq[i] == -1:
                    s += ("~" + vars[i] + ", ")
                    q.append(vars[i].lower())
                    flag = True
            if flag:
                s = s[:-2]
            s += " | "
            flag = False
            for i in range(0, num):
                if clickc[i] == 1:
                    s += (vars[i] + ", ")
                    c.append(vars[i])
                    flag = True
                elif clickc[i] == -1:
                    s += ("~" + vars[i] + ", ")
                    c.append(vars[i].lower())
                    flag = True
            if flag:
                s = s[:-2]
            s += ")"
            goto(-100, -300)
            pen(fillcolor = "white")
            begin_fill()
            forward(550)
            right(90)
            forward(150)
            right(90)
            forward(550)
            right(90)
            forward(150)
            right(90)
            end_fill()
            goto(-100, -330)
            write(s, font = ("Arial", 14, "bold"))
            goto(-100, -380)
            ans = calculate(q, c)
            write("Answer = " + str(ans), font = ("Arial", 14, "bold"))
    
    elif x >= -400 and x <= -350:
        for i in range(0, num):
            if y <= 325 - i*width and y >= 325 - i*width - bwidth:
                if clickq[i] == 0:
                    clickq[i] = 1
                    pen(fillcolor = "yellow")
                    begin_fill()
                    goto(-400, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(-380, 325 - width*i - 2*bwidth/3)
                    pd()
                    write(vars[i], font = ("Arial", 10, "bold"))
                    pu()
                    break
                else:
                    clickq[i] = 0
                    pen(fillcolor = "light green")
                    begin_fill()
                    goto(-400, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(-380, 325 - width*i - 2*bwidth/3)
                    pd()
                    write(vars[i], font = ("Arial", 10, "bold"))
                    pu()
                    break

    elif x >= -200 and x <= -150:
        for i in range(0, num):
            if y <= 325 - i*width and y >= 325 - i*width - bwidth:
                if clickq[i] == 0:
                    clickq[i] = -1
                    pen(fillcolor = "yellow")
                    begin_fill()
                    goto(-200, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(-180, 325 - width*i - 2*bwidth/3)
                    pd()
                    s1 = "~"
                    s2 = vars[i]
                    write("{}".format(s1 + s2), font = ("Arial", 10, "bold"))
                    pu()
                    break
                else:
                    clickq[i] = 0
                    pen(fillcolor = "light green")
                    begin_fill()
                    goto(-200, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(-180, 325 - width*i - 2*bwidth/3)
                    pd()
                    s1 = "~"
                    s2 = vars[i]
                    write("{}".format(s1 + s2), font = ("Arial", 10, "bold"))
                    pu()
                    break


    elif x >= 150 and x <= 200:
        for i in range(0, num):
            if y <= 325 - i*width and y >= 325 - i*width - bwidth:
                if clickc[i] == 0:
                    clickc[i] = 1
                    pen(fillcolor = "yellow")
                    begin_fill()
                    goto(150, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(175, 325 - width*i - 2*bwidth/3)
                    pd()
                    write("{}".format(vars[i]), font = ("Arial", 10, "bold"))
                    pu()
                    break
                else:
                    clickc[i] = 0
                    pen(fillcolor = "light green")
                    begin_fill()
                    goto(150, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(175, 325 - width*i - 2*bwidth/3)
                    pd()
                    write("{}".format(vars[i]), font = ("Arial", 10, "bold"))
                    pu()
                    break


    elif x >= 400 and x <= 450:
        for i in range(0, num):
            if y <= 325 - i*width and y >= 325 - i*width - bwidth:
                if clickc[i] == 0:
                    clickc[i] = -1
                    pen(fillcolor = "yellow")
                    begin_fill()
                    goto(400, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(420, 325 - width*i - 2*bwidth/3)
                    pd()
                    s1 = "~"
                    s2 = vars[i]
                    write("{}".format(s1 + s2), font = ("Arial", 10, "bold"))
                    pu()
                    break
                else:
                    clickc[i] = 0
                    pen(fillcolor = "light green")
                    begin_fill()
                    goto(400, 325 - width*i)
                    pd()
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    forward(50)
                    right(90)
                    forward(bwidth)
                    right(90)
                    pu()
                    end_fill()
                    goto(420, 325 - width*i - 2*bwidth/3)
                    pd()
                    s1 = "~"
                    s2 = vars[i]
                    write("{}".format(s1 + s2), font = ("Arial", 10, "bold"))
                    pu()
                    break

    else:
        pass

'''
Main GUI method
'''
def graphics():
    wn = Screen()
    wn.title("Probabilistic Reasoning")  
    setup (width=1200, height=900, startx=0, starty=0)
    pen(fillcolor="light green", pencolor="black", pensize=2)
    speed(100)
    onscreenclick(click)
    pu()
    goto(-350, 350)
    pd()
    write("Query Variables", font=("Arial", 14, "bold"))
    pu()
    goto(250, 350)
    write("Condition Variable" , font=("Arial", 14, "bold"))
    pu()
    j = 0
    for i in allNodes.keys():
        vars.append(i)
        clickq[j] = 0
        clickc[j] = 0
        j += 1
    vars.sort()
    global num
    num = len(vars)
    global width
    width = 600/num
    global bwidth
    bwidth = 0.8*width
    for i in range(0, num):
        begin_fill()
        goto(-400, 325 - width*i)
        pd()
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        pu()
        end_fill()
        goto(-380, 325 - width*i - 2*bwidth/3)
        pd()
        write(vars[i], font = ("Arial", 10, "bold"))
        pu()

    for i in range(0, num):
        begin_fill()
        goto(-200, 325 - width*i)
        pd()
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        pu()
        end_fill()
        goto(-180, 325 - width*i - 2*bwidth/3)
        pd()
        s1 = "~"
        s2 = vars[i]
        write("{}".format(s1 + s2), font = ("Arial", 10, "bold"))
        pu()

    for i in range(0, num):
        begin_fill()
        goto(150, 325 - width*i)
        pd()
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        pu()
        end_fill()
        goto(175, 325 - width*i - 2*bwidth/3)
        pd()
        write(vars[i], font = ("Arial", 10, "bold"))
        pu()

    for i in range(0, num):
        begin_fill()
        goto(400, 325 - width*i)
        pd()
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        forward(50)
        right(90)
        forward(bwidth)
        right(90)
        pu()
        end_fill()
        goto(420, 325 - width*i - 2*bwidth/3)
        pd()
        s1 = "~"
        s2 = vars[i]
        write("{}".format(s1 + s2), font = ("Arial", 10, "bold"))
        pu()
    
    pen(fillcolor = "orange")
    begin_fill()
    goto(-280, -300)
    pd()
    goto(-150, -300)
    goto(-150, -360)
    goto(-280, -360)
    goto(-280, -300)
    pu()
    end_fill()
    goto(-255, -340)
    pd()
    write("Evaluate", font = ("Arial", 14, "bold"))
    pu()

