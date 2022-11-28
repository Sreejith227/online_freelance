$(".slider")
  .slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true
  })
  .on("setPosition", function () {
    resizeSlider();
  });

$(window).on("resize", function (e) {
  resizeSlider();
});

var slickHeight = $(".slick-track").outerHeight();

var slideHeight = $(".slick-track").find(".slick-slide").outerHeight();

function resizeSlider() {
  $(".slick-track")
    .find(".slick-slide .slide-wrap")
    .css("height", slickHeight + "px");
}
$(document).ready(function(){
  // Prepare the preview for profile picture
      $("#wizard-picture").change(function(){
          readURL(this);
      });
  });
  function readURL(input) {
      if (input.files && input.files[0]) {
          var reader = new FileReader();
  
          reader.onload = function (e) {
              $('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
          }
          reader.readAsDataURL(input.files[0]);
      }
  }



  