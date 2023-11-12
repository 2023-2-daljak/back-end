const likeButtons = document.querySelectorAll(".work__icon");

likeButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const productId = button.getAttribute("data-product-id");

    fetch("/toggle_like/", {
      method: "POST",
      body: JSON.stringify({ product_id: productId }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken, // Django CSRF 토큰 설정
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.is_liked) {
          button.classList.add("liked");
        } else {
          button.classList.remove("liked");
        }
      });
  });
});
