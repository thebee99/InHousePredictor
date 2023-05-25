  function goIndonesian(){
    document.body.classList.add('loadingCursor');
    setTimeout(function(){
      window.location.href = 'Indonesian Version.html';
      document.body.classList.remove('loadingCursor');
    }, 1000);
    
  }

  function goEnglish(){
    document.body.classList.add('loadingCursor');
    setTimeout(function(){
      window.location.href = 'Ai Based House Estimation Price.html';
      document.body.classList.remove('loadingCursor');
    }, 1000);
    
  }

  function goToPredict(){
    var section = document.getElementById("signup");
    section.scrollIntoView({ behavior: "smooth"});
  }

  function sellProperty(){
    window.location.href = 'https://www.rumah.com/'
  }

  /* When the user clicks on the button,
  toggle between hiding and showing the dropdown content */

  function myFunction(dropdownName) {
    document.getElementById(dropdownName).classList.toggle("show");
  }
  
  function filterFunction(dropdownName, input) {
    var input, filter, ul, li, a, i;
    input = document.getElementById(input);
    filter = input.value.toUpperCase();
    div = document.getElementById(dropdownName);
    a = div.getElementsByTagName("button");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }

  function replaceName(myName, buttonName, label){
    const mainbutton = document.getElementById(buttonName);
    mainbutton.innerText = label + myName;
  }

  function showDialog(text) {
    var dialogBox = document.getElementById("dialogBox");
    var dialogText = document.getElementById("dialogText");
    dialogText.textContent = text;
    dialogBox.style.display = "block";
  }
  
  function hideDialog() {
    var dialogBox = document.getElementById("dialogBox");
    dialogBox.style.display = "none";
  }


  function myFunction1(myDropdown, buttonNumber, description, initializer, final, description1, input) {
    
    document.getElementById(myDropdown).classList.toggle("show");

    var line = '<input type="text" placeholder="Search ' + description1 + '" id="'+ input +'" onkeyup="filterFunction('+ "'" +myDropdown+ "'" +', '+ "'" +input+ "'" +')">';
    document.getElementById(myDropdown).insertAdjacentHTML('beforeend', line);
    

    for(var i=initializer; i<final; i++){
        var button = '<button onclick="replaceName(' + "'" + i + "'" +', ' + "'" + buttonNumber + "'" + ', '+ "'" +description+ "'" +')" class="myButtons">'+ i +'</button>';
        document.getElementById(myDropdown).insertAdjacentHTML('beforeend', button);
    }
  }

  function readFile(path,myDropdown, buttonNumber, description, description1, input){
    document.getElementById(myDropdown).classList.toggle("show");

    var line = '<input type="text" placeholder="Search ' + description1 + '" id="'+ input +'" onkeyup="filterFunction('+ "'" +myDropdown+ "'" +', '+ "'" +input+ "'" +')">';
    document.getElementById(myDropdown).insertAdjacentHTML('beforeend', line);

    var lines;

    fetch(path)
    .then(response => response.txt())
    .then(contents => {
        lines = contents.split('\n');
    })
    .catch(error => {
        console.error('Error finding file', error);
    })

    for(var i=0; i < lines.length; i++){
        
    }

    document.addEventListener("DOMContentLoaded", function() {
      const button = document.getElementById("button");
      const addressText = "Address";
      button.textContent = addressText;
    
      const logoImage = new Image();
      logoImage.src = "escritorio/WebsitePrototype2/static/img/location.png";
      logoImage.classList.add("logo-image");
    
      button.innerHTML = ""; // Clear the button's existing content
      button.appendChild(logoImage); // Append the logo image to the button
      button.appendChild(document.createTextNode(addressText)); // Append the text node to the button
    
      const otherDropdowns = document.querySelectorAll(".dropdown:not(#location)");
      otherDropdowns.forEach(function(dropdown) {
        dropdown.classList.add("no-logo");
      });
    });
    
    
    
    
    


  }
  

  
