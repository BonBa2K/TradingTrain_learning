// targetClass,targetcss is string
create_El_a_Img = (targetClass, targetData,targetcss) => {
    const target = document.getElementsByClassName(targetClass);
    const target_aElement = document.createElement('a');
    const target_imgElement = document.createElement('img');
    target_imgElement.style.cssText = targetcss
    target_imgElement.src = targetData.src;
    target_aElement.appendChild(target_imgElement);
    target_aElement.href = targetData.href;
    target[0].appendChild(target_aElement);
}
