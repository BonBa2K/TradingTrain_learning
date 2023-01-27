// create promotion
create_El_a_Img('promotion', promotionData, 'width:100% ;height:80px')

// create logo
create_El_a_Img('logo', logoData, 'width:100% ;height:100%')

// create menu
const menu = document.getElementsByClassName('menu');
for (const item of menuList) {
    const menu_aElement = document.createElement('a');
    menu_aElement.innerText = item.name
    menu_aElement.href = item.href
    menu[0].appendChild(menu_aElement);
}

// create menu_2
const menu_2 = document.getElementsByClassName('menu_2');
for (const item of menuList) {
    const menu_2_aElement = document.createElement('a');
    menu_2_aElement.innerText = item.name
    menu_2_aElement.href = item.href
    menu_2[0].appendChild(menu_2_aElement);
}

// create cover_mid_top
create_El_a_Img('cover_mid_top_image', coverMidTopImageData, 'width:100% ;height:100%')
const coverMidTopText = document.getElementsByClassName('cover_mid_top_text');
coverMidTopText[0].innerHTML = coverMidTopTextData.text;
coverMidTopText[0].href = coverMidTopTextData.href;

// create cover_mid_top
create_El_a_Img('cover_left_image', coverLeftImageData, 'width:95% ;')

const coverLeftOtherTitle = document.getElementsByClassName('cover_left_other_title');
i = 0;
for (const item of coverLeftOtherTitleList) {
    coverLeftOtherTitle[i].innerText = item.title;
    coverLeftOtherTitle[i].href = item.href;
    i = i + 1;
}
const coverRightOtherTitle = document.getElementsByClassName('cover_right_other_title');
i = 0;
for (const item of coverRightOtherTitleList) {
    coverRightOtherTitle[i].innerText = item.title;
    coverRightOtherTitle[i].href = item.href;
    i = i + 1;
}