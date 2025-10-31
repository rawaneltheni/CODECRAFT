document.addEventListener('DOMContentLoaded', () => {
  const checkPasswordBtn = document.getElementById('checkPassword');
  const password = document.getElementById('password');
  const result = document.getElementById('result');

  // Interactive background - mouse glow
  document.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth) * 100;
    const y = (e.clientY / window.innerHeight) * 100;
    document.body.style.setProperty('--x', `${x}%`);
    document.body.style.setProperty('--y', `${y}%`);
  });

  // Function to evaluate password strength
  const evaluatePassword = () => {
    let length = false, upperCase = false, lowerCase = false, num = false, specialChars = false;
    const pass = password.value;
    let passStrength = 0;

    if (pass.length >= 8) { passStrength++; length = true; }
    if (/[A-Z]/.test(pass)) { passStrength++; upperCase = true; }
    if (/[a-z]/.test(pass)) { passStrength++; lowerCase = true; }
    if (/[0-9]/.test(pass)) { passStrength++; num = true; }
    if (/[^A-Za-z0-9]/.test(pass)) { passStrength++; specialChars = true; }

    const showCheck = (condition) => condition 
      ? "<span style='color:green'>✅</span>" 
      : "<span style='color:red'>❌</span>";

    if (pass.length === 0) {
      result.innerHTML = ""; // Clear when empty
      return;
    }

    result.innerHTML = `
      <strong>Password check results:</strong><br><br>
      Length (≥8): ${showCheck(length)} <br>
      Uppercase letter: ${showCheck(upperCase)} <br>
      Lowercase letter: ${showCheck(lowerCase)} <br>
      Number: ${showCheck(num)} <br>
      Special character: ${showCheck(specialChars)} <br><br>
      <strong>Strength score:</strong> ${passStrength}/5
    `;

    let feedback = "";
    if (passStrength <= 2) feedback = "⚠️ Weak password";
    else if (passStrength === 3 || passStrength === 4) feedback = "💪 Good password";
    else feedback = "🔥 Very strong password!";

    result.innerHTML += `<br><br><strong>${feedback}</strong>`;
  };

  // Update dynamically while typing
  password.addEventListener('input', evaluatePassword);

});
