document.addEventListener("DOMContentLoaded", function () {
  const addMoreBtn = document.getElementById("add-more");
  const formsetContainer = document.getElementById("formset-container");
  const totalForms = document.getElementById("id_orderproduct_set-TOTAL_FORMS");

  addMoreBtn.addEventListener("click", function () {
    const currentFormCount = parseInt(totalForms.value);
    const firstForm = formsetContainer.querySelector(".form-row");
    const newForm = firstForm.cloneNode(true);

    // Reset values in the cloned form
    newForm.querySelectorAll("input, select").forEach((field) => {
      field.value = "";
    });

    // Update the name and id attributes to match the new form index
    newForm.innerHTML = newForm.innerHTML.replaceAll(
      /orderproduct_set-(\d+)-/g,
      `orderproduct_set-${currentFormCount}-`
    );

    formsetContainer.appendChild(newForm);
    totalForms.value = currentFormCount + 1;
  });
});
