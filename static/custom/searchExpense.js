const searchField = document.querySelector('#searchField');

const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const paginateContent = document.querySelector('.paginate-content');
const tbodyOutput = document.querySelector('.output-table-body');

tableOutput.style.display ="none";

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0) {
        paginateContent.style.display ="none";
        tbodyOutput.innerHTML = "";


        fetch("/expenses/search-expenses", {
            body: JSON.stringify({searchText:searchValue}),
            method:"POST",
        })
        .then((res) => res.json())
        .then((data) => {
            tableOutput.style.display ="block";
            appTable.style.display ="none";

            if (data.length===0) {
                tableOutput.innerHTML = "No results found"
            }else {
                    const i = 1;
                    data.forEach((item) =>
                    tbodyOutput.innerHTML += `
                     <tr>
                        <td>${i}</td>
                        <td>${item.amount}</td>
                        <td>${item.category}</td>
                        <td>${item.description}</td>
                        <td>${item.date}</td>
                        <td></td>
                    </tr>`
                    
                                  
                )}
        });
    }else {
        tableOutput.style.display ="none";
        appTable.style.display ="block";
        paginateContent.style.display ="block";
    }
})