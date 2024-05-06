function classifyImage() {
    const fileInput = document.getElementById('imageInput');
    const resultDiv = document.getElementById('result');

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    fetch('/classify', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display classification result
        resultDiv.innerHTML = '';
        data.forEach(prediction => {
            resultDiv.innerHTML += `<p>${prediction.label}: ${prediction.probability}</p>`;
        });
    })
    .catch(error => console.error('Error:', error));
}
