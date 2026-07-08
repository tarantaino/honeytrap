async function fetchAttacks() {
    try {
        const response = await fetch('/api/attacks');
        const data = await response.json();

        const tableBody = document.getElementById('attack-table-body');
        tableBody.innerHTML = "";

        data.forEach(attack => {

            const row = document.createElement('tr');


            const tdId = document.createElement('td');
            const tdTimestamp = document.createElement('td');
            const tdIp = document.createElement('td');
            const tdUsername = document.createElement('td');
            const tdPassword = document.createElement('td');

            //using textContext insted of innerHTML for better security
            tdId.textContent = attack.id;
            tdTimestamp.textContent = attack.timestamp;
            tdIp.textContent = attack.ip_address;


            tdUsername.textContent = attack.username;
            tdUsername.style.color = "yellow";
            tdUsername.style.fontWeight = "bold";

            tdPassword.textContent = attack.password;
            tdPassword.style.color = "red";
            tdPassword.style.fontWeight = "bold";


            row.appendChild(tdId);
            row.appendChild(tdTimestamp);
            row.appendChild(tdIp);
            row.appendChild(tdUsername);
            row.appendChild(tdPassword);


            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
fetchAttacks();
setInterval(fetchAttacks, 5000); //loads data once the page is opened and then every 5 secs