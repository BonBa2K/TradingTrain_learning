const one_Button = document.getElementById("one");
const two_Button = document.getElementById("two");
const three_Button = document.getElementById("three");
const four_Button = document.getElementById("four");
const five_Button = document.getElementById("five");
const six_Button = document.getElementById("six");
const seven_Button = document.getElementById("seven");
const eight_Button = document.getElementById("eight");
const nine_Button = document.getElementById("nine");
const zero_Button = document.getElementById("zero");

const point_Button = document.getElementById("point"); 
const clear_Button = document.getElementById("clear"); 
const backspace_Button = document.getElementById("backspace"); 
const OutputElement = document.getElementById("output"); 

num_Button = document.getElementsByClassName("num"); 
operator_Buttons = document.getElementsByClassName("operator"); 

Output = "0"; 
temp = ""; 
evalStringArray = []; 
/*function define*/
updateDisplayVal = (input) =>{ 
    let buttonText = input.target.innerHTML; 
    if(Output === "0"){
        Output = '';
    }
    
    Output += buttonText;
    OutputElement.innerHTML = Output;
}
CalculatingCore = (input) => {
    operator = input.target.innerHTML; 
    switch(operator){
        case '+':
            temp = Output; 
            Output = '0'; 
            OutputElement.innerText = Output;
            /*append string*/ 
            evalStringArray.push(temp); 
            evalStringArray.push('+'); 
            break;
        case '-':
            temp = Output;
            Output = '0';
            /*append string*/ 
            OutputElement.innerText = Output;
            evalStringArray.push(temp);
            evalStringArray.push('-');
            break;  
        case 'x':
            temp = Output;
            Output = '0';
            OutputElement.innerText = Output;
            /*append string*/ 
            evalStringArray.push(temp);
            evalStringArray.push('*');
            break;
        case '÷':
            temp = Output;
            Output = '0';
            OutputElement.innerText = Output;
            /*append string*/ 
            evalStringArray.push(temp);
            evalStringArray.push('/');
            break;  
        case '=':
            evalStringArray.push(Output); 
            /*Calculate */
            Output = eval(evalStringArray.join(' ')); 
            OutputElement.innerText = Output; 
            evalStringArray = []; 
            break; 
        default:
            break;
    }
}

/*initialize Listener*/
for(let i=0; i < num_Button.length; i++){ 
    num_Button[i].addEventListener("click",updateDisplayVal,false) 
}
for(let i=0; i < operator_Buttons.length; i++){ 
    operator_Buttons[i].addEventListener("click",CalculatingCore,false)
}
/* AC */
clear_Button.onclick = () => {
    Output = "0"; 
    pendingVal = undefined; 
    evalStringArray = []; 
    OutputElement.innerHTML = Output; 
}
/* backspace */
backspace_Button.onclick = () =>{
    let lengthOfDisplayVal = Output.length; 
    Output = Output.slice(0, lengthOfDisplayVal -1); 
    if(Output === ""){ Output = "0"; }
    OutputElement.innerHTML = Output;  
}
/* point */
point_Button.onclick = () => {
    if(!Output.includes('.')){ Output +="."; }
    OutputElement.innerText = Output; 
}
