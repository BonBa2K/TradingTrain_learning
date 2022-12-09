const OutputElement = document.getElementById("output");

const point_Button = document.getElementById("point");
const clear_Button = document.getElementById("clear");
const backspace_Button = document.getElementById("backspace");

const num_Buttons = document.getElementsByClassName("num");
const operator_Buttons = document.getElementsByClassName("operator");

const htmlEl = document.documentElement;
/*鍵盤讀取函式 */
Key_Function = (event) => {
    console.log("event.key = " + event.key);
    switch (event.key) {
        case '7':
            num_Buttons[0].click();
            break;
        case '8':
            num_Buttons[1].click();
            break;
        case '9':
            num_Buttons[2].click();
            break;
        case '4':
            num_Buttons[3].click();
            break;
        case '5':
            num_Buttons[4].click();
            break;
        case '6':
            num_Buttons[5].click();
            break;
        case '1':
            num_Buttons[6].click();
            break;
        case '2':
            num_Buttons[7].click();
            break;
        case '3':
            num_Buttons[8].click();
            break;
        case '0':
            num_Buttons[9].click();
            break;
        case '/':
            operator_Buttons[0].click();
            break;
        case '*':
            operator_Buttons[1].click();
            break;
        case '-':
            operator_Buttons[2].click();
            break;
        case 'Enter':
            operator_Buttons[3].click();
            break;
        case '+':
            operator_Buttons[4].click();
            break;
        case '.':
            point_Button.click();
            break;
        case 'Backspace':
            backspace_Button.click()
            break;
        case 'Escape':
            clear_Button.click()
            break;

    }
}
htmlEl.addEventListener('keyup', Key_Function);

var output = "0";
var operand_0 = 0;
var operand_1 = 0;
var operand_status = false;

/*function define*/
/*數字鍵*/
NumCore = (input) => {
    let buttonText = input.target.innerHTML;
    if (output == "0") {
        output = '';
    }
    output += buttonText;
    OutputElement.innerHTML = output;
    OutputElement.style.left = '0px';
}
/*運算鍵 */
OpCore = (input) => {
    if (operand_status == false) {
        if (input.target.innerHTML != '=') {
            operator = input.target.innerHTML;
            operand_status = true;
            if (!OutputElement.innerHTML.includes('.'))
                operand_0 = parseInt(OutputElement.innerHTML);
            else
                operand_0 = parseFloat(OutputElement.innerHTML);
            output = '0';
        }
    }
    else {
        if (!OutputElement.innerHTML.includes('.'))
            operand_1 = parseInt(OutputElement.innerHTML);
        else
            operand_1 = parseFloat(OutputElement.innerHTML);

        operand_0 = CalculatingCore(operand_0, operand_1, operator)
        operand_1 = 0;
        output = '0';
        OutputElement.innerHTML = operand_0;

        if (input.target.innerHTML == '=') {
            operator = null;
            operand_status = false;
        }
    }
    OutputElement.style.left = '0px';
}
/*計算程式 */
CalculatingCore = (op_0, op_1, op) => {
    switch (op) {
        case '+':
            return op_0 + op_1;
        case '-':
            return op_0 - op_1;
        case 'x':
            return op_0 * op_1;
        case '÷':
            if (op_1 != 0)
                return op_0 / op_1;
            else
                return 'error';
        default:
            break;
    }
}

/*滑動輸出內容相關函式*/
var move = false;
var exmove = false;
var origin_x;
mouseDown = () => {
    move = true;
}
mouseUp = () => {
    move = false;
}
function MoveOutput(event) {
    bodyElement = document.body;
    // console.log("exmove == " + exmove);
    // console.log("move == " + move);
    if (move == true) {
        if (exmove != move) {
            origin_x = event.clientX;
            origin_offset = OutputElement.offsetLeft;

        }
        else {
            OutputElement.style.left = (origin_offset + event.clientX - origin_x) + 'px';
        }
        // document.getElementById("c_p_x").textContent = event.clientX;
        // document.getElementById("c_p_y").textContent = origin_x;
        // document.getElementById("c_p_z").textContent = boxElement.offsetLeft
    }
    exmove = move;
}

/*initialize Listener*/
for (let i = 0; i < num_Buttons.length; i++) {
    num_Buttons[i].addEventListener("click", NumCore)
}
for (let i = 0; i < operator_Buttons.length; i++) {
    operator_Buttons[i].addEventListener("click", OpCore)
}
/* AC */
clear_Button.onclick = () => {
    output = "0";
    operand_0 = 0;
    operand_1 = 0;
    operand_status = false;
    float_status = false;

    OutputElement.innerHTML = output;
    OutputElement.style.left = '0px';
}
/* backspace */
backspace_Button.onclick = () => {
    let lengthOfDisplayVal = output.length;
    output = output.slice(0, lengthOfDisplayVal - 1);
    if (output === "") { output = "0"; }
    OutputElement.innerHTML = output;
    OutputElement.style.left = '0px';
}
/* point */
point_Button.onclick = () => {
    if (!output.includes('.')) { output += "."; }
    OutputElement.innerText = output;
    OutputElement.style.left = '0px';
}
