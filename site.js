/* jshint esversion:6 */

const h1 = document.getElementById("loc");
const ul = document.getElementById("list");

const req = new XMLHttpRequest();
req.open("GET", "/tree.json", false);
req.send(null);

/**
 * @type {Map<String, Array<String>>}
 */
const json = JSON.parse(req.responseText);

/**
 * @type {Array<String>}
 */
const filesAndFolders = json["./" + window.location.pathname.replace(/\//g, " ").trim().replace(/ /g, "/")];

for (let i = 0; i < filesAndFolders.length; i++) {
    /**
     * @type {String}
     */
    const thing = filesAndFolders[i];

    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = thing;
    a.innerHTML = thing;
    li.appendChild(a);
    ul.appendChild(li);
}

h1.innerHTML = "Index of " + window.location.pathname;