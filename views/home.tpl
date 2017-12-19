<html>
   <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link href="stylesheet.css" rel="stylesheet">
   </head>
   <body>
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
      <h1>Welcome User</h1>
      <br>
      <h2>Your Blog Posts</h2>
      <br>
      <center><a class="waves-effect waves-light btn"><i class="material-icons left">edit</i>Create New Post</a></center>
      %for t in collection:
      <div class="row">
         <div class="col s12 m12">
            <div class="card blue-grey darken-1">
               <div class="card-content white-text">
                  <span class="card-title">{{t["author"]}}</span>
                  <p>{{t["text"]}}</p>
               </div>
               <div class="card-action">
                  <a href="#">{{t["date"]}}</a>
               </div>
            </div>
         </div>
      </div>
      %for c in t["comments"]:
      <div class="row">
         <div class="col s12 m5">
            <div class="card-panel teal" style="margin-left: 150px;">
               <{{c['commentAuthor']}}
               <span class="white-text">{{c['commentText']}}
               </span><br>
               {{c['commentDate']}}
            </div>
         </div>
      </div>
      %end
      %end
   </body>
</html>
