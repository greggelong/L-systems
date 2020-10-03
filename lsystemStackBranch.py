import turtle
wn = turtle.Screen()
wn.bgcolor("black")
#wn.title("L-System")
greg = turtle.Turtle()
greg.color('green')
greg.speed(0)
greg.penup()
greg.goto(0,-200)
greg.pendown()
greg.left(90)
stack =[]

def generate(sentence,number):
    #print(sentence)
    longSentence =""
    for i in range(number):
        longSentence = generateNext(sentence)
        sentence = longSentence
        #print(i,longSentence)
    return longSentence

def generateNext(sentence):
    nextSentence =""
    for chr in sentence:
        current = chr
        found = False
        for rule in rules:
            if current == rule['a']:
                nextSentence += rule['b']
                found = True
                break
        if found == False:
            nextSentence += current
            
    return nextSentence



def plotturt(instructions, angle):
    global stack
    for chr in instructions:
        if chr == 'F':
            greg.forward(7)
        elif chr == '+':
            greg.right(angle)
        elif chr == '-':
            greg.left(angle)
        elif chr == '[':
            ang=greg.heading()
            pos=[greg.xcor(),greg.ycor()] #pos appended as a list index 0 = x indext 1 = y
            stack.append((ang,pos))
            
            
        elif chr == ']':
            ang,pos = stack.pop()
            greg.setheading(ang)
            greg.penup()
            greg.goto(pos[0],pos[1]) # at index of appended lists are x and y vals
            greg.pendown()
            


axiom = "F"
#rules = [{'a':"F",'b':"F-F+F+FF-F-F+F"}]
rules = [{'a':"F",'b':"FF+[+F-F-F]-[-F+F+F]"}]
print(rules[0]['a'])
mysent = axiom
instr = generate(mysent,4)

print(instr)
plotturt(instr,25)
wn.exitonclick()

