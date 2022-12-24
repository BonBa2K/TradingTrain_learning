const name_El = document.getElementById("name");
const email_El = document.getElementById("email");
const phone_El = document.getElementById("phone");
const addButton_El = document.getElementById("addButton");
const tbody = document.getElementById("tbody");


AddNewRow = () => {
    var input_Name = name_El.value;
    var input_email = email_El.value;
    var input_phone = phone_El.value;
    var tr = document.createElement('tr')
    var td = []

    /*seting new row */
    for (var i = 0; i < 5; i++) {
        td.push(document.createElement('td'))
    }
    td[0].innerText = input_Name;
    td[1].innerText = input_email;
    td[2].innerText = input_phone;
    td[3].innerText = new Date().toISOString();
    td[4].innerHTML = '<button >修改</button> <button class= "deleteButton">刪除</button>';
    for (var i = 0; i < 5; i++) {
        tr.appendChild(td[i]);
    }
    tbody.appendChild(tr);

    /*delete button addEventListener */
    tr.children[4].children[1].addEventListener('click', function () {
        tr.remove();
    });
    /*用id */

    /*clear value*/
    name_El.value = "";
    email_El.value = "";
    phone_El.value = "";
}

var tr = document.createElement('tr')
var td = []
/*Listener setting*/
addButton_El.addEventListener('click', AddNewRow)

for (var i = 0; i < 5; i++) {
    td.push(document.createElement('td'))
}
td[0].innerText = '杜伊凱';
td[1].innerText = 'z890657@gmail.com';
td[2].innerText = '0920200954';
td[3].innerText = new Date().toISOString();
td[4].innerHTML = '<button >修改</button> <button class= "deleteButton">刪除</button>';
for (var i = 0; i < 5; i++) {
    tr.appendChild(td[i]);
}
tbody.appendChild(tr);

/*delete button addEventListener */
tr.children[4].children[1].addEventListener('click', function () {
    tr.remove();
});