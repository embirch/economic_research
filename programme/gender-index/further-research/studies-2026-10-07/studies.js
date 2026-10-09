'use strict';
// Optional explanations supplement labels and the native chart-values disclosure.
const tooltip = document.createElement('div');
tooltip.className = 'tooltip';
tooltip.hidden = true;
tooltip.setAttribute('role', 'status');
document.body.appendChild(tooltip);
function show(mark, event) {
  tooltip.textContent = mark.getAttribute('aria-label');
  tooltip.hidden = false;
  const rect = mark.getBoundingClientRect();
  const x = event && Number.isFinite(event.clientX) ? event.clientX : rect.left;
  const y = event && Number.isFinite(event.clientY) ? event.clientY : rect.bottom;
  tooltip.style.left = Math.max(12, Math.min(x + 12, window.innerWidth - 325)) + 'px';
  tooltip.style.top = Math.max(12, Math.min(y + 12, window.innerHeight - tooltip.offsetHeight - 12)) + 'px';
}
document.querySelectorAll('.data-mark').forEach(mark => {
  mark.addEventListener('mouseenter', event => show(mark, event));
  mark.addEventListener('mousemove', event => show(mark, event));
  mark.addEventListener('mouseleave', () => tooltip.hidden = true);
  mark.addEventListener('focus', () => show(mark));
  mark.addEventListener('blur', () => tooltip.hidden = true);
});
document.addEventListener('keydown', event => {if (event.key === 'Escape') tooltip.hidden = true;});
