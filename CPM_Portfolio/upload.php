<?php
if (isset($_FILES['pdfFile'])) {
    $targetDirectory = 'uploads/';  // Set the directory where you want to store uploaded files
    $targetFile = $targetDirectory . basename($_FILES['pdfFile']['name']);

    if (move_uploaded_file($_FILES['pdfFile']['tmp_name'], $targetFile)) {
        echo "File uploaded successfully.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
