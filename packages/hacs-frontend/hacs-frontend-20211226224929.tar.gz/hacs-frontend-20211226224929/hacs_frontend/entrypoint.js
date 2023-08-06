
try {
  new Function("import('/hacsfiles/frontend/main-146c650c.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-146c650c.js';
  el.type = 'module';
  document.body.appendChild(el);
}
  