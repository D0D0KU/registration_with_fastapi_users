async function registerUser() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = {
        "email": email,
        "password": password,
        "is_active": true,
        "is_superuser": false,
        "is_verified": false,
        "username": username,
        "role_id": 0
    };

    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Handle successful response, for example, redirect to a successful registration page
        window.location.href = '/auth/registration-success';

    } catch (error) {
        console.error('Error during registration:', error);
        // Handle error, for example, display an alert message to the user
        alert('An error occurred during registration. Please try again.');
    }
}
