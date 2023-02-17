// create promotion
update_El_a_Img('promotion', promotionData)

// create logo
update_El_a_Img('logo', logoData)

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

// create cover_left
update_El_a_Img('cover_left_image', coverLeftData);
update_El_a('cover_left_text', coverLeftData)

// update cover_left_other_title List
update_other_titles('cover_left_other_title', coverLeftOtherTitleList);

// create cover_mid_top
update_El_a_Img('cover_mid_top_image', coverMidTopImageData);
update_El_a('cover_mid_top_text', coverMidTopTextData)

// create cover_mid_bottom
update_El_a_Img('cover_mid_bottom_image', coverMidBottomData);
update_El_a('cover_mid_bottom_title', coverMidBottomData)
update_El_a_text('cover_mid_bottom_text', coverMidBottomData)

// create cover_right editor_News
update_El_a('editor_News_title', editorNewsData)
update_El_a_text('editor_News_author', editorNewsData)

// create cover_right_editor_News_container
const coverRightEditorNewsContainer = document.getElementsByClassName('cover_right_editor_News_container');
const author_img_aElement = document.createElement('a');
const author_imgElement = document.createElement('img');
author_img_aElement.href = editorNewsData.text_href;
author_img_aElement.style.cssText = "width: 30%;";
author_imgElement.src = editorNewsData.src;
author_imgElement.style.cssText = "width: 100%;";
author_img_aElement.appendChild(author_imgElement);
coverRightEditorNewsContainer[0].appendChild(author_img_aElement);

// update cover_right_other_title List
update_other_titles('cover_right_other_title', coverRightOtherTitleList);