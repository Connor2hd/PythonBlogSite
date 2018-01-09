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
        <center><h2></h2><br>
        <h3>Update Blog Post</h3><br>
      </div>
      %for t in Posts:
      <div class="row">
         <div class="col s12 m12">
            <div class="card blue-grey darken-1">
               <div class="card-content white-text">
                  <span class="card-title">{{t["author"]}}</span>
                  <p>{{t["text"]}}</p>
               </div>
               <div class="card-action">
                  <a href="#">{{t["date"]}}</a>
                  <form action="/deletePost" method="post">
                    <button class="waves-effect waves-light btn" type="submit" name="id" value="{{'_id'}}">Delete</button>
                    <input type="hidden" value="{{t['author']}}" name="author">
                  </form>
                  <br>
               </div>
            </div>
         </div>
      </div>

      <br>

      <div class="row">
      <form class="col s12" action="/updatePost" method="post">
      <div class="row">
        <div class="input-field col s12">
          <textarea name="newText" class="materialize-textarea">{{t["text"]}}</textarea>
          <input type="hidden" value="{{t['author']}}" name="author">
          <input type="hidden" value="{{t['_id']}}" name="id">
        </div>
      </div>
      <button type="submit" value="Submit" class="waves-effect waves-light btn">Submit Post</button>
    </form>
  </div>
  %end
   </body>
</html>
