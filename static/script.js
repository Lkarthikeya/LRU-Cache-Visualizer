function renderCache(data) {
    const cacheDiv = document.getElementById("cache");
    cacheDiv.innerHTML = "";

    data.forEach(item => {
        const div = document.createElement("div");
        div.className = "cache-box";
        div.innerText = `${item[0]} : ${item[1]}`;
        cacheDiv.appendChild(div);
    });
}

function put() {
    const key = document.getElementById("key").value;
    const value = document.getElementById("value").value;

    fetch('/put', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ key, value })
    })
    .then(res => res.json())
    .then(data => renderCache(data));
}

function get() {
    const key = document.getElementById("key").value;

    fetch('/get', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ key })
    })
    .then(res => res.json())
    .then(data => {
        alert("Value: " + data.value);
        renderCache(data.cache);
    });
}