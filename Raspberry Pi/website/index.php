<html>
  <head>
    <meta charset="UTF-8">
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
    <script src="js/bootstrap.bundle.min.js" type="text/javascript"></script>
    <style>
     body {
     background-color: #FFA500;
     }
     #form-box {
      width: 380px;
      height: 480px;
      position: relative;
      margin: 6% auto;
      background-color: #fff;
      padding: 5px;
     }
     .title {
       text-align: center;
       
     }
     .form-group {
       top: 180px;
       position: absolute:
       width: 280px;
       transition: .5s;
       padding: 20px;
     }
     .form-control {
       width: 100%;
       padding: 10px 0;
       margin: 5px 0;
       border-left: 0;
       border-top: 0;
       border-right: 0;
       border-bottom: 1px solid #999;
       outline: none;
       background: transparent;
      }
     .submit-btn {
       width: 85%;
       padding: 10px 30px;
       cursor: pointer;
       display: block;
       margin: auto;
       margin-top: 30px;
       background: linear-gradient(to right, #ff105f, #ffad06);
       border: 0;
       outline: none;
       border-radius: 30px;
      }
    </style>
  </head>

<body id="body">
<div class="container" id="form-box">
  <div class="title">
    <h1>C300</h1>
  </div>
  <form id="login" class="form-group" method="post" action="doLogin.php">
    <input class="form-control" type="text" placeholder="Enter Username" name="username" id="username" required>
    <br>
    <input class="form-control" type="text" placeholder="Enter Password" name="password" id="password" required>
    <input class="submit-btn" type="Submit" value="Login">
  </form>  
</div>
</body>
</html>

