document.getElementById("cadastroForm").addEventListener("submit", function(event) {
    event.preventDefault()

    const nome = document.getElementById("nome").value
    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value

    const data = {
        nome: nome,
        email: email,
        senha: senha
    }

    fetch("http://localhost:8000/cadastro", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
        window.location.href = "login/";
    })
    .catch(error => console.error("Error", error))
})