$(document).ready(function () {
  $('#name').on('input', function () {
    var name = $(this).val();
    if (name.length < 2 || !/^[a-zA-Z\s]+$/.test(name)) {
      $('#nameError').text('Nama harus minimal 2 karakter dan hanya mengandung huruf dan spasi.');
    } else {
      $('#nameError').text('');
    }
  });

  $('#username').on('input', function () {
    var username = $(this).val();
    if (username.length < 3 || !/^[a-zA-Z0-9_]+$/.test(username)) {
      $('#usernameError').text('Nama pengguna harus minimal 3 karakter dan hanya boleh berisi huruf, angka, dan garis bawah.');
    } else {
      $('#usernameError').text('');
    }
  });

  $('#email').on('input', function () {
    var email = $(this).val().toLowerCase();
    var emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    if (!emailRegex.test(email)) {
      $('#emailError').text('Format email tidak valid.');
    } else {
      $('#emailError').text('');
    }
  });

  $('#password').on('input', function () {
    var password = $(this).val();
    var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!passwordRegex.test(password)) {
      $('#passwordError').text('Kata sandi harus minimal 8 karakter dan mengandung setidaknya satu huruf besar, satu huruf kecil, dan satu angka.');
    } else {
      $('#passwordError').text('');
    }
  });

  $('#registerForm').on('submit', function (event) {
    if ($('#nameError').text() || $('#usernameError').text() || $('#emailError').text() || $('#passwordError').text()) {
      event.preventDefault();
      alert("Harap perbaiki kesalahan sebelum mengirimkan.");
    }
  });
});
