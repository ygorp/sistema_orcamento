document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault()

    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value

    const data = {
        email: email,
        senha: senha
    }

    fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if(result.sucess) {
            window.location.href = "home/"
        } else {
            console.log("Login falhou", result.message)
        }
    })
    .catch(error => console.error("Erro", error))
})