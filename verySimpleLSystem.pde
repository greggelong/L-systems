String current = "F"; // axiom
// Number of  generations
int count = 0;
float len;
float angle = 25;

void setup() {
  size(600, 600);
  background(0);
  stroke(255,100);
  len =height/4;
  //println("Generation " + count + ": " + current);
  translate(width/2,height);
  turtle();
}

void draw(){
 // you need draw to listen for mouse pressed
 // but if you put in noLoop it will not draw
 // maybe different from canvas in p5js
 
  
}

void mousePressed() {
   if (count < 5){
  // A new StringBuffer for the next generation
  StringBuffer next = new StringBuffer();
  
  // Look through the current String to replace according to L-System rules
  for (int i = 0; i < current.length(); i++) {
    char c = current.charAt(i);
    if (c == 'F') {
      // If we find F replace with long string
      next.append("FF+[+F-F-F]-[-F+F+F]");
    } else{   // otherwise append the non expanding  character
      next.append(c);
  }
  }
  // The current String is now the next one
  current = next.toString();
  println("this is current", current);
  count++;
  // Print to message console
  //println("Generation " + count + ": " + current);
  //println(count + " " + current.length());
  // srink line
  len*=0.5;
  // send to turtle to render
  turtle();
  
}else{
 current = "F";
 background(0);
 angle = random(-60,60);
 count = 0;
 len = height/4;
 turtle();
}
}
  
  



void turtle(){
  
  background(0);
  resetMatrix(); // need to reset the matrix each time through
  
  translate(width/2,height);  // turtle origin
  
  for (int i =0; i < current.length(); i++){
    char ch = current.charAt(i);
   
    switch (ch) {
      case 'F':   // note well single quotes 'are for chr and dub " for string
        float alph = map(count,0,5,255,60);
        stroke(255,alph);
        fill(255);
        //ellipse(0,0,12,12);
        line(0, 0, 0, -len); // turtle starts by moving up from origin
        translate(0, -len); // trans to end of that line
        //rect(0,0,20,20);
       
        break;
      case '+':
        
        rotate(radians(angle)); //PI/6
        break;
      case '-':
        rotate(radians(-angle)); //PI/6
        break;
      case '[':
        pushMatrix();
        break;
      case ']':
        popMatrix(); 
        break;

    }
    
  }
  
  
  
}
