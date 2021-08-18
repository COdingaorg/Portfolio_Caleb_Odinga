// function getDocHeight() {	// $(document).height() value depends on browser
//   var D = document;
//   return Math.max(
//     D.body.scrollHeight, D.documentElement.scrollHeight,
//     D.body.offsetHeight, D.documentElement.offsetHeight,
//     D.body.clientHeight, D.documentElement.clientHeight
//   );
// }
$(document).ready(function () {
  $('#talk_talk').click(function (event) {
    event.preventDefault()
    $(document).scrollTop($(document).height())
    $("#footer_page").focus()
    $("#footer_page").css({'border':'2px solid gold'})
    
  })
  $('div#the-story:nth-child(3)').removeclass('col-md-6')
  $('div#the-story:nth-child(3)').addclass('col-md-12')
  $('div#the-story:nth-child(3)').css({'border':'red'})
  
})
