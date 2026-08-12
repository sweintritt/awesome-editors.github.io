let mode = "light";

function onLoad() {
    toggleLight();
    createTable();
}

function createTable() {
    const optionalColumns1 = new Set(["modes", "ai", "lsp", "plugins", "first release"])
    const optionalColumns2 = new Set(["written in", "gui or terminal", "latest release", "license"])
    const table = document.createElement("table");
    const tableHead = document.createElement("thead");
    const tableBody = document.createElement("tbody");

    // Append the table head and body to table
    table.appendChild(tableHead);
    table.appendChild(tableBody);

    // Creating table head
    let row = tableHead.insertRow();
    Object.keys(data[0]).forEach((key) => {
        if (key != "link") {
            let th = document.createElement("th");
            th.textContent = key.toUpperCase();
            if (optionalColumns1.has(key)) {
                th.classList.add("optional1");
            } else if (optionalColumns2.has(key)) {
                th.classList.add("optional2");
            }
            row.appendChild(th);
        }
    });

    // Creating table body
    data.forEach((item) => {
        let row = tableBody.insertRow();
        Object.keys(item).forEach((key) => {
            if (key !== 'link') {
                let cell = row.insertCell();
                let value = item[key];
                if (key === "name") {
                    let a = document.createElement("a");
                    a.href = item["link"];
                    a.target = "_blank";
                    a.title = "Link to project"
                    a.appendChild(document.createTextNode(value));
                    cell.appendChild(a);
                } else if (key === "repository") {
                    let a = document.createElement("a");
                    a.href = value;
                    a.target = "_blank";
                    a.title = "Link to repository"
                    a.appendChild(document.createTextNode("repo"));
                    cell.appendChild(a);
                } else {
                    cell.textContent = value;
                    if (optionalColumns1.has(key)) {
                        cell.classList.add("optional1");
                    } else if (optionalColumns2.has(key)) {
                        cell.classList.add("optional2");
                    }
                }
            }
        });
    });

    document.getElementById("data").replaceChildren();
    document.getElementById("data").appendChild(table);
}

function filter() {
    let input = document.getElementById("search");
    let filter = input.value.toLowerCase();
    let table = document.getElementById("data");
    let tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        let tds = tr[i].getElementsByTagName("td");
        if (tds.length > 0) {
            let value = getLineText(tds);
            if (value.includes(filter)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function getLineText(tds) {
    let result = "";
    for (let i = 0; i < tds.length; i++) {
        result += tds[i].textContent || td[i].innerText;
    }
    return result.toLowerCase();
}

function toggleLight() {
    let button = document.getElementById("lightswitch");

    if (mode === "light") {
        document.documentElement.classList.remove("light");
        document.documentElement.classList.add("dark");
        mode = "dark";
        button.innerText = "light [ ]";
    } else if (mode === "dark") {
        document.documentElement.classList.remove("dark");
        document.documentElement.classList.add("light");
        mode = "light";
        button.innerText = "light [x]";
    }
}