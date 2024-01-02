document.addEventListener('DOMContentLoaded', function() {
  const generateBtn = document.getElementById('generateBtn');
  const passwordDisplay = document.getElementById('passwordDisplay');

  if (generateBtn && passwordDisplay) {
      generateBtn.addEventListener('click', generatePassword);
  }

  function getFormValues() {
      const form = document.getElementById('passwordForm');
      return {
          type: form.elements['type'].value,
          length: form.elements['pwLength'].value,
          numbers: form.elements['numbers'].checked,
          symbols: form.elements['symbols'].checked
      };
  }

  function displayPassword(password) {
      passwordDisplay.textContent = `Generated Password: ${password}`;
  }

  function generatePassword() {
      const { type, length, numbers, symbols } = getFormValues();
      const url = 'http://127.0.0.1:5000/generate';
      fetch(url, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({
              type,
              length,
              numbers,
              symbols,
          }),
      })
          .then(response => {
              if (!response.ok) {
                  throw new Error(`HTTP error! Status: ${response.status}`);
              }
              return response.json();
          })
          .then(data => displayPassword(data.password))
          .catch(error => console.error('Error:', error));
  }
});
