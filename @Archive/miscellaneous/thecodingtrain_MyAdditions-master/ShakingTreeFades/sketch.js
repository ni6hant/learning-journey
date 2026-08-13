var angle = 0; //Creates a variable with name "angle" and assignes it's value to 0
var branchFraction = 0.5; //Creates a variable with name "branchFunction" and assignes it's value to 0.5

function setup() { //this is the setup function which I dont know a lot about
  createCanvas(600 ,600); //Creates a blank window with width 600 and height 600
  }

function draw() {
  background(225); //Assignes the color with color code 225 (white) to the background
  translate(200,height); //moves the origin to 200 in x direction and height(600) in the -y direction
  //Now the new coordinate is at the bottom of the canvas and 200 from the left edge of the canvas
  stroke(0,map(millis(),0,10000,225,0),0); //Stroke function defines a color for a new shape to be drawn
  //millis() returns the time since the program was run in milli seconds
  angle1 = (PI/4)*random(0.94,0.95);  //angle1 is defined as PI/4*(random value between 0.94 and 0.95)
  angle2 = (PI/4)*random(0.89,0.90);  //angle2 is defined as PI/4*(random value between 0.89 and 0.90)
  branch(100);
}

function branch(len){
  line(0,0,0,-len);
  translate(0,-len);
  if (len>1){
    push();
    rotate(angle1*random(0.95,0.96));
    branch(len*branchFraction*random(0.85,0.86));
    branch(len*branchFraction);
    pop();
    push();
    rotate(-angle2*random(0.85,0.86));
    branch(1.1*len*branchFraction*random(0.80,0.81));
    branch(len*branchFraction);
    pop();
  }
}
