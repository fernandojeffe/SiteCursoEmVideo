function validoEmail(){
    const emailInput = document.getElementById("email-input");
    const emailErroMsn = document.getElementById("emailErro-Msn");
    const notificaBtn = document.getElementById("notifica-btn");
    const email = emailInput.value;
    const emailV = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


    if (!emailV.test(email)){
      emailInput.style.borderColor = "hsl(354, 100%, 66%)";
      emailInput.style.background = "hsl(5, 100%, 95%)";
      emailErroMsn.style.display = "block";
      notificaBtn.disabled = true;
    } else {
      emailInput.style.borderColor = "";
      emailErroMsn.style.display = "none";
      notificaBtn.disabled = false;
    }
  }

  function limpar(){
    document.getElementById("email-input").valeu = "";
  }

  function success(){
    const emailInput =document.getElementById("email-input")
    const notificaBtn = document.getElementById("notifica-btn");
    const puxarPgn = 
  }
  