const listExpenses = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/expenses/");
        const data = await response.json();

        let content = ``;

        data.expenses.forEach((expense, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${expense.amount}</td>
                    <td>${expense.description}</td>
                    <td>${expense.category}</td>
                    <td>${expense.date}</td>
                    <td></td>
                </tr>
            `;
        });
        
    } catch(ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await listExpenses();
});