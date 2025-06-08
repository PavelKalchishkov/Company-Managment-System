document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript is running");

    const formsetContainer = document.getElementById("formset-container");
    const totalFormsInput = document.querySelector('#id_orderproduct_set-TOTAL_FORMS');

    document.getElementById("add-more").addEventListener("click", function () {
        if (!totalFormsInput) {
            console.error("TOTAL_FORMS input not found in the DOM!");
            return;
        }

        const formCount = parseInt(totalFormsInput.value);
        const templateHtml = document.getElementById("empty-form-template").innerHTML;
        const newFormHtml = templateHtml.replace(/__prefix__/g, formCount);

        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = newFormHtml;

        const newFormElement = tempDiv.firstElementChild;
        formsetContainer.appendChild(newFormElement);

        // Increment the form count
        totalFormsInput.value = formCount + 1;

        // Initialize Select2 on any <select> in the new form row
        $(newFormElement).find("select").select2();
    });

    // Init Select2 on initial selects
    $('#id_client, #id_employee, #id_shipper').select2();
    $('#formset-container select').select2();
});
