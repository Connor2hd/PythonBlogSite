$(function()
{
  $.get('http://localhost:8082/blog_posts/Alex', function(r)
  {
    let temp = $("#blogTemp").html();
    let output = Mustache.render(temp, r)
    $("#blogPosts").html(output);
  });
});
