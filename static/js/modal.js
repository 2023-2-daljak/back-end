const openButton = document.querySelector(".pic-filter__filterbtn");
const modal = document.querySelector(".modal");
const close = document.querySelector("#close-btn");

const openModal = () => {
  modal.classList.remove("hidden");
};

const closeModal = () => {
  modal.classList.add("hidden");
};

openButton.addEventListener("click", (e) => {
  console.log("hello");
  modal.classList.remove("hidden");
});

close.addEventListener("click", (e) => {
  console.log("이 씨발롬아");
  modal.classList.add("hidden");
});

picContainer.addEventListener("click", console.log("hello"));

document.querySelector(".modal-button__x").addEventListener("click", (e) => {
  console.log("이 새끼야");
  document.querySelectorAll(".modal input").forEach((v) => {
    v.checked = false;
  });
});
