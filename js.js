let anoNascimento = "Qual é o seu ano de nascimento?";

let anoAtual = new Date().getFullYear();

let idade = anoAtual - parseInt(anoNascimento);

alert("Sua idade é: " + idade + " anos.");