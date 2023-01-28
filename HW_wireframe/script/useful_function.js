// targetClass,targetcss is string
create_El_a_Img = (targetClass, targetData, targetcss) => {
    const targetEl = document.getElementsByClassName(targetClass);
    const target_aElement = document.createElement('a');
    const target_imgElement = document.createElement('img');
    target_aElement.style.cssText = 'height: 100%;';
    target_imgElement.style.cssText = targetcss;
    target_imgElement.src = targetData.src;
    target_imgElement.className = targetClass + '_img';
    target_aElement.appendChild(target_imgElement);
    target_aElement.href = targetData.href;
    targetEl[0].appendChild(target_aElement);
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