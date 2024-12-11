const makeSureModal = (id) => {
  $(`#modal-delete-menu-${id}`).modal('show')
  $(`#modal-delete-user-${id}`).modal('show')
}