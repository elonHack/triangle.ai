const closeForm = document.getElementById('closeForm');
const signup = document.getElementById('signup'); // Swap this line
const login = document.getElementById('login'); // with this line
const signButton = document.getElementById('signButton');
const LoginForm = document.getElementById('loginForm');
const signForm = document.getElementById('signForm');
const closeForm2 = document.getElementById('closeForm2');

LoginForm.addEventListener('click', () => {
    signup.style.display = 'block';
    login.style.display = 'none';
  });
  
  signForm.addEventListener('click', () => {
    signup.style.display = 'block';
    login.style.display = 'none';
  });