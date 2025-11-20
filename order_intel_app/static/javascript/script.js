// const cursor = document.querySelector('.cursor');

// document.addEventListener('mousemove', e => {
//   cursor.style.left = e.pageX + 'px';
//   cursor.style.top = e.pageY + 'px';
// });

// Optional smoother infinite scroll
const track = document.querySelector('.carousel-track');
if (track) {
  const clone = track.cloneNode(true);
  track.parentElement.appendChild(clone);
}