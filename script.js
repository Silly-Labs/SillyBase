import { execSync } from 'child_process'
const execSync = require('child_process').execSync;

// just playing around with stuff
var query = document.getElementByID("test").value;
const try_out = document.createElement('button')

try_out.innerText = 'run the code';
try_out.addEventListener('click', () => {
  const output = execSync('make sillybase', { encoding: 'utf-8' });
  alert(output);
})
