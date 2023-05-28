$(document).ready(function() {
  // Fetch the translation text from the JSON file
  fetch('translation.json')
    .then(response => response.json())
    .then(data => {
      // Use the translation text based on the selected language
      const language = 'indonesian'; // Replace with your logic to determine the selected language
      const translations = data[language];

      // Update the text content using the translations
      document.getElementById('services').textContent = translations.services;
      document.getElementById('questions').textContent = translations.questions;
      document.getElementById('feedback').textContent = translations.feedback;
      document.getElementById('contact').textContent = translations.contact;
    })
    .catch(error => {
      console.error('Failed to fetch translation data:', error);
    });

  // Event listener for "Contact Us" button
  $('#contact-us-button').click(function(e) {
    e.preventDefault();
    $('#floatMessage').show();
  });

  // Event listener for close button in the floating message
  $('#close').click(function() {
    hideDialog();
  });

  // Submit form event listener
  $('#contactForm').submit(function(e) {
    e.preventDefault();
    // Perform any necessary form validation or data processing here

    // Show the success message
    $('#floatMessage').show();
    // Clear the form fields
    $(this).trigger('reset');
  });

  // Other JavaScript functions
  function goIndonesian() {
    document.body.classList.add('loadingCursor');
    setTimeout(function() {
      window.location.href = 'Indonesian Version.html';
      document.body.classList.remove('loadingCursor');
    }, 1000);
  }

  function goEnglish() {
    document.body.classList.add('loadingCursor');
    setTimeout(function() {
      window.location.href = 'Ai Based House Estimation Price.html';
      document.body.classList.remove('loadingCursor');
    }, 1000);
  }

  function sellProperty() {
    window.location.href = 'https://www.rumah.com/';
  }

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

  function replaceName(myName, buttonName, label) {
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

    var line = '<input type="text" placeholder="Search ' + description1 + '" id="' + input + '" onkeyup="filterFunction(\'' + myDropdown + '\', \'' + input + '\')">';
    document.getElementById(myDropdown).insertAdjacentHTML('beforeend', line);

    for (var i = initializer; i < final; i++) {
      var button = '<button onclick="replaceName(\'' + i + '\', \'' + buttonNumber + '\', \'' + description + '\')" class="myButtons">' + i + '</button>';
      document.getElementById(myDropdown).insertAdjacentHTML('beforeend', button);
    }
  }

  function readFile(path, myDropdown, buttonNumber, description, description1, input) {
    document.getElementById(myDropdown).classList.toggle("show");

    var line = '<input type="text" placeholder="Search ' + description1 + '" id="' + input + '" onkeyup="filterFunction(\'' + myDropdown + '\', \'' + input + '\')">';
    document.getElementById(myDropdown).insertAdjacentHTML('beforeend', line);

    var lines;

    fetch(path)
      .then(response => response.text())
      .then(contents => {
        lines = contents.split('\n');
      })
      .catch(error => {
        console.error('Error finding file', error);
      });

    for (var i = 0; i < lines.length; i++) {
      // Process each line of the file
    }
  }

  // End of $(document).ready()
});
