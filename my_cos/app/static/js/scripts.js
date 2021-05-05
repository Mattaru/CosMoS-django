const updatingImgHandler = () => {
    let formImg = document.querySelector(".form-img");
    let imgLink = document.querySelectorAll(".form-img a");

    if (formImg && imgLink) {
        formImg.innerHTML = `
        <p>Currently:</p>
        <img class="currently-img" src="${imgLink[0].href}" alt="product img">
        <input type="file" name="img" accept="img/*" id="img_id">
        `;
    }
};

updatingImgHandler();
