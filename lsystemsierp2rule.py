import turtle
wn = turtle.Screen()
wn.bgcolor("black")
#wn.tracer(False) # turns animation off
#wn.title("L-System")
greg = turtle.Turtle()
greg.color('white')
greg.hideturtle() # need to do this with tracer false
greg.speed('fastest')
greg.penup()
greg.width(3)
greg.goto(125,-300)
greg.pendown()
greg.left(90)
stack =[]

def expand(currgen):
	global rule
	nextgen =""
	for char in currgen:
		if char == "F":
			nextgen+=frule
		elif char == "G":
			nextgen+=grule
		else:
			nextgen+=char
	return nextgen
	
def cntChr(lst, str):
	#list of characters
	count = 0
	for i in str:
		if i in lst:
			count =count +1
			
	return count


def plotturt(instructions, angle):
    global stack
    for chr in instructions:
        if chr == 'F' or chr == 'G': #prints f and g
            greg.forward(17)
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
            


#axiom="F"
axiom = "F-G-G"
frule="F-G+F+G-F"
grule="GG"
dna=axiom
for g in range(1,6):
	dna = expand(dna)
	print('this is gen', g, 'dna len', len(dna), 'dna', dna)
	print("number of Fs",cntChr(["F"],dna))
	print("number of terminal chr",cntChr(["+","-","[","]"],dna))
	print("total number of chars:",len(dna))


plotturt(dna,120)
wn.exitonclick()
