$('#add_item').click(function () {
  const element = $('<li></li>').text('Item');
  $('ul.my_list').append(element);
});
