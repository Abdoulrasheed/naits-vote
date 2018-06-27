  function check_notifications() {
    $.ajax({
      url: '/messages/',
      cache: false,
      success: function (data) {
        if (data != "0") {
          $("#notifications").addClass("new-notifications");
        }
        else {
          $("#notifications").removeClass("new-notifications");
        }
      },
      complete: function () {
        window.setTimeout(check_notifications, 6000);
      }
    });
  };
  check_notifications();
});