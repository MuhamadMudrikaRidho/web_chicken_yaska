$(document).ready(() => {

  const username = $('#username-info').val();

  getCartData();
  getWishlistData();
  getOrdersData(username);

});

const viewOrder = (id) => {
  $(".anywere-home").addClass("bgshow");
  $(`#order-${id}`).addClass("popup");
}

$(".anywere-home").on('click', function () {
  $(".rts-newsletter-popup").removeClass("popup")
  $(".anywere-home").removeClass("bgshow")
});

const closeViewOrder = (id) => {
  $(`#order-${id}`).removeClass("popup")
  $(".anywere-home").removeClass("bgshow")
}

function formatRupiah(number) {
  // Pastikan input adalah angka
  if (isNaN(number)) {
    return "Invalid number";
  }

  // Konversi angka ke format Rupiah
  return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function showToast(title, message, delay = 5000, type = 'primary', url = '#', urlTitle = '') {
  const toastContainer = document.getElementById("toast-container");
  const toastElement = document.createElement("div");
  toastElement.classList.add("toast");
  toastElement.setAttribute("role", "alert");
  toastElement.setAttribute("aria-live", "assertive");
  toastElement.setAttribute("aria-atomic", "true");
  toastElement.setAttribute("data-bs-autohide", "true");
  toastElement.setAttribute("data-bs-delay", delay);
  toastElement.innerHTML = `
    <div class="toast-header bg-${type}">
      <strong class="me-auto text-light">${title}</strong>
      <small class="text-light">just now</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      ${message}
      <br>
      <a href='${url}'>${urlTitle}</a>
    </div>
  `;
  toastContainer.appendChild(toastElement);
  const toast = new bootstrap.Toast(toastElement);
  toast.show();
  toastElement.addEventListener('hidden.bs.toast', () => {
    toastElement.remove();
  });
}

const checkLogin = async () => {
  try {
    const response = await $.ajax({
      type: "GET",
      url: "/auth/check-login",
    });
    return response.isLoggedIn;
  } catch (error) {
    console.error("Error checking login status:", error);
    return false;
  }
};

const updateCartInDB = (cartId, quantity) => {
  $.ajax({
    type: "POST",
    url: "/cart/update",
    contentType: "application/json",
    data: JSON.stringify({
      cart_id: cartId,
      quantity: quantity
    }),
    success: (res) => {
      console.log(res.message);
    },
    error: (err) => {
      console.error("Failed to update cart:", err.responseJSON.error);
    }
  });
};


const incQty = (id) => {
  const qty = $(`#cart-qty-${id}`);
  const qtyCheckout = $(`#qty-checkout-${id}`);
  let currentQty = parseInt(qty.val());
  const subTotal = $(`#sub-total-${id}`);
  const productPrice = ($(`#product-price-${id}`)).data('price');

  // Pastikan currentQty tidak NaN atau kurang dari 1
  if (isNaN(currentQty) || currentQty < 1) currentQty = 1;

  // Tambahkan 1 ke qty
  const newQty = currentQty + 1;

  // Perbarui nilai qty dan qtyCheckout menjadi nilai baru
  qty.val(newQty);
  qtyCheckout.text(newQty);
  subTotal.text(`Rp. ${formatRupiah(newQty * productPrice)}`);

  // Perbarui total harga
  updateTotalPrice();

  // Perbarui database dengan qty baru
  updateCartInDB(id, newQty);
};


const incQtyGlobal = (id) => {
  const productQty = $(`#product-qnty-${id}`)
  const qtyGlobal = $(`#cart-qty-global-${id}`)
  let currentQtyGlobal = parseInt(qtyGlobal.val());
  if (isNaN(currentQtyGlobal) || currentQtyGlobal < 1) currentQtyGlobal = 1;
  qtyGlobal.val(currentQtyGlobal + 1)
  productQty.text(`${currentQtyGlobal + 1} ×`)
  updateTotalPriceGlobal();
  updateCartInDB(id, currentQtyGlobal + 1);
}

const decQty = (id) => {
  const qty = $(`#cart-qty-${id}`);
  const qtyCheckout = $(`#qty-checkout-${id}`);
  let currentQty = parseInt(qty.val());
  const subTotal = $(`#sub-total-${id}`);
  const productPrice = ($(`#product-price-${id}`)).data('price');

  // Pastikan currentQty tidak NaN atau kurang dari 1
  if (isNaN(currentQty) || currentQty <= 1) currentQty = 1;

  // Jika currentQty lebih besar dari 1, kurangi 1
  if (currentQty > 1) {
    const newQty = currentQty - 1;

    // Perbarui nilai qty dan qtyCheckout
    qty.val(newQty);
    qtyCheckout.text(newQty);
    subTotal.text(`Rp. ${formatRupiah(newQty * productPrice)}`);

    // Perbarui database dengan qty baru
    updateCartInDB(id, newQty);

    // Perbarui total harga
    updateTotalPrice();
  }
};

const decQtyGlobal = (id) => {
  const productQty = $(`#product-qnty-${id}`)
  const qtyGlobal = $(`#cart-qty-global-${id}`)
  let currentQtyGlobal = parseInt(qtyGlobal.val());
  if (isNaN(currentQtyGlobal) || currentQtyGlobal <= 1) currentQtyGlobal = 1;
  if (currentQtyGlobal > 1) {
    qtyGlobal.val(currentQtyGlobal - 1)
    productQty.text(`${currentQtyGlobal - 1} ×`)
    updateCartInDB(id, currentQtyGlobal - 1);
  }

  updateCartInDB(id, currentQtyGlobal - 1);
  updateTotalPriceGlobal();
}

const updateTotalPrice = () => {
  const totalPrice = $('#total-price');
  let total = 0;

  $('.cart-qty').each(function () {
    const qty = parseInt($(this).val());
    const price = parseFloat($(this).data('price'));

    if (!isNaN(qty)) {
      total += qty * price;
    }
  });

  totalPrice.text(`Rp. ${formatRupiah(total)}`);
};

const updateTotalPriceGlobal = () => {
  const totalPriceGlobal = $('#total-price-global');
  let total = 0;

  $('.cart-qty-global').each(function () {
    const qty = parseInt($(this).val());
    const price = parseFloat($(this).data('price'));

    if (!isNaN(qty)) {
      total += qty * price;
    }
  });
  totalPriceGlobal.text(`Rp. ${formatRupiah(total)}`);
}

// Fetching Cart Start
// const getCartData = async () => {

//   const cartBox = $('#cart-data-page');
//   const itemCheckout = $('#item-checkout');
//   const cartBoxGlobal = $('#cart-data-global')
//   const totalPrice = $('#total-price');
//   const totalPriceGlobal = $('#total-price-global');
//   const totalItems = $('#total-items-global');
//   const cartItemsTotal = $('#cart-items-total-global');
//   cartBox.html('<p>Loading...</p>');
//   cartBoxGlobal.html('<p>Loading...</p>');
//   itemCheckout.empty();
//   cartBox.empty();
//   cartBoxGlobal.empty();

//   $.ajax({
//     type: "GET",
//     url: "/cart/all",
//     data: {},
//     success: res => {

//       const carts = res.data;
//       const total = res.total;

//       totalPrice.text(`Rp. ${formatRupiah(total)}`);
//       totalPriceGlobal.text(`Rp. ${formatRupiah(total)}`);
//       totalItems.text(`MY CART (${res.data.length} ITEMS)`);
//       cartItemsTotal.text(res.data.length);

//       if (carts.length) {
//         carts.forEach(cart => {

//           const id = cart.id;
//           const name = cart.menu_name;
//           const category = cart.menu_category;
//           const image = cart.menu_image;
//           const qty = cart.quantity;
//           const price = cart.price;

//           const temp_html_global = `
//             <div class="product-item">
//             <div class="product-detail">
//               <div class="product-thumb"><img src="/static/${image}" alt="product-thumb">
//               </div>
//               <div class="item-wrapper">
//                 <span class="product-name">${name}</span>
//                 <div class="item-wrapper">
//                 </div>
//                 <div class="item-wrapper">
//                   <span class="product-qnty" id="product-qnty-${id}">${qty} ×</span>
//                   <span class="product-price">${price}</span>
//                 </div>
//               </div>
//             </div>
//             <div class="cart-edit">
//               <div class="quantity-edit">
//                 <button type="button" onclick="decQtyGlobal('${id}')" class="button minus">
//                   <i class="fal fa-minus minus"></i>
//                 </button>
//                 <input id="cart-qty-global-${id}" class="cart-qty-global" data-price="${price}" type="number" value="${qty}" disabled>
//                 <button type="button" onclick="incQtyGlobal('${id}')" class="button plus">
//                   <i class="fal fa-plus plus"></i>
//                 </button>
//               </div>
//               <div class="item-wrapper d-flex mr--5 align-items-center">
//                 <button onclick="removeFromCart('${id}')" class="delete-cart"><i class="fal fa-times"></i></button>
//               </div>
//             </div>
//           </div>
//           `

//           const temp_html_page = `
//               <tr>
//                 <td>
//                   <div class="product-thumb"><img src="/static/${image}"
//                       alt="product-thumb" style="width: 200px; height: 200px; border-radius: 7px;">
//                   </div>
//                 </td>
//                 <td>
//                   <div class="product-title-area">
//                     <span class="pretitle">${category}</span>
//                     <h4 class="product-title">${name}</h4>
//                   </div>
//                 </td>
//                 <td><span class="product-price" id="product-price-${id}" data-price="${price}">Rp. ${formatRupiah(price)}</span></td>
//                 <td>
//                 <td>
//                   <div class="cart-edit">
//                     <div class="quantity-edit">
//                         <button onclick="decQty('${id}')" class="button"><i class="fal fa-minus minus"></i></button>
//                         <input id="cart-qty-${id}" class="cart-qty" data-price="${price}" type="number" value="${qty}" disabled>
//                         <button onclick="incQty('${id}')" class="button plus">+<i class="fal fa-plus plus"></i></button>
//                     </div>
//                   </div>
//                 </td>

//                 </td>
//                 <td class="last-td">
//                   <button onclick="removeFromCart('${id}')" class="remove-btn">Remove</button>
//                 </td>
//               </tr>
//               `

//           const temp_html_checkout = `
//           <div class="category-item mb-2">
//                   <div
//                     class="category-item-inner"
//                     style="
//                       display: flex;
//                       justify-content: space-between;
//                       align-items: center;
//                     "
//                   >
//                     <div class="category-title-area">
//                       <span class="pretitle"> ${name} × <span id="qty-checkout-${id}">${qty}</span></span>
//                     </div>
//                     <div id="sub-total-${id}" class="price" style="text-align: right">Rp. ${formatRupiah(price * qty)}</div>
//                   </div>
//                 </div>
//           `

//           cartBox.append(temp_html_page)
//           cartBoxGlobal.append(temp_html_global)
//           itemCheckout.append(temp_html_checkout)
//         });
//       } else {
//         cartBox.html('<p>Cart is empty,<a href="/menu">Add Some</a></p>')
//       }
//     }
//   })
// }

const getCartData = async () => {
  const cartBox = $('#cart-data-page');
  const itemCheckout = $('#item-checkout');
  const cartBoxGlobal = $('#cart-data-global')
  const totalPrice = $('#total-price');
  const totalPriceGlobal = $('#total-price-global');
  const totalItems = $('#total-items-global');
  const cartItemsTotal = $('#cart-items-total-global');
  const orderButton = $('#order-btn');
  const orderButtonGlobal = $('#order-btn-global');

  cartBox.html('<p>Loading Menu...</p>');
  cartBoxGlobal.html('<p>Loading Menu...</p>');
  totalPrice.html('<p>Loading Total Price...</p>');
  totalPriceGlobal.html('<p>Loading Total Price...</p>');
  itemCheckout.empty();
  cartBox.empty();
  cartBoxGlobal.empty();

  $.ajax({
    type: "GET",
    url: "/cart/all",
    data: {},
    success: res => {
      const carts = res.data;
      const total = res.total;

      totalPrice.text(`Rp. ${formatRupiah(total)}`);
      totalPriceGlobal.text(`Rp. ${formatRupiah(total)}`);
      totalItems.text(`MY CART (${res.data.length} ITEMS)`);
      cartItemsTotal.text(res.data.length);

      if (carts.length) {
        carts.forEach(cart => {
          const id = cart.id;
          const name = cart.menu_name;
          const category = cart.menu_category;
          const image = cart.menu_image;
          const qty = cart.quantity;
          const price = cart.price;

          const temp_html_global = `
            <div class="product-item">
            <div class="product-detail">
              <div class="product-thumb"><img src="/static/${image}" alt="product-thumb">
              </div>
              <div class="item-wrapper">
                <span class="product-name">${name}</span>
                <div class="item-wrapper">
                </div>
                <div class="item-wrapper">
                  <span class="product-qnty" id="product-qnty-${id}">${qty} ×</span>
                  <span class="product-price">${price}</span>
                </div>
              </div>
            </div>
            <div class="cart-edit">
              <div class="quantity-edit">
                <button type="button" onclick="decQtyGlobal('${id}')" class="button minus">
                  <i class="fal fa-minus minus"></i>
                </button>
                <input id="cart-qty-global-${id}" class="cart-qty-global" data-price="${price}" type="number" value="${qty}" disabled>
                <button type="button" onclick="incQtyGlobal('${id}')" class="button plus">
                  <i class="fal fa-plus plus"></i>
                </button>
              </div>
              <div class="item-wrapper d-flex mr--5 align-items-center">
                <button onclick="removeFromCart('${id}')" class="delete-cart"><i class="fal fa-times"></i></button>
              </div>
            </div>
          </div>
          `;

          const temp_html_page = `
              <tr>
                <td>
                  <div class="product-thumb"><img src="/static/${image}"
                      alt="product-thumb" style="width: 200px; height: 200px; border-radius: 7px;">
                  </div>
                </td>
                <td>
                  <div class="product-title-area">
                    <span class="pretitle">${category}</span>
                    <h4 class="product-title">${name}</h4>
                  </div>
                </td>
                <td><span class="product-price" id="product-price-${id}" data-price="${price}">Rp. ${formatRupiah(price)}</span></td>
                <td>
                <td>
                  <div class="cart-edit">
                    <div class="quantity-edit">
                        <button onclick="decQty('${id}')" class="button"><i class="fal fa-minus minus"></i></button>
                        <input id="cart-qty-${id}" class="cart-qty" data-price="${price}" type="number" value="${qty}" disabled>
                        <button onclick="incQty('${id}')" class="button plus">+<i class="fal fa-plus plus"></i></button>
                    </div>
                  </div>
                </td>

                </td>
                <td class="last-td">
                  <button onclick="removeFromCart('${id}')" class="remove-btn">Remove</button>
                </td>
              </tr>
              `;

          const temp_html_checkout = `
          <div class="category-item mb-2">
                  <div
                    class="category-item-inner"
                    style="display: flex; justify-content: space-between; align-items: center;"
                  >
                    <div class="category-title-area">
                      <span class="pretitle"> ${name} × <span id="qty-checkout-${id}">${qty}</span></span>
                    </div>
                    <div id="sub-total-${id}" class="price" style="text-align: right">Rp. ${formatRupiah(price * qty)}</div>
                  </div>
                </div>
          `;

          cartBox.append(temp_html_page);
          cartBoxGlobal.append(temp_html_global);
          itemCheckout.append(temp_html_checkout);
          orderButton.attr({ 'href': '/order', 'class': 'procced-btn' })
          orderButtonGlobal.attr({ 'href': '/order', 'class': 'checkout-btn cart-btn' })
        });

      } else {
        cartBox.html('<p>Cart is empty,<a href="/menu">Add Some</a></p>');
        orderButton.attr({ 'href': '/menu', "class": "procced-btn" });
        orderButtonGlobal.attr({ 'href': '/menu', "class": 'checkout-btn cart-btn' })
      }
    }
  });
};


const addToCart = async (menu_id) => {

  const isLoggedIn = await checkLogin();
  if (!isLoggedIn) {
    window.location.href = "/auth/login";
    return;
  }

  const menuQty = $(`#qty-${menu_id}`).val();
  let qty = 1;
  if (menuQty) {
    qty = menuQty
  }

  $.ajax({
    type: "POST",
    url: `/cart/${menu_id}`,
    data: { quantity: qty },
    success: res => {
      showToast("added to cart", `${res.message}`, 3000, res.status, '/cart', 'go to cart &nbsp; <i class="fal fa-long-arrow-right"></i>');
      getCartData();
    }
  })
}


const removeFromCart = async (cart_id) => {

  const isLoggedIn = await checkLogin();
  if (!isLoggedIn) {
    window.location.href = "/auth/login";
    return;
  }

  $.ajax({
    type: "POST",
    url: `/cart/${cart_id}/destroy`,
    data: {},
    success: res => {
      showToast("deleted from cart", res.message, 2000, res.status);
      getCartData();
    }
  })
}
// Fetching Cart End

// Fetching Wishlist Start

const getWishlistData = () => {

  const wishlistBox = $('#wishlist-box');
  const wishlistItemsTotal = $('#wishlist-items-total');
  wishlistBox.html('<td></td><td>Loading...</td>');

  $.ajax({
    type: "GET",
    url: "/wishlist/all",
    data: {},
    success: res => {

      wishlistBox.empty();
      const wishlists = res.data;
      const totalItems = res.data.length;

      wishlistItemsTotal.text(totalItems)

      if (wishlists.length) {
        wishlists.forEach((wishlist) => {
          const name = wishlist.menu_name;
          const image = wishlist.menu_image;
          const price = wishlist.price;
          const id = wishlist.menu_id;

          const temp_html = `
            <tr>
                <td class="first-td"><button onclick="deleteWishlistData('${id}')" class="remove-btn"><i class="fal fa-times"></i></button></td>
                <td class="first-child"><a href="/menu/${id}"><img src="/static/${image}"
                            style="height: 100px; width: 100px;" alt=""></a>
                    <a href="/menu/${id}" class="pretitle">${name}</a>
                </td>
                <td><span class="product-price">Rp. ${formatRupiah(price)}</span></td>
                <td class="last-td"><button onclick="addToCart('${id}')" class="cart-btn"><i class="rt-basket-shopping"></i> Add To Cart</button>
                </td>
            </tr>
          `
          wishlistBox.append(temp_html)
        });
      } else {
        wishlistBox.append("<td></td><td>You haven't added any menus to your wishlist,<a href='/menu'>Add Some</a></p></td>")
      }

      console.log(res.message)
    }
  });
}

const addWishlistData = async (menu_id) => {
  const isLoggedIn = await checkLogin();
  if (!isLoggedIn) {
    window.location.href = "/auth/login";
    return;
  }

  $.ajax({
    type: "POST",
    url: `/wishlist/${menu_id}`,
    data: {},
    success: res => {

      if (res.status == 'danger') {
        showToast("can't added to wishlist", `${res.message}`, 3000, res.status, '/wishlist', 'go to wishlist &nbsp; <i class="fal fa-long-arrow-right"></i>');
      } else {
        showToast("added to wishlist", `${res.message}`, 3000, res.status, '/wishlist', 'go to wishlist &nbsp; <i class="fal fa-long-arrow-right"></i>');
      }

      getWishlistData();
    }
  })
}

const deleteWishlistData = async (menu_id) => {

  const isLoggedIn = await checkLogin();
  if (!isLoggedIn) {
    window.location.href = "/auth/login";
    return;
  }

  $.ajax({
    type: "post",
    url: `/wishlist/${menu_id}/destroy`,
    data: {},
    success: res => {
      showToast("deleted from wishlist", res.message, 2000, res.status);
      getWishlistData();
    }
  })
}

// Fetching Wishlist End

// Fetching Orders Start

const getOrdersData = (username) => {

  const ordersData = $('#orders-data');
  const orderPopup = $('#order-popup')

  $.ajax({
    type: "GET",
    url: `/order/all/${username}`,
    data: {},
    success: res => {

      ordersData.empty();

      if (res.data) {

        const orders = res.data;
        orders.forEach(order => {
          const id = order._id;
          const menuItems = order.items;
          const totalItems = order.items.length;
          const totalPrice = order.total_price;
          const status = order.status;
          const date = order.date;
          const payment = order.payment_method;
          const delivery = order.delivery_charge;
          const address = order.address;

          const temp_html = `
            <tr>
                <td>#${id}</td>
                <td>${date}</td>
                <td>${status}</td>
                <td>Rp. ${formatRupiah(totalPrice)} for ${totalItems} menu</td>
                <td><button onclick="viewOrder('${id}')" class="btn-small d-block">View</button></td>
            </tr>
          `

          const temp_html_order = `
            <div class="rts-newsletter-popup" id="order-${id}">
              <button onclick="closeViewOrder('${id}')" class="newsletter-close-btn"><i class="fal fa-times"></i></button>
              <div class="newsletter-inner">
                <div class="mb-2">
                  <span>#${id}</span>
                  <p style="margin: 0;">${date}</p>
                </div>
                <div class="mb-2">
                  <p style="margin: 0;">Delivered to</p>
                  <span>${address.address || "-"}</span>
                </div>
                <div class="mb-2">
                  <p style="margin-bottom: 0;">Status Order</p>
                  <h5>${status}</h5>
                </div>
                <div>
                  <p style="margin: 0;">Payment Method</p>
                  <h5>${payment}</h5>
                </div>
                <hr />
                <div style="max-height: 200px; overflow: auto;">
                ${menuItems.map((menu) => `
                  <div class="d-flex justify-content-between align-items-center">
                  <div>
                  <span>${menu.menu_name}</span>
                  <p style="margin-bottom: 0;">${menu.quantity}x</p>
                    </div>
                    <span>Rp. ${formatRupiah(menu.price * menu.quantity)}</span>
                    </div>
                    `).join('')}
                </div>
                <hr />
                <div>
                  <div class="d-flex justify-content-between align-items-center mb-1">
                    <p style="margin-bottom: 0;">Delivery Charge</p>
                    <span>Rp. ${formatRupiah(delivery)}</span>
                  </div>
                  <div class="d-flex justify-content-between align-items-center">
                    <h5>Total</h5>
                    <h5>Rp. ${formatRupiah(totalPrice)}</h5>
                  </div>
                </div>
              </div>
            </div>
          `;
          orderPopup.append(temp_html_order);
          ordersData.append(temp_html);
        });
      } else {
        $('#orders-page').html(res.message)
      }
    },
    error: err => {
      console.log("Something Wrong while fetching orders data");
    }
  })
}

const checkout = () => {

  const selectedPaymentMethod = $('input[name="paymentMethod"]:checked').val();

  if (!selectedPaymentMethod) {
    alert("Pilih metode pembayaran terlebih dahulu!");
    return;
  }

  const name = $('#name').val();
  const address = $('#address').val();
  const placeType = $('#placeType').val();
  const phone = $('#phone').val();
  const email = $('#email').val();
  const notes = $('#orderNotes').val();

  if (selectedPaymentMethod == "COD") {
    if (!name.length || !address.length || !phone.length) {
      alert("Mohon isi data Anda untuk pengiriman");
      return;
    }
  }


  const addressData = {
    name,
    address,
    placeType,
    phone,
    email,
    notes
  }

  $.ajax({
    type: "POST",
    url: "/order/checkout",
    data: JSON.stringify({ paymentMethod: selectedPaymentMethod, address: addressData }),
    contentType: "application/json",
    success: res => {
      alert(res.message);
      window.location.href = `/order/thankyou/${res.order_id}`
    },
    error: err => {
      if (err.responseJSON.info == "!login") {
        showToast("error", `${err.responseJSON.message}`, 3000, err.responseJSON.status, '/auth/login', `go to login page &nbsp; <i class="fal fa-long-arrow-right"></i>`);
      } else if (err.responseJSON.info == "!paymentMethod") {
        showToast("error", `${err.responseJSON.message}`, 3000, err.responseJSON.status);
      } else if (err.responseJSON.info == "!cart") {
        showToast("error", `${err.responseJSON.message}`, 3000, err.responseJSON.status, '/menu', `add some menu &nbsp; <i class="fal fa-long-arrow-right"></i>`);
      } else {
        showToast("500", `Something Wrong`, 3000, "danger", '/', `go to homepage &nbsp; <i class="fal fa-long-arrow-right"></i>`);
      }
    }
  });
};

