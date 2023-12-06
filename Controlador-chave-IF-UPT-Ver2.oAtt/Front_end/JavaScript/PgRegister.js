// Importando o Axios
import axios from 'axios';

new Vue({
    el: '#app',
    data: {
        username: '',
        email: '',
        password: '',
        errorMessage: ''
    },
    methods: {
        async register() {
            try {
                const response = await axios.post('http://127.0.0.1:8000/register', {
                    username: this.username,
                    email: this.email,
                    password: this.password
                });

                if (response.data.success) {
                    alert('Registration successful');
                } else {
                    this.errorMessage = response.data.message;
                }
            } catch (error) {
                console.error('Error:', error);
                this.errorMessage = 'An error occurred during registration';
            }
        }
    }
});