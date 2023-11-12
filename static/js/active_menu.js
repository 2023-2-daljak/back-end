// DOM이 준비되면 실행될 함수
document.addEventListener("DOMContentLoaded", function () {
  // 모든 메뉴 아이템 요소를 가져옵니다.
  const menuItems = document.querySelectorAll(".header__menu__item");
  console.log(menuItems);
  // 현재 페이지 URL을 가져옵니다.
  const currentURL = window.location.href;
  console.log(currentURL);

  // 각 메뉴 아이템에 대한 클릭 이벤트 리스너를 등록합니다.
  menuItems.forEach(function (item, index) {
    // 초기 URL인 경우 첫 번째 메뉴 아이템에만 "active" 클래스를 추가합니다.
    if (currentURL === "http://127.0.0.1:8000/" && index === 0) {
      item.classList.add("active");
    } else if (currentURL === "http://127.0.0.1:8000/products" && index === 1) {
      console.log(item);
      item.classList.add("active");
    } else if (
      currentURL === "http://127.0.0.1:8000/users/login/" &&
      index === 3
    ) {
      console.log(item);
      item.classList.add("active");
    } else {
      // 다른 URL인 경우 나머지 메뉴 아이템에서는 "active" 클래스를 제거합니다.
      item.classList.remove("active");
    }

    // 클릭된 메뉴 아이템에 대한 클릭 이벤트 리스너를 등록합니다.
    item.addEventListener("click", function () {
      // 클릭된 메뉴 아이템에 "active" 클래스를 추가하고 나머지 메뉴 아이템에서 "active" 클래스를 제거합니다.
      menuItems.forEach(function (menuItem) {
        menuItem.classList.remove("active");
      });
      item.classList.add("active");
    });
  });
});
