//
//
const optionMenu = document.getElementById("73"),
    options = optionMenu.querySelectorAll(".option");
//     optionMenu2 = document.getElementById("73"),
//     selectBtn = document.getElementById("B72"),
//     selectBtn2 = document.getElementById("B73"),
    // sBtn_text = optionMenu.querySelector(".sBtn-text");
//
// selectBtn.addEventListener("click", () =>
//     optionMenu.classList.toggle("active")
// );
// selectBtn2.addEventListener("click", () =>
//     optionMenu2.classList.toggle("active")
// );
//
//
options.forEach((option) => {
    option.addEventListener("click", () => {
        optionMenu.classList.remove("active");
        option.classList.add("selected");
        const url = '/search_auto/?address=' + option.textContent;
        console.log(url);
    });
});
//
// $(document).ready(function () {
//     if (!$.browser.webkit) {
//         $('.wrapper').html('<p>Sorry! Non webkit users. :(</p>');
//     }
// });