function newElement() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
      if (inputValue === '') {
          
      } else {
      document.getElementById("myUL").appendChild(li);
      }
    document.getElementById("myInput").value = "";
  }