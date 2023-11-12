const workBtnContainer = document.querySelector(".work__categories");
const projectContainer = document.querySelector(".work__projects");
const projects = document.querySelectorAll(".project");
const button = document.querySelector(".category__button");

workBtnContainer.addEventListener("click", (e) => {
  const filter = e.target.dataset.filter || e.target.parentNode.dataset.filter;
  if (filter == null) {
    return;
  }
  console.log(projects);

  // Remove selection from the previous item and select the new one
  const active = document.querySelector(".category__btn.selected");

  active.classList.remove("selected");
  const target =
    e.target.nodeName === "BUTTON" ? e.target : e.target.parentNode;
  target.classList.add("selected");

  projectContainer.classList.add("anim-out");
  projects.forEach((v) => {
    if (filter === v.dataset.type) {
      v.classList.remove("invisible");
    } else {
      v.classList.add("invisible");
    }
  });

  setTimeout(() => {
    projectContainer.classList.remove("anim-out");
  }, 300);
});

// active가 될경우
