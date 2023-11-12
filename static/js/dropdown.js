// li 요소를 선택합니다.
const popLi = document.querySelector(".pic-filter__pop");
const myLi = document.querySelector(".pic-filter__my");

// 드롭다운 리스트를 선택합니다.
const popDropdown = popLi.querySelector(".dropdown");
const myDropdown = myLi.querySelector(".dropdown");

// 드롭다운을 토글하는 함수를 정의합니다.
function toggleDropdown(dropdown) {
  dropdown.classList.toggle("show");
}

// 이벤트 리스너를 추가합니다.
popLi.addEventListener("click", () => toggleDropdown(popDropdown));
myLi.addEventListener("click", () => toggleDropdown(myDropdown));

// 문서의 다른 영역을 클릭하면 드롭다운이 닫히도록 합니다.
document.addEventListener("click", (event) => {
  if (!event.target.closest(".pic-filter__ul")) {
    popDropdown.classList.remove("show");
    myDropdown.classList.remove("show");
  }
});
