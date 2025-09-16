$(document).ready(function() {
    const urlParams = new URLSearchParams(window.location.search);
    const orderId = urlParams.get('order');
    if (orderId) {
        $('#id_order').val(orderId).trigger('change');
    }
});
