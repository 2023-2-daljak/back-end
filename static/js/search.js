// 버튼 요소들을 선택합니다.
const buttons = document.querySelectorAll(".pic-filter__button");

// 각 버튼에 클릭 이벤트 리스너를 추가합니다.
buttons.forEach((button) => {
  button.addEventListener("click", function (event) {
    // 클릭한 버튼의 data-query 값을 가져옵니다.
    const query = button.dataset.query;

    // 검색어를 URL에 추가하여 검색 페이지로 이동합니다.
    window.location.href = "/search/?city=" + query;
  });
});
