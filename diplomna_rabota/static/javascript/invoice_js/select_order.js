$(document).ready(function () {
  const price_without_dds_input = $("#id_whole_price_without_dds");
  const price_with_dds_input = $("#id_whole_price_with_dds");
  const dds = $("#id_DDS");
  const discount = $("#id_discount");

function update_price() {
  const orderId = $("#id_order").val();
  if (!orderId)
      return;

  fetch(`/orders/get-order/${orderId}/`)
    .then(response => {
      return response.json();
    })
    .then(data => {
      if (data.price !== undefined) {
        let dds_value = parseFloat(dds.val());
        if (dds_value !== 0) {
          dds_value *= 0.01;
          dds_value *= data.price;
        }

        let discount_value = parseFloat(discount.val());
        if (discount_value !== 0 && discount_value) {
            discount_value *= 0.01;
        }
        else {
          discount_value = 0
        }

          price_without_dds_input.val((data.price - (data.price * discount_value)).toFixed(2));
          price_with_dds_input.val(((data.price + dds_value) - (data.price + dds_value) * discount_value).toFixed(2));
      }
    })
    .catch(error => {
      console.error("AJAX error:", error);
    });
  }

$("#id_order").on("change", update_price);
$("#id_discount").on("input", update_price);
$("#id_DDS").on("change", update_price);
});

