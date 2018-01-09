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

        <center><h2>Welcome </h2><h2 name="lblUsername" value="{{lblUsername}}">{{lblUsername}}</h2><br>

        <h3>Your Current Blog Posts</h3><br>
        <a class="waves-effect waves-light btn" href="/allBlogs"><i class="material-icons left">camera</i>View All Blog Posts</a><br><br>
      </div>

      <br>
      <div class="row">
      <form class="col s12" action="/insertPost" method="post">
      <div class="row">
        <input type="hidden" name="username" value="{{lblUsername}}">
        <div class="input-field col s12">
          <textarea id="textarea1" name="blogText" class="materialize-textarea"></textarea>
          <label for="textarea1">New Blog Post</label>
        </div>
      </div>
      <button type="submit" value="Submit" class="waves-effect waves-light btn">Submit Post</button>
    </form>
  </div>
      <br>
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
                  <a href="#">{{t["date"]}}</a><br>
                  <div class="row">
                  <form class="col s1" action="/deletePost" method="post">
                    <button class="waves-effect waves-light btn" type="submit" name="id" value="{{t['_id']}}">Delete</button>
                    <input type="hidden" value="{{t['author']}}" name="author">
                  </form>
                  <form class="col s1" action="/updatePostPage" method="post">
                    <button class="waves-effect waves-light btn" type="submit" name="id" value="{{t['_id']}}">Edit</button>
                    <input type="hidden" value="{{t['author']}}" name="author">
                  </form>
                </div>
                  <hr>
                  <div class="row">
                  <form action="/insertComment" method="post">
                    <textarea name="commentText" class="materialize-textarea"></textarea>
                    <input type="hidden" value="{{t['author']}}" name="author">
                    <input type="hidden" value="{{t['_id']}}" name="postId">
                    <button type="submit" value="Submit" class="waves-effect waves-light btn">Submit Comment</button>
                  </form>
                </div>
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
               </span><br><br>
               {{c['commentDate']}}
            </div>
         </div>
      </div>
    </div>
      %end
      %end
   </body>
</html>
