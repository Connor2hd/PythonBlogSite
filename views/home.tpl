<html>
<h1>Welcome User</h1>
<br>
<h2>Your Blog Posts</h2>
<br>
<div>
%for t in collection:
<h2>{{t["author"]}}</h2>
<br>
<h3>{{t["date"]}}</h3>
<br>
<p>{{t["text"]}}</p>
%end
</div>
</html>