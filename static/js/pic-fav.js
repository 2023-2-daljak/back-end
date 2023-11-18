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

// 편집 아이콘에 대한 클릭 이벤트 처리
document.getElementById("editIcon").addEventListener("click", function () {
  // 특정 URL로 이동
  window.location.href = "{% url 'product:edit' product.pk %}";
});

// 삭제 아이콘에 대한 클릭 이벤트 처리
document.getElementById("deleteIcon").addEventListener("click", function () {
  // 특정 URL로 이동
  window.location.href = "{% url 'product:delete' product.pk %}";
});

// 삭제 아이콘에 대한 클릭 이벤트 처리
document.getElementById("messageIcon").addEventListener("click", function () {
  // 특정 URL로 이동
  console.log("hello");
  window.location.href = "{% url 'conversations:detail' product.pk %}";
});

document.getElementById("favIcon").addEventListener("click", function () {
  // 특정 URL로 이동
  console.log("hello");
  window.location.href = "{% url 'lists:toggle_room' product.id %}";
});

document.getElementById("favsIcon").addEventListener("click", function () {
  // 특정 URL로 이동
  console.log("hello");
  window.location.href = "{% url 'lists:toggle_room' product.id %}";
});

// DOM이 준비되면 실행될 함수
document.addEventListener("DOMContentLoaded", function () {
  // 첫 번째 아이콘을 선택합니다.
  const favsIcon1 = document.getElementById("favsIcon1");

  // 클릭 이벤트 리스너 등록
  favsIcon1.addEventListener("click", function () {
    // active 클래스를 토글
    if (favsIcon1.classList.contains("active")) {
      favsIcon1.classList.remove("active");
    } else {
      favsIcon1.classList.add("active");
    }
  });
});
