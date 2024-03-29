async function loginUser() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = new URLSearchParams();
    data.append('username', email);
    data.append('password', password);

    try {
        const response = await fetch('/auth/jwt/login', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: data,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Handle successful login, for example, redirect to a dashboard
        window.location.href = '/auth/jwt/dashboard';

    } catch (error) {
        console.error('Error during login:', error);

        if (error.response) {
            console.error('Response data:', await error.response.json());
        } else if (error.request) {
            console.error('No response received. Request details:', error.request);
        } else {
            console.error('Error details:', error.message);
        }

        // Handle login error, for example, display an alert to the user
        alert('Login failed. Please try again.');
    }
}
