/* 

This version uses a different sentence expansion algorithm.
 The L-System rule in a simple switch statement.
 
 case "F"
 If sentences contains an "F" (non terminal) make the substitution "FF+[+F-F-F]-[-F+F+F]".
 
 defualt;
 If sentence contains a terminal character +-[] then just append it 
 I think this makes the substitution more explicit and easier to understand.
 More complex rules can be captured in a switch statement.

   I have refactored the turtle to use a switch statement
   I have added a generation count so it will reset before it breaks the browser

Another benefit of this if then else or switch() sentence expansion algorithm is that you can use it directly in Processing3.
Processing3 doesn't have the object literal (comma separated name-value pairs in curly braces). 
So you can end up making a class to encapsulate that data.  And the code gets you farther away from the simple substitution.
you can see the processing code in the repository.  
  
*/
let angle = 20;
let n =7;
let gen = 0;
//let axiom = "F";
let axiom = "X";
let sentence = axiom;
let mybutton;
let len = 100
let cvs;
let output;

function setup() {
  cvs = select('#canvasHolder');
  cvs = createCanvas(400, 400);
  //cnvs.background(93, 0, 172);
  cvs.parent('canvasHolder'); // sticks the canvas into this html div set in index
  background(0);

  angleMode(DEGREES);
  stroke(0, 255, 0, 100);
  //noCanvas();
  mybutton = select("#button");
  mybutton.mousePressed(generate);
  output = select('#output');
  output.html(axiom);
  //translate(width/2,height);
  turtle();

}


function generate() {
  console.log(gen);
  if (gen < n) { // only 5 generations
    len *= 0.5;
    gen++
    //len *=0.618;
    let nextsentence = "";
    for (let i = 0; i < sentence.length; i++) {
      let current = sentence.charAt(i); // get char in sentence
      // simple rule with switch statement
      switch (current) {
        // rule 1
        case "F":
          nextsentence += "FF";   // with X rules
         // nextsentence += "FF+[+F-F-F]-[-F+F+F]"; // l-sys c
          //nextsentence += "F[+F]F[-F][F]";  // L-sys b
          break;
        
        case "X":
          nextsentence += "F[+X][-X]FX" // L-SYS e with axiomm x
          //nextsentence += "FF+[+F-F-F]-[-F+F+F]";
          //nextsentence += "F[+F]F[-F][F]";
          break;

        default:
          nextsentence += current;


      }


      /* if (current === 'F') { // if 'F' make substitution
        nextsentence += "FF+[+F-F-F]-[-F+F+F]";
      } else { // else just append the terminal character +-[]
        nextsentence += current;
      }*/
    }

    sentence = nextsentence // 
    output.html(sentence);
    turtle();

  } else { // reset the tree and sentence, get random angle, call turtle 
    gen = 0;
    //sentence = "F";
    sentence = "X";  // for axiom X rules
    output.html(sentence);
    len = 100;
    angle = random(-60, 60);
    turtle();
  }
}

function turtle() {
  background(0);
  resetMatrix(); // need to reset the matrix each time through
  translate(width / 2, height);
  for (let i = 0; i < sentence.length; i++) {
    let current = sentence.charAt(i); // get char in sentence

    switch (current) {
      case "F":
        let alp = map(gen, 0, n, 255, 50); // mapping the alpha

        stroke(0, 255, 0, alp);
        line(0, 0, 0, -len); // line from origin up
        translate(0, -len); // move to the end of the line
        break;
      case "+":
        rotate(angle); //PI/6
        break;
      case "-":
        rotate(-angle); //PI/6
        break;
      case "[":
        push();
        break;
      case "]":
        pop();
        break;
    }
  }
}


/*
let rules = []; // put rules in an array so you can loop over them
rules[0] = {
  a: "F",
  b: "FF+[+F-F-F]-[-F+F+F]"
}
*/


/*   Shiffman substitution algorithm
     let found = false; // a catch to see if it is found
     for (let j = 0; j < rules.length; j++) { // loop over the rules array
       if (current == rules[j].a) {
         nextsentence += rules[j].b
         found = true;
         break; // only one rule can be true at a time;
      }

     }
     if (!found) {
       nextsentence += current
     }*/