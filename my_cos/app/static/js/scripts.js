const imgHandler = () => {
    let imgLinksList = document.querySelectorAll(".form-img a");
    let ingLinksList = document.querySelectorAll(".form-ingredients-img a");

    if (imgLinksList[0]) {
        imgLinksList[0].innerHTML = "show img";
    }

    if (ingLinksList[0]) {
        ingLinksList[0].innerHTML = "show img";
    }
};

imgHandler();
