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
            const probabilityPercentage = (prediction.probability * 100).toFixed(2);
            resultDiv.innerHTML += `<p>${prediction.label}: ${probabilityPercentage}%</p>`;
        });
    })
    .catch(error => console.error(('Error:', error)));
}
