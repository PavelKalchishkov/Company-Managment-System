document.addEventListener("DOMContentLoaded", () => {
$(document).ready(function() {
    function tester() {
        const company_id = $("#id_company").val();
        if (!company_id) {
         return;
        }

        fetch(`/invoices/companies/get-company-values/${company_id}`)
            .then(response =>{
                return response.json()
            })
            .then(company_data => {
                document.getElementById("company_database_name_p").innerText = company_data.company_database_name;
                document.getElementById("company_id_p").innerText = company_data.id;
                document.getElementById("company_eik_p").innerText = company_data.eik;
                document.getElementById("company_dds_p").innerText = company_data.dds;
                document.getElementById("company_name_p").innerText = company_data.name;
                document.getElementById("company_address_p").innerText = company_data.address;
                document.getElementById("company_mol_p").innerText = company_data.mol;
                document.getElementById("company_recipient_p").innerText = company_data.recipient;
            })
    }

$("#id_company").on("change", tester);
});

});