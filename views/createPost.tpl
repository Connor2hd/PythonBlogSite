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
        <center><h2>Welcome USER</h2><br>
        <h3>Create New Blog Post</h3><br>
      </div>
      <div class="row">
      <form class="col s12" action="/insertPost" method="post">
      <div class="row">
        <div class="input-field col s12">
          <textarea id="textarea1" name="blogText" class="materialize-textarea"></textarea>
          <label for="textarea1">New Blog Post</label>
        </div>
      </div>
      <button type="submit" value="Submit">Submit</button>
    </form>
  </div>
   </body>
</html>
