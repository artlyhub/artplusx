// $(function () {
//   /* 1. OPEN THE FILE EXPLORER WINDOW */
//   $(".js-upload-photos").click(function () {
//     $("#fileupload").click();
//   });
//
//   /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
//   $("#fileupload").fileupload({
//     dataType: 'json',
//     done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
//       if (data.result.is_valid) {
//         console.log(data.result.is_valid)
//         $("#gallery tbody").prepend(
//           "<tr><td><a href='" + data.result.url + "'>" + data.result.title + "</a></td></tr>"
//         )
//       }
//     }
//   });
//
// });

$(function() {
  var elem = document.querySelector('.masonry-grid')
  var msnry = new Masonry(elem, {
    itemSelector: '.grid-item',
    columnWidth: 200,
    gutter: 10
  })
})
