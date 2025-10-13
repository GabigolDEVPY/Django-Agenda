document.getElementById('userForm').onsubmit = async e => {
  e.preventDefault();
  try {
    const r = await fetch('/users-json');
    console.log(await r.json());
  } catch (err) {
    console.error(err);
  }
};



