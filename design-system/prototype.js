/* UI-Army · prototype.js
   Lee ?theme=light|dark y ?device=web|tablet de la URL y los aplica a <html>.
   Así compare.html puede cambiar de modo sin duplicar prototipos.
   Uso: <script src="../../../design-system/prototype.js"></script> en el <head>. */
(function () {
  var p = new URLSearchParams(location.search);
  var root = document.documentElement;
  var theme = p.get("theme");
  var device = p.get("device");
  if (theme === "dark") root.setAttribute("data-theme", "dark");
  if (theme === "light") root.removeAttribute("data-theme");
  if (device === "tablet") root.setAttribute("data-device", "tablet");
  if (device === "web") root.removeAttribute("data-device");
})();
