document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('uploadedImage').src = e.target.result;
            document.getElementById('uploadedImage').style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});

document.getElementById('getClass').addEventListener('click', async function() {
    const imageClassDiv = document.getElementById('imageClass');
    const fileInput = document.getElementById('imageUpload');

    if (!fileInput.files.length) {
        imageClassDiv.innerText = "Please upload an image first.";
        return;
    }

    imageClassDiv.innerText = "Classifying...";

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);
    try {
        // Replace 'http://localhost:5000/classify' with your actual API endpoint
        const response = await fetch('/classify', {
            method: 'POST',
            body: formData
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        imageClassDiv.innerHTML = '';
        data.forEach(prediction => {
            const probabilityPercentage = (prediction.probability * 100).toFixed(2);
            imageClassDiv.innerHTML += `<p>${prediction.label}: ${probabilityPercentage}%</p>`;
        });
            console.log("Classification result:", data);
    } catch (error) {
        console.error('Error:', error);
        imageClassDiv.innerText = "An error occurred during classification.";
    }
});
