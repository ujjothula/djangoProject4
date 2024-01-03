from django.shortcuts import render



# Create your views here.
def hello(request):
    print("hello request url executed");
    tt = '''
  
<!DOCTYPE html>
<html>
<body>
<style>
body  {
  background-image: url("paper.gif");
  background-color:lightpink;
}
</style>
<center>
<h1 style="background-color:lightblue;">Aparna Construction PVT.Limited</h1><br><br>
<form action="/action_page.php">
  <label for="fname">Username: </label>
  <input type="text" id="fname" name="fname"><br><br>
  
  <label for="lname">Password: </label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="submit">
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>
</center>
</body>
</html>


   	''';
    return HttpResponse(tt);
