const form = document.getElementById("shorten-form");

const urlInput = document.getElementById("url-input");

const result = document.getElementById("result");

const shortUrl = document.getElementById("short-url");

const error = document.getElementById("error");


form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const originalUrl = urlInput.value;

    result.classList.add("hidden");
    error.classList.add("hidden");

    try {

        const response = await fetch(
            "/api/shorten",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    url: originalUrl
                })
            }
        );

        if (!response.ok) {
            throw new Error("Failed to shorten URL");
        }

        const data = await response.json();

        const fullShortUrl = window.location.origin + data.short_url;

        shortUrl.textContent = fullShortUrl;
        shortUrl.href = fullShortUrl;

        result.classList.remove("hidden");

    } catch (err) {

        error.textContent = err.message;

        error.classList.remove("hidden");

    }

});