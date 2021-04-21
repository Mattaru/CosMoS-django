const imgHandler = () => {
    let formImg = document.querySelector(".form-img");
    let imgLink = document.querySelectorAll(".form-img a")[0].href;
    let formIngredientsImg = document.querySelector(".form-ingredients-img");
    let ingredientsLink = document.querySelectorAll(".form-ingredients-img a")[0].href;

    formImg.innerHTML = `
    <p>Currently:</p>
    <img class="currently-img" src="${imgLink}">
    <input type="file" name="img" accept="img/*" id="img_id">
    `;

    if (ingredientsLink) {
        formIngredientsImg.innerHTML = `
        <p>Currently:</p>
        <img class="currently-img" src="${ingredientsLink}">
        <input type="file" name="img" accept="img/*" id="img_id">
        `;
    } else {
        formIngredientsImg.innerHTML = `
        <input type="file" name="img" accept="img/*" id="img_id">
        `;
    }
};

imgHandler();
