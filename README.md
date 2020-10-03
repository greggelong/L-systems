# L-systems
L-systems in p5.js and processing3 

![lsys2.png](lsys2.png)

[live: if else sentence expansion](https://editor.p5js.org/greggelong/full/JCBNfEyMW)

![lsys2b.png](lsys2b.png)

[live: switch statement sentence expansion, branching](https://editor.p5js.org/greggelong/full/BOO0xB5yp)

![lsys3.png](lsys3.png)

[live: switch statement sentence expansion, dragon](https://editor.p5js.org/greggelong/full/KbinrqOT-)

![lsys4.png](lsys4.png)

[live: switch statement sentence expansion, random rules](https://editor.p5js.org/greggelong/full/1JsOaNZm6)




Revisiting L-Systems. Previously I have used #danielshiffman #thecodingtrain and #natureofcode algorithms. But this version uses a different sentence expansion algorithm.

 The L-System rule is just in a simple if else clause, or switch statement.
 
 If sentences contains an "F" (non terminal) make the substitution "FF+[+F-F-F]-[-F+F+F]".
 
 If sentence contains a terminal character +-[] then just append it
 
 I think this makes the substitution more explicit and easier to understand.
 More complex rules can be captured in a switch statement.

   I have refactored the turtle to use a switch statement
   I have added a generation count so it will reset before it breaks the browser

Another benefit of this if else or switch() sentence expansion algorithm is that you can use it directly in Processing3. Black and white pictures.
Processing3 doesn't have the object literal (comma separated name-value pairs in curly braces).
So you can end up making a class to encapsulate that data.  And the code gets you farther away from the simple substitution. #creativecoding #lsystem


There is also an L-system in Python. It is drawn with Turtle and is very slow.  I also needed to create a stack to push and pop the turtles heading and location as python turtle does not have a push() and pop() like processing and P5.js

[see python code live](https://trinket.io/python/eeedd06121)

L-Systems are a grammar. See my other code on [Context Free Grammar](https://greggelong.github.io/context-free-grammar/)

[home](https://greggelong.github.io)



