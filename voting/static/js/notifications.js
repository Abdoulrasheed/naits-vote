$(function () {
  function check_messages() {
    $.ajax({
      url: '/notifications/',
      cache: false,
      success: function (data) {
        $("#unread").text(data);
      },
      complete: function () {
        window.setTimeout(check_messages, 3000);
      }
    });
  };
  check_messages();
});