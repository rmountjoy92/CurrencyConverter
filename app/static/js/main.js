let convertCurrencyForm = document.getElementById("convertCurrencyForm");
let convertCurrencyFormSuccess = document.getElementById("convertCurrencyFormSuccess");
let convertCurrencyFormError = document.getElementById("convertCurrencyFormError");

convertCurrencyForm.addEventListener("submit", function (e) {
    e.preventDefault();
    fetch(convertCurrencyURL, {
        method: "post",
        body: new FormData(convertCurrencyForm),
    })
        .then((r) => r.json())
        .then(function (r) {
            if (r.data.error) {
                convertCurrencyFormSuccess.classList.add('d-none');
                convertCurrencyFormError.classList.remove('d-none');
                convertCurrencyFormError.innerText = r.data.error;
            } else {
                convertCurrencyFormError.classList.add('d-none');
                convertCurrencyFormSuccess.classList.remove('d-none');
                convertCurrencyFormSuccess.innerText = r.data.result;
            }
        });
});
