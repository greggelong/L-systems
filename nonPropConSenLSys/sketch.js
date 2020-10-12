
let axiom="BBBBBBBBBBABBBBBBBBBB";

let gen=axiom;
let sz=20;
let y = 0;

function setup() {
  createCanvas(420, 820);
  background(0);
  frameRate(3);
  //showit();

   
  
}

function draw(){
  
  if(y < height){
  
    showit();
    replaceit();
  
  
  } else{
    //gen ="BBBBBBBBBBABBBBBBBBBB";
      background(0);
      y = 0;
  }
  
}


function showit(){
  for (let i=0;i<gen.length;i++){
    if (gen[i]==="B"){
      fill(0);
    }else{
      fill(255);
    }
    stroke(255,0,0);
    rect(i*sz,y,sz,sz);
  }
}
    
  
function replaceit(){
  nextGen = "";
  for(let i=0;i<gen.length;i++){
    // ((((i-1)%20)+20)%20) 
  threeText =gen [((((i-1)%gen.length)+gen.length)%gen.length)]+ gen[i] + gen[(i+1)%gen.length]
  //console.log(threeText)
  switch(threeText) {
  case"AAA":              //128
    nextGen = nextGen + "B"
    
    break;
  case "AAB":   //64
    nextGen = nextGen + "A"
    
    break;
    
   case "ABA":  //32
    nextGen = nextGen + "B"
    
    break;
  
   case "ABB": //16
    nextGen = nextGen + "A"
    
    break;
    
   case "BAA":  //8
    nextGen = nextGen + "A"
    
    break;
  
   case "BAB":  //4
    nextGen = nextGen + "B"
    
    break;
   case "BBA":    //2
    nextGen = nextGen + "A"
    
    break;
   case "BBB":    //1
    nextGen = nextGen + "B"
    
    break;
   
    }
 
  }
  y=y+sz;
  gen=nextGen;
}