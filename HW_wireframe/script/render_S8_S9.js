//Section 8

const newestList = document.getElementsByClassName('newest');
i = 0;
for (const Ele of newestList) {
    // newest_image
    Ele.children[0].href = newestDataList[i].href;
    newest_imageElement = Ele.children[0].children[0];
    newest_imageElement.src = newestDataList[i].src;
    // newest_title
    newest_titleElement = Ele.children[1].children[0].children[0];
    newest_titleElement.innerHTML = newestDataList[i].title;
    newest_titleElement.href = newestDataList[i].href;
    // newest_text
    newest_textElement = Ele.children[1].children[1].children[0];
    newest_textElement.innerHTML = newestDataList[i].text;
    newest_textElement.href = newestDataList[i].text_href;
    i = i + 1;
}

//Section 9
const podList = document.getElementsByClassName('pod');
i = 0;
for (const Ele of podList) {
    // pod_image
    Ele.children[0].href = podDataList[i].href;
    pod_imageElement = Ele.children[0].children[0];
    pod_imageElement.src = podDataList[i].src;
    // pod_title
    pod_titleElement = Ele.children[1].children[0].children[0];
    pod_titleElement.innerHTML = podDataList[i].title;
    pod_titleElement.href = podDataList[i].href;
    i = i + 1;
}

update_El_a_Img('footer_social_FB', footerSocialList[0]);
update_El_a_Img('footer_social_IG', footerSocialList[1]);
update_El_a_Img('footer_social_LINE', footerSocialList[2]);
update_El_a_Img('footer_social_YT', footerSocialList[3]);

