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
