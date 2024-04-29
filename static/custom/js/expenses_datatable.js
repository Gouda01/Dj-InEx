
window.load( async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/expenses/");
        const data = await response.json();
        console.log(data);

        

        
        
    } catch(ex) {
        alert(ex);
    }
});