// update promotion
update_El_a_Img('promotion', promotionData)

// update logo
update_El_a_Img('logo', logoData)

// update menu
const menu = document.getElementsByClassName('menu');
for (const item of menuList) {
    const menu_aElement = document.createElement('a');
    menu_aElement.innerText = item.name
    menu_aElement.href = item.href
    menu[0].appendChild(menu_aElement);
}

// update menu_2
const menu_2 = document.getElementsByClassName('menu_2');
for (const item of menuList) {
    const menu_2_aElement = document.createElement('a');
    menu_2_aElement.innerText = item.name
    menu_2_aElement.href = item.href
    menu_2[0].appendChild(menu_2_aElement);
}

// update cover_left
update_El_a_Img('cover_left_image', coverLeftData);
update_El_a('cover_left_text', coverLeftData)

// update cover_left_other_title List
update_other_titles('cover_left_other_title', coverLeftOtherTitleList);

// update cover_mid_top
update_El_a_Img('cover_mid_top_image', coverMidTopImageData);
update_El_a('cover_mid_top_text', coverMidTopTextData)

// update cover_mid_bottom
update_El_a_Img('cover_mid_bottom_image', coverMidBottomData);
update_El_a('cover_mid_bottom_title', coverMidBottomData)
update_El_a_text('cover_mid_bottom_text', coverMidBottomData)

// update cover_right editor_News
update_El_a('editor_News_title', editorNewsData)
update_El_a_text('editor_News_author', editorNewsData)
update_El_a_Img('cover_right_editor_News_author_img', editorNewsData);

// update cover_right_other_title List
update_other_titles('cover_right_other_title', coverRightOtherTitleList);

update_El_a_Img('cover_right_newspaper_news', newspaperNewsData);
update_El_a_Img('newspaper_768_news', newspaperNewsData);
