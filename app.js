/* =========================================
   KINDORI KINDERGARTEN – app.js
   ========================================= */

// ─── STICKY NAVBAR ───────────────────────
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// ─── HAMBURGER MENU ──────────────────────
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("navLinks");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  const spans = hamburger.querySelectorAll("span");
  if (navLinks.classList.contains("open")) {
    spans[0].style.transform = "rotate(45deg) translate(5px, 5px)";
    spans[1].style.opacity = "0";
    spans[2].style.transform = "rotate(-45deg) translate(5px, -5px)";
  } else {
    spans[0].style.transform = "";
    spans[1].style.opacity = "";
    spans[2].style.transform = "";
  }
});

// Close menu on link click
navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
    hamburger.querySelectorAll("span").forEach((s) => {
      s.style.transform = "";
      s.style.opacity = "";
    });
  });
});

// ─── ACTIVE NAV LINK ON SCROLL ───────────
const sections = document.querySelectorAll("section[id]");
const navItems = navLinks.querySelectorAll('a[href^="#"]');

const activateLink = () => {
  let current = "";
  sections.forEach((sec) => {
    const secTop = sec.offsetTop - navbar.offsetHeight - 60;
    if (window.scrollY >= secTop) current = sec.getAttribute("id");
  });
  navItems.forEach((link) => {
    link.classList.toggle(
      "active",
      link.getAttribute("href") === "#" + current,
    );
  });
};
window.addEventListener("scroll", activateLink, { passive: true });

// ─── SEARCH TOGGLE ───────────────────────
const searchToggle = document.getElementById("searchToggle");
const searchBar = document.getElementById("searchBar");
const searchInput = document.getElementById("searchInput");

searchToggle.addEventListener("click", () => {
  searchBar.classList.toggle("open");
  if (searchBar.classList.contains("open")) searchInput.focus();
});

document.getElementById("searchSubmit").addEventListener("click", () => {
  const query = searchInput.value.trim();
  if (query) alert(`Buscando: "${query}"`);
});
searchInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    const query = searchInput.value.trim();
    if (query) alert(`Buscando: "${query}"`);
  }
});

// ─── SCROLL REVEAL ───────────────────────
const revealElements = document.querySelectorAll(
  ".card, .blog-card, .class-card, .teacher-card, .guiding-image, .guiding-content, .enroll-inner, .hero-content",
);

revealElements.forEach((el) => el.classList.add("reveal"));

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 },
);

revealElements.forEach((el) => observer.observe(el));

// ─── SCROLL TO TOP ───────────────────────
const scrollTopBtn = document.getElementById("scrollTop");

window.addEventListener(
  "scroll",
  () => {
    scrollTopBtn.classList.toggle("visible", window.scrollY > 400);
  },
  { passive: true },
);

scrollTopBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

// ─── CARD HOVER RIPPLE ───────────────────
document
  .querySelectorAll(".card, .blog-card, .class-card, .teacher-card")
  .forEach((card) => {
    card.addEventListener("click", (e) => {
      const ripple = document.createElement("span");
      const rect = card.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;

      Object.assign(ripple.style, {
        position: "absolute",
        width: size + "px",
        height: size + "px",
        left: x + "px",
        top: y + "px",
        borderRadius: "50%",
        background: "rgba(255,255,255,.35)",
        transform: "scale(0)",
        animation: "rippleAnim .6s ease-out forwards",
        pointerEvents: "none",
      });

      card.style.position = "relative";
      card.style.overflow = "hidden";
      card.appendChild(ripple);
      setTimeout(() => ripple.remove(), 700);
    });
  });

// Inject ripple keyframe if not already injected
if (!document.getElementById("rippleStyle")) {
  const style = document.createElement("style");
  style.id = "rippleStyle";
  style.textContent = `@keyframes rippleAnim {
    to { transform: scale(2.5); opacity: 0; }
  }`;
  document.head.appendChild(style);
}
