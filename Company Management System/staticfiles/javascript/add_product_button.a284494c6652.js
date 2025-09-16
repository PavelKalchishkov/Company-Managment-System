// The trenches

document.addEventListener("DOMContentLoaded", function () {
  const addMoreBtn = document.getElementById("add-more");
  const formsetContainer = document.getElementById("formset-container");
  const totalForms = document.getElementById("id_orderproduct_set-TOTAL_FORMS");

  addMoreBtn.addEventListener("click", function () {
    const currentFormCount = parseInt(totalForms.value);
    const firstForm = formsetContainer.querySelector(".form-row");

    // Destroy select2 before cloning to avoid issues
    $(firstForm).find("select").select2('destroy');

    const newForm = firstForm.cloneNode(true);

    // Reset values
    newForm.querySelectorAll("input, select").forEach((field) => {
      field.value = "";
    });

    // Update name/id attributes
    newForm.innerHTML = newForm.innerHTML.replaceAll(
      /orderproduct_set-(\d+)-/g,
      `orderproduct_set-${currentFormCount}-`
    );

    formsetContainer.appendChild(newForm);
    totalForms.value = currentFormCount + 1;

    // Re-initialize Select2 on both old and new selects
    $('#formset-container select').select2();
  });

  // Initial load
  $('#id_client, #id_employee, #id_shipper').select2();
  $('#formset-container select').select2();
});
