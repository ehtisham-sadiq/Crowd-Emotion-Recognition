// document.addEventListener('DOMContentLoaded', function () {
//     const fileInput = document.getElementById('file-input');
//     const resultsDiv = document.getElementById('results');
//     const uploadImageBtn = document.getElementById('upload-image-btn');
//     const uploadVideoBtn = document.getElementById('upload-video-btn');
//     const captureImageBtn = document.getElementById('capture-image-btn');
//     const captureVideoBtn = document.getElementById('capture-video-btn');
//     const displayResultsBtn = document.getElementById('display-results-btn');
//     const dashboardBtn = document.getElementById('dashboard-btn');

//     uploadImageBtn.addEventListener('click', () => {
//         fileInput.accept = 'image/*';
//         fileInput.click();
//     });

//     uploadVideoBtn.addEventListener('click', () => {
//         fileInput.accept = 'video/*';
//         fileInput.click();
//     });

//     captureImageBtn.addEventListener('click', () => {
//         captureMedia('image');
//     });

//     captureVideoBtn.addEventListener('click', () => {
//         captureMedia('video');
//     });

//     displayResultsBtn.addEventListener('click', () => {
//         displayResults();
//     });

//     dashboardBtn.addEventListener('click', () => {
//         window.location.href = 'dashboard.html';  // Update with actual dashboard URL
//     });

//     fileInput.addEventListener('change', (event) => {
//         const file = event.target.files[0];
//         if (file) {
//             const reader = new FileReader();
//             reader.onload = function(e) {
//                 resultsDiv.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image" style="max-width: 100%; height: auto;">`;
//             };
//             reader.readAsDataURL(file);
//         }
//     });

//     function captureMedia(type) {
//         if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//             const constraints = type === 'image' ? { video: true } : { video: { facingMode: 'environment' } };
//             navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
//                 const mediaElement = document.createElement(type);
//                 mediaElement.srcObject = stream;
//                 mediaElement.play();
//                 resultsDiv.innerHTML = '';
//                 resultsDiv.appendChild(mediaElement);
//             }).catch((error) => {
//                 console.error("Error accessing media devices.", error);
//             });
//         } else {
//             alert("Media devices are not supported in this browser.");
//         }
//     }

//     function displayResults() {
//         // Simulate detected emotion result
//         resultsDiv.innerHTML = '<h4>Detected Emotion: Happy</h4>';
//     }
// });

// document.addEventListener('DOMContentLoaded', function() {
//     const uploadImageButton = document.getElementById('upload-image-btn');
//     const uploadVideoButton = document.getElementById('upload-video-btn');
//     const captureImageButton = document.getElementById('capture-image-btn');
//     const captureVideoButton = document.getElementById('capture-video-btn');
//     const fileInput = document.getElementById('file-input');
//     const imageVideoPreview = document.getElementById('image-video-preview');
//     const displayResultsButton = document.getElementById('display-results-btn');
//     const dashboardButton = document.getElementById('dashboard-btn');
//     const resultsDiv = document.getElementById('results');
//     const emotionBarplot = document.getElementById('emotion-barplot');

//     // Function to handle file uploads
//     function handleFileUpload(event) {
//         const file = event.target.files[0];
//         if (file) {
//             const fileType = file.type;
//             const fileReader = new FileReader();

//             fileReader.onload = function(e) {
//                 const fileURL = e.target.result;
//                 displayFile(fileURL, fileType);
//             };

//             fileReader.readAsDataURL(file);
//         }
//     }

//     // Function to display the uploaded file
//     function displayFile(fileURL, fileType) {
//         imageVideoPreview.innerHTML = '';

//         if (fileType.startsWith('image/')) {
//             const img = document.createElement('img');
//             img.src = fileURL;
//             img.alt = 'Uploaded Image';
//             imageVideoPreview.appendChild(img);
//         } else if (fileType.startsWith('video/')) {
//             const video = document.createElement('video');
//             video.src = fileURL;
//             video.controls = true;
//             imageVideoPreview.appendChild(video);
//         }
//     }

//     // Event listeners for the buttons
//     uploadImageButton.addEventListener('click', function() {
//         fileInput.accept = 'image/*';
//         fileInput.click();
//     });

//     uploadVideoButton.addEventListener('click', function() {
//         fileInput.accept = 'video/*';
//         fileInput.click();
//     });

