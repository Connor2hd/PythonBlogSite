<html>
   <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="stylesheet.css">
   </head>
   <body>
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
      <div>
        <center><h2>Welcome</h2><br>
        <h3>All Current Blog Posts by All Users</h3><br>
        <a class="waves-effect waves-light btn" href="/allBlogs"><i class="material-icons left">camera</i>View All Blog Posts</a><br><br>
      </div>
      %for t in Posts:
      <div class="row">
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
    </div>
      %end
      %end
   </body>
</html>
