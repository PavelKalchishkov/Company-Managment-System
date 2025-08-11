document.addEventListener("DOMContentLoaded", () => {
$(document).ready(function() {
    function change_order_details() {
        const order_id = $("#id_order").val()
        if (!order_id) {
            return;
        }

        fetch(`/orders/get-order-values/${order_id}`)
            .then(response => {
                return response.json()
        })
            .then(order_data => {
                document.getElementById("order_id_p").innerText = order_data.id;
                document.getElementById("order_price_p").innerText = order_data.price;
                document.getElementById("order_products_p").innerText = order_data.products.join("\n");
                document.getElementById("order_payment_method_p").innerText = order_data.payment_method;
                document.getElementById("order_status_p").innerText = order_data.status;
                document.getElementById("order_address_p").innerText = order_data.address;
                document.getElementById("order_version_p").innerText = order_data.version;
                document.getElementById("order_client_p").innerText = order_data.client;
                document.getElementById("order_employee_p").innerText = order_data.employee;
                document.getElementById("order_shipper_p").innerText = order_data.shipper;
            })
    }

if ($("#id_order").val()) {
    change_order_details()
}

$("#id_order").on("change", change_order_details);
});
});