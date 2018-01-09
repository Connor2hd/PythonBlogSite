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
        <h3>Please Login to the Blog Site</h3><br>
      </div>
      <div class="row">
        <div class="container">
          <form action="/login" method="post">
            <label><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="txtUsername" required>

            <label><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="txtPassword" required>

            <button type="submit">Login</button>
          </form>
          </div>
        </div>
   </body>
</html>
