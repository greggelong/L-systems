""" non propagative L-system:
     meaning it replaces characters 1 for 1, so the sentence does not grow
    context sensitive:
     meaning it makes replacements by looking at neighbors as well as the char itself
     
     This happens to encode a one dimensional Wolfram cellular automaton
     the rule here is Wolfram 90
    
    There is an edge problem in these kind of cellular automata when you are looking at the neighbors
     of the first and last index 
    
     I am using modulo to solve the problem in python
    >>>(19+1)%20
    0
    
    the last index of a string of 20 chars is 19 so using modulo you can get 0
    
    >>>(0-1)%20
    19
    the first index of a sting of 20 chars - 1 will then = the last
    
    !!! but beware the JavaScript modulo bug !!!!!!
    !!!                                         !!!!
    
    >>(19+1)%20
     0

    >>(0-1)%20

     -1
     
     gives a negative result
     
     so here is the fix for javaScript negitive modulo
     from https://medium.com/@thomaspoignant/how-to-get-always-a-positive-modulo-remainder-9ac965361ff4
     
     ((((i-1)%20)+20)%20)  /// yikes!!!!
     
     where you have a string of 20 chars and yikes!!!
    
    or just for the edge case when you are moving by negative one you can do it this way
    
    (0-1)%20+20
    (i-1)%20+20
    
     """

def replaceIt(currGen):
    nextGen = ""
    v=""
    for i in range(len(currGen)):
        threeText = currGen[(i-1)%len(currGen)] + currGen[i] + currGen[(i+1)%len(currGen)]
        if threeText == "AAA":              
            nextGen = nextGen + "B"
            v=v+" "
            
        elif threeText == "AAB":
            nextGen = nextGen + "A"
            v=v+"#"
            
        elif threeText == "ABA":
            nextGen = nextGen + "B"
            v=v+" "
            
        elif threeText == "ABB":
            nextGen = nextGen + "A"
            v=v+"#"
            
        elif threeText == "BAA":
            nextGen = nextGen + "A"
            v=v+"#"
            
        elif threeText == "BAB":
            nextGen = nextGen + "B"
            v=v+" "
            
        elif threeText == "BBA":
            nextGen = nextGen + "A"
            v=v+"#"
            
        elif threeText == "BBB":
            nextGen = nextGen + "B"
            v=v+" "
            
    return nextGen, v
        
        
        
axiom = "BBBBBBBBBBABBBBBBBBBB"
gen = axiom
print(0,'\t', gen, "          #          ")
for i in range(30):
    
    gen, v= replaceIt(gen)
    print(i+1,'\t', gen, v)
    
            
    