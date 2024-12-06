$(document).ready(() => {
  getCartData();
  getWishlistData();
});

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
  let currentQty = parseInt(qty.val());
  if (isNaN(currentQty) || currentQty < 1) currentQty = 1;

  qty.val(currentQty + 1);

  updateTotalPrice();
  updateCartInDB(id, currentQty + 1);
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
  let currentQty = parseInt(qty.val());
  if (isNaN(currentQty) || currentQty <= 1) currentQty = 1;

  if (currentQty > 1) {
    qty.val(currentQty - 1);
    updateCartInDB(id, currentQty - 1);
  }

  updateCartInDB(id, currentQty - 1);
  updateTotalPrice();
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
const getCartData = async () => {

  const cartBox = $('#cart-data-page');
  const cartBoxGlobal = $('#cart-data-global')
  const totalPrice = $('#total-price');
  const totalPriceGlobal = $('#total-price-global');
  const totalItems = $('#total-items-global');
  const cartItemsTotal = $('#cart-items-total-global');
  cartBox.html('<p>Loading...</p>');
  cartBoxGlobal.html('<p>Loading...</p>');

  $.ajax({
    type: "GET",
    url: "/cart/all",
    data: {},
    success: res => {

      cartBox.empty();
      cartBoxGlobal.empty();

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
          `

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
                <td><span class="product-price">Rp. ${formatRupiah(price)}</span></td>
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
              `

          cartBox.append(temp_html_page)
          cartBoxGlobal.append(temp_html_global)
        });
      } else {
        cartBox.html('<p>Cart is empty,<a href="/menu">Add Some</a></p>')
      }
    }
  })
}

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