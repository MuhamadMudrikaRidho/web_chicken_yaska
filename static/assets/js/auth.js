$(document).ready(function () {
  $('#name').on('input', function () {
    var name = $(this).val();
    if (name.length < 2 || !/^[a-zA-Z\s]+$/.test(name)) {
      $('#nameError').text('Name must be at least 2 characters and only contain letters and spaces.');
    } else {
      $('#nameError').text('');
    }
  });

  $('#username').on('input', function () {
    var username = $(this).val();
    if (username.length < 3 || !/^[a-zA-Z0-9_]+$/.test(username)) {
      $('#usernameError').text('Username must be at least 3 characters and can only contain letters, numbers, and underscores.');
    } else {
      $('#usernameError').text('');
    }
  });

  $('#email').on('input', function () {
    var email = $(this).val().toLowerCase();
    var emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    if (!emailRegex.test(email)) {
      $('#emailError').text('Invalid email format.');
    } else {
      $('#emailError').text('');
    }
  });

  $('#password').on('input', function () {
    var password = $(this).val();
    var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!passwordRegex.test(password)) {
      $('#passwordError').text('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.');
    } else {
      $('#passwordError').text('');
    }
  });

  $('#registerForm').on('submit', function (event) {
    if ($('#nameError').text() || $('#usernameError').text() || $('#emailError').text() || $('#passwordError').text()) {
      event.preventDefault();
      alert("Please fix the errors before submitting.");
    }
  });
});
