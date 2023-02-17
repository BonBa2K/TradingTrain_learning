//Section 6
update_El_a_Img("S6_image", S6Data)
S6TextArea_aElement = document.getElementsByClassName("S6_text_area");
S6TextArea_aElement[0].href = S6Data.href;
S6Text_aElement = document.getElementsByClassName("S6_text");
S6Text_aElement[0].innerHTML = S6Data.text;
S6Text_aElement = document.getElementsByClassName("S6_title");
S6Text_aElement[0].innerHTML = S6Data.title;
//Section 7

update_El_a_Img('army_1_image', army1ImageData);
update_El_a('army_1_title', army1ImageData);
update_El_a_text('army_1_text', army1ImageData);
update_El_a_Img('army_2_image', army2ImageData);
update_El_a('army_2_title', army2ImageData);
update_El_a_text('army_2_text', army2ImageData);

update_El_a_Img('hot_1_image', hot1ImageData);
update_El_a('hot_1_title', hot1ImageData);
update_El_a_text('hot_1_text', hot1ImageData);
update_El_a_Img('hot_2_image', hot2ImageData);
update_El_a('hot_2_title', hot2ImageData);
update_El_a_text('hot_2_text', hot2ImageData);