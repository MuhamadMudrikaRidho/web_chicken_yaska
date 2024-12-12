$(document).ready(function () {
  // Rating logic
  const stars = $('#rating-icons span');
  const ratingInput = $('#rating');
  const ratingError = $('#rating-error');
  const form = $('#review-form');

  stars.on('click', function () {
    const value = $(this).data('value');
    ratingInput.val(value);

    stars.find('i').removeClass('fas').addClass('fal');
    stars.slice(0, value).find('i').removeClass('fal').addClass('fas');

    ratingError.hide();
  });

  form.on('submit', function (e) {
    if (!ratingInput.val()) {
      e.preventDefault();
      ratingError.show();
    }
  });

  // Profile image logic
  const profileImage = $('#profileImage');
  const profileInput = $('#profileInput');
  const profileForm = $('#profileForm');
  const cancelUpdate = $('#cancelUpdate');

  let originalProfileSrc = profileImage.attr('src');

  $('.profile-dp').on('click', function () {
    profileInput.click();
  });

  profileInput.on('change', function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        profileImage.attr('src', e.target.result);
      };
      reader.readAsDataURL(file);

      profileForm.show();
    }
  });

  cancelUpdate.on('click', function () {
    profileImage.attr('src', originalProfileSrc);
    profileInput.val('');
    profileForm.hide();
  });

});