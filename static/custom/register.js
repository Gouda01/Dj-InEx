const usernameField=document.querySelector('#usernameField')
const feedbackArea=document.querySelector('.invalid_feedback')

const emailField=document.querySelector('#emailField')
const emailFeedbackArea=document.querySelector('.emailFeedbackArea')

const usernameSuccessOutput=document.querySelector('.usernameSuccessOutput')


emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailFeedbackArea.computedStyleMap.display="none";

    if(emailVal.length>0){
        fetch("/authentication/validate-email", {
        body: JSON.stringify({email:emailVal}),
        method:"POST",
    })
    .then(res=>res.json())
    .then((data) => {
        if (data.email_error){
            emailField.classList.add("is-invalid");
            emailFeedbackArea.computedStyleMap.display="block";
            emailFeedbackArea.innerHTML=`<p>${data.email_error}</p>`;
        }
    });
    }
});

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameSuccessOutput.style.display = "block";
    usernameSuccessOutput.textContent = `Checking ${usernameVal}`;

    usernameField.classList.remove("is-invalid");
    feedbackArea.computedStyleMap.display="none";

    if(usernameVal.length>0){
        fetch("/authentication/validate-username", {
        body: JSON.stringify({username:usernameVal}),
        method:"POST",
    })
    .then(res=>res.json())
    .then((data) => {
        usernameSuccessOutput.style.display = "none";
        if (data.username_error){
            usernameField.classList.add("is-invalid");
            feedbackArea.computedStyleMap.display="block";
            feedbackArea.innerHTML=`<p>${data.username_error}</p>`;
        }
    });
    }
});