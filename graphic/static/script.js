document.addEventListener('DOMContentLoaded', function () {
    function handleCheckboxChange(checkbox, checkboxes) {
        checkbox.addEventListener("change", function () {
            checkboxes.forEach(function (cb) {
                cb.checked = checkbox.checked;
            });
        });
    }

    var countryCheckbox = document.getElementById("countryCheckbox");
    var countryCheckboxes = document.querySelectorAll("#dropdownContentCountry input[type='checkbox']");
    handleCheckboxChange(countryCheckbox, countryCheckboxes);

    var stateCheckbox = document.getElementById("stateCheckbox");
    var stateCheckboxes = document.querySelectorAll("#dropdownContentState input[type='checkbox']");
    handleCheckboxChange(stateCheckbox, stateCheckboxes);

    var jobCheckbox = document.getElementById("job");
    var jobCheckboxes = document.querySelectorAll("#dropdownContentJob input[type='checkbox']");
    handleCheckboxChange(jobCheckbox, jobCheckboxes);

    var yearCheckbox = document.getElementById("year");
    var yearCheckboxes = document.querySelectorAll("#dropdownContentYear input[type='checkbox']");
    handleCheckboxChange(yearCheckbox, yearCheckboxes);

    var mkbCheckbox = document.getElementById("MKB");
    var mkbCheckboxes = document.querySelectorAll("#dropdownContentMKB input[type='checkbox']");
    handleCheckboxChange(mkbCheckbox, mkbCheckboxes);
});

document.getElementById("create-chart-button").addEventListener("click", function() {
    document.querySelector("form").submit();
});