//     captureImageButton.addEventListener('click', function() {
//         alert('Capture Image functionality not yet implemented');
//         // Implement image capture functionality here
//     });

//     captureVideoButton.addEventListener('click', function() {
//         alert('Capture Video functionality not yet implemented');
//         // Implement video capture functionality here
//     });

//     fileInput.addEventListener('change', handleFileUpload);

//     // Display results on button click
//     displayResultsButton.addEventListener('click', function() {
//         // Replace with actual ML model integration
//         const detectedEmotion = 'Happy'; // Example emotion
//         const emotionScores = {
//             'Happy': 0.8,
//             'Sad': 0.1,
//             'Angry': 0.05,
//             'Surprised': 0.05
//         };

//         // Display detected emotion
//         resultsDiv.innerHTML = `<h4>Detected Emotion: ${detectedEmotion}</h4>`;

//         // Display emotion barplot
//         displayEmotionBarplot(emotionScores);
//     });

//     // Navigate to dashboard
//     dashboardButton.addEventListener('click', function() {
//         window.location.href = 'dashboard.html';
//     });

//     // Function to display the emotion barplot
//     function displayEmotionBarplot(emotionScores) {
//         const labels = Object.keys(emotionScores);
//         const data = Object.values(emotionScores);

//         const ctx = document.createElement('canvas');
//         emotionBarplot.innerHTML = '';
//         emotionBarplot.appendChild(ctx);

//         new Chart(ctx, {
//             type: 'bar',
//             data: {
//                 labels: labels,
//                 datasets: [{
//                     label: 'Emotion Scores',
//                     data: data,
//                     backgroundColor: [
//                         'rgba(75, 192, 192, 0.2)',
//                         'rgba(255, 99, 132, 0.2)',
//                         'rgba(255, 206, 86, 0.2)',
//                         'rgba(153, 102, 255, 0.2)'
//                     ],
//                     borderColor: [
//                         'rgba(75, 192, 192, 1)',
//                         'rgba(255, 99, 132, 1)',
//                         'rgba(255, 206, 86, 1)',
//                         'rgba(153, 102, 255, 1)'
//                     ],
//                     borderWidth: 1
//                 }]
//             },
//             options: {
//                 responsive: true,
//                 scales: {
//                     y: {
//                         beginAtZero: true
//                     }
//                 }
//             }
//         });
//     }
// });

document.addEventListener('DOMContentLoaded', function() {
    const uploadImageButton = document.getElementById('upload-image-btn');
    const uploadVideoButton = document.getElementById('upload-video-btn');
    const captureImageButton = document.getElementById('capture-image-btn');
    const captureVideoButton = document.getElementById('capture-video-btn');
    const fileInput = document.getElementById('file-input');
    const imageVideoPreview = document.getElementById('image-video-preview');
    const displayResultsButton = document.getElementById('display-results-btn');
    const dashboardButton = document.getElementById('dashboard-btn');
    const resultsDiv = document.getElementById('detected-emotion');
    const emotionBarplot = document.getElementById('emotion-barplot');

    // Function to handle file uploads
    function handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('http://localhost:8000/analyze-emotion/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                const detectedEmotion = data.dominant_emotion;
                const emotionScores = data.emotion_scores;

                // Display detected emotion
                resultsDiv.innerHTML = `Detected Emotion: ${detectedEmotion}`;

                // Display emotion barplot
                displayEmotionBarplot(emotionScores);
            })
            .catch(error => console.error('Error analyzing emotion:', error));
        }
    }

    // Function to display the emotion barplot
    function displayEmotionBarplot(emotionScores) {
        const labels = Object.keys(emotionScores);
        const data = Object.values(emotionScores);

        const ctx = document.createElement('canvas');
        emotionBarplot.innerHTML = '';
        emotionBarplot.appendChild(ctx);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Emotion Scores',
                    data: data,
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(153, 102, 255, 0.2)'
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(153, 102, 255, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Event listeners for the buttons
    uploadImageButton.addEventListener('click', function() {
        fileInput.accept = 'image/*';
        fileInput.click();
    });

    uploadVideoButton.addEventListener('click', function() {
        fileInput.accept = 'video/*';
        fileInput.click();
    });

    fileInput.addEventListener('change', handleFileUpload);

    // Navigate to dashboard
    dashboardButton.addEventListener('click', function() {
        window.location.href = 'dashboard.html';
    });

});

