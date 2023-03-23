update_El_a_Img = (targetClass, targetData) => {
    const target_aElement = document.getElementsByClassName(targetClass);
    const target_imgElement = target_aElement[0].children[0];
    target_aElement.href = targetData.href;
    target_imgElement.src = targetData.src;
}

update_El_a = (targetClass, targetData) => {
    const targetEl = document.getElementsByClassName(targetClass);
    targetEl[0].innerHTML = targetData.title;
    targetEl[0].href = targetData.href;
}

update_El_a_text = (targetClass, targetData) => {
    const targetEl = document.getElementsByClassName(targetClass);
    targetEl[0].innerHTML = targetData.text;
    targetEl[0].href = targetData.text_href;
}
update_other_titles = (targetClass, targetDataList) => {
    const targetEl = document.getElementsByClassName(targetClass);
    i = 0;
    for (const item of targetDataList) {
        targetEl[i].innerText = item.title;
        targetEl[i].href = item.href;
        i = i + 1;
    }
}