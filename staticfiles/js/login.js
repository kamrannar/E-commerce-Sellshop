var login_form = document.getElementById('login_form')

login_form.addEventListener('submit', async function (event) {

    let postData = { 
        username: login_form.username.value, 
        password:login_form.password.value
    };

    let response = await fetch('http://localhost:8000/api/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            
        },
        body: JSON.stringify(postData)
    }
    )
    if(response.ok){
        data= await response.json();
        access=window.localStorage.setItem('access',data.access)
        refresh = window.localStorage.setItem('refresh',data.refresh)
    }   
})
