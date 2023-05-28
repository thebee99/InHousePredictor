<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];

  // Set up the email parameters
  $to = 'contactmygroup7@gmail.com'; // Specify the recipient email address
  $subject = $_POST['image_id'];
  $headers = "From: $name <$email>";

  // Compose the email body
  $email_body = "Name: $name\n\nEmail: $email\nSubject: $subject\nMessage:\n$message";

  // Send the email
  if (mail($to, $subject, $email_body, $headers)) {
    echo 'Email sent successfully!';
  } else {
    echo 'Oops! Something went wrong.';
  }
}
?>