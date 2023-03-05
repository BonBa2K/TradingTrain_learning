//Section 4
i = 0;
for (const readerEle of document.getElementsByClassName('reader')) {
    for (const readerRightEle of readerEle.children) {
        if (i % 2) {
            article_now = (i - 1) / 2;
            // S4_article_image
            readerRightEle.children[0].children[0].children[0].src = readerImageDataList[article_now].article[0].articleSrc;
            // S4_article_title 
            readerRightEle.children[0].children[1].children[1].children[0].innerHTML = readerImageDataList[article_now].article[0].articleTitle;
            // S4_article_image
            readerRightEle.children[1].children[0].children[0].src = readerImageDataList[article_now].article[1].articleSrc;
            // S4_article_title 
            readerRightEle.children[1].children[1].children[1].children[0].innerHTML = readerImageDataList[article_now].article[1].articleTitle;

        }
        else {
            // reader_image
            readerEle.children[0].children[0].href = readerImageDataList[i / 2].href;
            reader_imageElement = readerEle.children[0].children[0].children[0];
            reader_imageElement.src = readerImageDataList[i / 2].arthorSrc;
            // reader_author
            reader_authorElement = readerEle.children[0].children[1].children[0];
            reader_authorElement.innerHTML = readerImageDataList[i / 2].arthor;
            reader_authorElement.href = readerImageDataList[i / 2].arthorSrc;
            // reader_title
            reader_titleElement = readerEle.children[0].children[1].children[1];
            reader_titleElement.innerHTML = readerImageDataList[i / 2].arthorTitle;
            reader_titleElement.href = readerImageDataList[i / 2].arthorTitle;
        }
        i = i + 1;
    }
}

//Section 5
i = 0;
for (const item of document.getElementsByClassName('comment')) {
    // comment_image
    item.children[0].href = commentImageDataList[i].href;
    comment_imageElement = item.children[0].children[0];
    comment_imageElement.src = commentImageDataList[i].src;
    // comment_author
    comment_authorElement = item.children[1].children[0];
    comment_authorElement.innerHTML = commentImageDataList[i].text;
    comment_authorElement.href = commentImageDataList[i].text_href;
    // comment_title
    comment_authorElement = item.children[1].children[1];
    comment_authorElement.innerHTML = commentImageDataList[i].title;
    comment_authorElement.href = commentImageDataList[i].href;
    i = i + 1;
}
