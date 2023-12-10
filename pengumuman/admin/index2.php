<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload with Tailwind CSS</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
</head>
<body class="bg-gray-200 p-8">

    <div class="max-w-md mx-auto bg-white p-6 rounded-md shadow-md">
        <h2 class="text-2xl font-semibold mb-4">File Upload</h2>

        <?php
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // Handle file upload logic here
            $targetDir = "/var/www/html/uploads/";
            $targetFile = $targetDir . basename($_FILES["file"]["name"]);

            if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
                $url = "http://127.0.0.1:8080/";
                echo $url;
                echo '<p class="text-green-600">File uploaded successfully!</p>';
            } else {
                echo '<p class="text-red-600">Error uploading file.</p>';
            }
        }
        ?>

        <form action="" method="post" enctype="multipart/form-data">
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="file">
                    Choose a file
                </label>
                <input type="file" name="file" id="file" class="border rounded p-2 w-full">
            </div>

            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md">Upload</button>
        </form>
    </div>

</body>
</html>

