function hello(){
  console.log("hello world!");
}

// Show type coersion
function addNum(num1,num2){
  console.log(num1+num2);
}

// Show default parameters
function formal(name="Derek",title='Sir'){
  console.log(title + " " + name);
}

// Now show returning
// Show default parameters
function formal(name="Derek",title='Sir'){
  return title + " " + name;
}

function timesFive(numInput){
  var result = numInput * 5
  return result
}

// GLOBAL SCOPE
// ANYTHING DEFINED OUTSIDE A FUNCTION IS GLOBAL
var v = "GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside function"
  console.log(stuff);
}
