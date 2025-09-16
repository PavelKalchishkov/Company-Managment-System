$(document).ready(function() {
    const urlParams = new URLSearchParams(window.location.search);
    const companyId = urlParams.get('company');
    if (companyId) {
        $('#id_company').val(companyId).trigger('change');
    }
});
