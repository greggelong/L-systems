# L-systems
L-systems in p5.js and processing3 

![lsys2.png](lsys2.png)

![lsys2b.png](lsys2b.png)

![lsys3.png](lsys3.png)


Revisiting L-Systems. Previously I have used #danielshiffman #thecodingtrain and #natureofcode algorithms. But this version uses a different sentence expansion algorithm.
 The L-System rule is just in a simple if else clause, or in switch statement.
 If sentences contains an "F" (non terminal) make the substitution "FF+[+F-F-F]-[-F+F+F]".
 If sentence contains a terminal character +-[] then just append it
 I think this makes the substitution more explicit and easier to understand.
 More complex rules can be captured in a switch statement.

   I have refactored the turtle to use a switch statement
   I have added a generation count so it will reset before it breaks the browser

Another benefit of this if else or switch() sentence expansion algorithm is that you can use it directly in Processing3. Black and white pictures.
Processing3 doesn't have the object literal (comma separated name-value pairs in curly braces).
So you can end up making a class to encapsulate that data.  And the code gets you farther away from the simple substitution. #creativecoding #lsystem


