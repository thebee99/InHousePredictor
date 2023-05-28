function replaceCertificate(certificateName, buttonName, label) {
    const mainButton = document.getElementById(buttonName);
    mainButton.innerText = label + certificateName;
  }
  
  function myFunction2(myDropdown, buttonNumber, description, description1, input) {
    document.getElementById(myDropdown).classList.toggle("show");
  
    var line = '<input type="text" placeholder="Search ' + description1 + '" id="' + input + '" onkeyup="filterFunction(' + "'" + myDropdown + "'" + ', ' + "'" + input + "'" + ')">';
    document.getElementById(myDropdown).insertAdjacentHTML('beforeend', line);
  
    readFile('txt_files/certificates.txt', function(content) {
      var certificateOptions = content.split('\n');
      for (var i = 0; i < certificateOptions.length; i++) {
        var button = '<button onclick="replaceCertificate(' + "'" + certificateOptions[i] + "'" + ', ' + "'" + buttonNumber + "'" + ', ' + "'" + description + "'" + ')" class="myButtons">' + certificateOptions[i] + '</button>';
        document.getElementById(myDropdown).insertAdjacentHTML('beforeend', button);
      }
    });
  }
  