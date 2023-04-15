// just playing around with stuff
var query = document.getElementByID("test").value;

const execSync = require('child_process').execSync;
// import { execSync } from 'child_process';  // replace ^ if using ES modules

const output = execSync('make sillybase', { encoding: 'utf-8' });  // the default is 'buffer'
alert(output);
