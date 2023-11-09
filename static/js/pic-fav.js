const item = document.querySelector(".project__description");
const work__icon = document.querySelector(".work__icon");
const work = document.querySelector(".work");
const project = document.querySelector(".project");

project.addEventListener("click", (e) => {
  e.preventDefault();
});

const projectLinks = document.querySelectorAll(".project");

projectLinks.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    // 추가로 수행할 작업을 여기에 작성하세요.
  });
});

item.addEventListener("click", (e) => {
  print(item);
  e.preventDefault();
});

work__icon.addEventListener("click", function (e) {
  e.preventDefault();
});

const topHearts = document.querySelectorAll(".topHeart");
const bottomHearts = document.querySelectorAll(".bottomHeart");

topHearts.forEach((topHeart) => {
  topHeart.addEventListener("click", function (e) {
    e.preventDefault();
    topHeart.style.display = "none";
    // 해당 topHeart에 연결된 bottomHeart를 찾아서 보이도록 변경
    const relatedBottomHeart =
      topHeart.parentElement.querySelector(".bottomHeart");
    relatedBottomHeart.style.display = "block";
  });
});

bottomHearts.forEach((bottomHeart) => {
  bottomHeart.addEventListener("click", function (e) {
    e.preventDefault();
    bottomHeart.style.display = "none";
    // 해당 bottomHeart에 연결된 topHeart를 찾아서 보이도록 변경
    const relatedTopHeart =
      bottomHeart.parentElement.querySelector(".topHeart");
    relatedTopHeart.style.display = "block";
  });
});
