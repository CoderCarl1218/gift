document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a[data-load-content]');
    const soundToggle = document.getElementById('sound-toggle');
    const audio = document.getElementById('snowfall-sound');
    
    // Load sound state
    soundToggle.addEventListener('click', () => {
        if (audio.muted) {
            audio.muted = false; // Unmute
            soundToggle.innerHTML = '🔊'; // Change icon to sound on
        } else {
            audio.muted = true; // Mute
            soundToggle.innerHTML = '🔇'; // Change icon to sound off
        }
    });

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent default link behavior
            const url = this.getAttribute('href'); // Get the URL from the link
            
            // Fetch the content from the URL
            fetch(url)
                .then(response => {
                    if (!response.ok) throw new Error('Network response was not ok');
                    return response.text();
                })
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const newContent = doc.querySelector('#main-content'); // Grab the new content
                    document.querySelector('#main-content').innerHTML = newContent.innerHTML; // Update the main content area

                    // Reinitialize the audio button after new content is loaded
                    initAudioToggle();
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        });
    });

    function initAudioToggle() {
        soundToggle.addEventListener('click', () => {
            if (audio.muted) {
                audio.muted = false; // Unmute
                soundToggle.innerHTML = '🔊'; // Change icon to sound on
            } else {
                audio.muted = true; // Mute
                soundToggle.innerHTML = '🔇'; // Change icon to sound off
            }
        });
    }

    // Initial audio button setup
    initAudioToggle();
});

document.addEventListener("DOMContentLoaded", function () {
    const currentDate = new Date();
    const month = currentDate.getMonth(); // 0-11 (0 = January, 11 = December)
    const snowfallSound = document.getElementById('snowfall-sound');
    
    // Start with muted sound
    snowfallSound.muted = true;

    // Function to toggle sound
    function toggleSound() {
        snowfallSound.muted = !snowfallSound.muted; // Toggle mute
        const soundIcon = document.getElementById('sound-icon');
        soundIcon.textContent = snowfallSound.muted ? '🔇' : '🔊'; // Change icon based on mute state
    }

    // Add event listener to the sound toggle button
    document.getElementById('sound-toggle').addEventListener('click', toggleSound);

    // Play sound and start snowfall automatically in December
    if (month === 8) { // If it's December
        snowfallSound.muted = false; // Unmute
        snowfallSound.loop = true; // Loop the sound
        snowfallSound.play(); // Play snowfall sound
        createSnowfall(); // Start the snowfall effect
    }

    function createSnowfall() {
        const snowflakesCount = 50; // Number of snowflakes
        const snowflakeContainer = document.createElement('div');
        snowflakeContainer.classList.add('snowflake-container');
        document.body.appendChild(snowflakeContainer);
    
        // Array of emoticons to use
        const emoticons = ['❄️', '☃️', '🎅', '🎄'];
    
        for (let i = 0; i < snowflakesCount; i++) {
            const snowflake = document.createElement('div');
            snowflake.classList.add('snowflake');
    
            // Randomly select an emoticon
            const randomEmoticon = emoticons[Math.floor(Math.random() * emoticons.length)];
            snowflake.innerHTML = randomEmoticon;
    
            snowflakeContainer.appendChild(snowflake);
            animateSnowflake(snowflake);
        }
    }

    function animateSnowflake(snowflake) {
        snowflake.style.position = 'absolute';
        snowflake.style.top = '-10px'; // Start above the viewport
        snowflake.style.left = Math.random() * window.innerWidth + 'px'; // Random horizontal position
        snowflake.style.opacity = Math.random(); // Random opacity

        const fallDuration = Math.random() * 5 + 5; // Random fall duration between 5 and 10 seconds
        const translateX = Math.random() * 100 - 50; // Random horizontal drift

        snowflake.animate([ 
            { transform: `translateY(0) translateX(0)`, opacity: 1 },
            { transform: `translateY(${window.innerHeight}px) translateX(${translateX}px)`, opacity: 0 }
        ], {
            duration: fallDuration * 1200,
            easing: "linear",
            iterations: Infinity
        });
    }
});


// Modal and dropdown functions
function toggleModal(modalId) {
    document.getElementById(modalId).classList.toggle('hidden');
}

function toggleDropdown() {
    document.getElementById('dropdownMenu').classList.toggle('hidden');
}