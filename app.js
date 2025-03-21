async function fetchAPOD() {
    const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${CONFIG.NASA_API_KEY}`;
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        displayAPOD(data);
    } catch (error) {
        console.error('Error fetching the APOD:', error);
    }
}

function displayAPOD(data) {
    const titleElement = document.getElementById('title');
    const imageElement = document.getElementById('image');
    const descriptionElement = document.getElementById('description');

    titleElement.textContent = data.title;
    imageElement.src = data.url;
    descriptionElement.textContent = data.explanation;
}

fetchAPOD();