const makeSureModal = (menu_id) => {
  $(`#modal-delete-menu-${menu_id}`).modal('show')
}

const deleteMenu = (menu_id) => {
  $.ajax({
    type: "POST",
    url: `/admin/menu/${menu_id}/destroy`,
    success: res => {
      window.location.href = '/admin/menu';
    }
  })
}

const postMenu = () => {
  const formData = new FormData()

  const name = $('#name').val();
  const category = $('#category').val();
  const price = $('#price').val();
  const image = $('#image').prop("files")[0];
  const description = $('#description').val();

  formData.append('name', name)
  formData.append('category', category)
  formData.append('price', price)
  formData.append('image', image)
  formData.append('description', description)

  $.ajax({
    type: "POST",
    url: "/admin/menu",
    data: formData,
    contentType: false,
    processData: false,
    success: res => {
      alert(res.status);
      console.log(res.data)
    },
    error: err => {
      console.error("AJAX Error:", err);
      alert("Error: " + err.responseText || "Something went wrong!");
    }
  })
}