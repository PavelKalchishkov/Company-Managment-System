
document.addEventListener("DOMContentLoaded", () => {
const orderSelect = document.getElementById("id_order");
const price_without_dds_input = document.getElementById("id_whole_price_without_dds");
const price_with_dds_input = document.getElementById("id_whole_price_with_dds")
const dds = document.getElementById("id_DDS")
const discount = document.getElementById("id_discount")

orderSelect.addEventListener("change", () => {
  const orderId = orderSelect.value;
  if (!orderId)
      return;

  fetch(`/orders/get-order/${orderId}/`)
    .then(response => {
      return response.json();
    })
    .then(data => {
      if (data.price !== undefined) {
        let dds_value = parseFloat(dds.value);
        if (dds_value !== 0) {
          dds_value *= 0.01;
          dds_value *= data.price;
        }

        let discount_value = parseFloat(discount.value);
        if (discount_value !== 0) {
            discount_value *= 0.01;
        }

        price_without_dds_input.value = data.price - (data.price * discount_value);
        price_with_dds_input.value = (data.price + dds_value) - (data.price + dds_value) * discount_value;
      }
    })
    .catch(error => {
      console.error("AJAX error:", error);
    });
});
});
