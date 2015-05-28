$(document).ready(function(){

  var theme = $("#theme")

  $("#changeStyle").on("click", function(){
    console.log(theme.attr("href"))
    if (theme.attr("href") === "css/orangeFlair.css"){
      theme.attr("href","css/basic.css")
      $("#changeStyle").css("color","#1C4678")

    }
    else {
      theme.attr("href","css/orangeFlair.css")
      $("#changeStyle").css("color","#FF644F")
    }
  })

})
