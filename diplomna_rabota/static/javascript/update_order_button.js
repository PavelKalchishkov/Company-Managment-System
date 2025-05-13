document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript is running");

    document.getElementById("add-more").addEventListener("click", function () {
        const formsetContainer = document.getElementById("formset-container");
        const totalFormsInput = document.querySelector('#id_orderproduct_set-TOTAL_FORMS');

        if (!totalFormsInput) {
            console.error("TOTAL_FORMS input not found in the DOM!");
            return;
        }

        const formCount = parseInt(totalFormsInput.value);

        const templateHtml = document.getElementById("empty-form-template").innerHTML;
        const newFormHtml = templateHtml.replace(/__prefix__/g, formCount);

        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = newFormHtml;

        // Append the new form row
        formsetContainer.appendChild(tempDiv.firstElementChild);

        // Increment the management form counter
        totalFormsInput.value = formCount + 1;
    });
});
