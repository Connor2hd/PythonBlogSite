<html>
   <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
   </head>
   <body>
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
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
      </div>
      %for c in t["comments"]:
      <div>
         <h2>{{c['commentAuthor']}}</h2>
         <br>
         <h3>{{c['commentDate']}}</h3>
         <br>
         <p>{{c['commentText']}}</p>
         <br>
      </div>
      %end
      %end
   </body>
</html>
