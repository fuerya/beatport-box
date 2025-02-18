function getCurrentTrack() {
    let trackElement = document.querySelector('.Player-style__TrackName-sc-8d683075-5');
    let mixElement = document.querySelector('.Player-style__MixName-sc-8d683075-4');

    if (trackElement && mixElement) {
        let trackTitle = trackElement.innerText.trim();
        let mixTitle = mixElement.innerText.trim();
        console.log(`Now Playing: ${trackTitle} (${mixTitle})`);
    } else {
        console.log("no song");
    }
}

// Run the function every 5 seconds
setInterval(getCurrentTrack, 1000);
