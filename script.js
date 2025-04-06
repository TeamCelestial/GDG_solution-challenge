// script.js - JS for API Calls

async function predictText(text) {
    const response = await fetch("/predict/text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });
    const data = await response.json();
    return data.prediction;
}

async function predictImage(image) {
    const response = await fetch("/predict/image", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ image: image })
    });
    const data = await response.json();
    return data.predictions;
}

async function predictSpeech(audio) {
    const response = await fetch("/predict/speech", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ audio: audio })
    });
    const data = await response.json();
    return data.prediction;
}
