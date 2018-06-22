$(function () {

  $(".btn-more_about").click(function () {
    if ($(".about_student").hasClass("composing")) {
      $(".about_student").removeClass("composing");
      $(".about_student").slideUp();
    }
    else {
      $(".about_student").addClass("composing");
      $(".about_student textarea").val("");
      $(".about_student").slideDown(600, function () {
        $(".about_student textarea").focus();
      });
    }
  });
});