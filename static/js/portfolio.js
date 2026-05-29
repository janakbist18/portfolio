const themeToggle = document.getElementById("themeToggle");
const loader = document.getElementById("page-loader");

const setTheme = (mode) => {
  document.documentElement.setAttribute("data-theme", mode);
  localStorage.setItem("portfolio-theme", mode);
  if (themeToggle) {
    themeToggle.setAttribute(
      "aria-label",
      mode === "light" ? "Switch to dark mode" : "Switch to light mode",
    );
  }
};

const savedTheme = localStorage.getItem("portfolio-theme") || "light";
setTheme(savedTheme);

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");
    setTheme(current === "light" ? "dark" : "light");
  });
}

window.addEventListener("load", () => {
  if (loader) {
    loader.classList.add("hidden");
  }
  if (window.AOS) {
    AOS.init({ duration: 800, once: true, offset: 60 });
  }
});
