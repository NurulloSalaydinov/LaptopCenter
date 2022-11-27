const addBtn = document.querySelector(".add-btn"),
  minusBtn = document.querySelector(".minus-btn"),
  addCart = document.querySelector("#AddCart"),
  changeHref = document.querySelector('.changeHref'),
  result = document.querySelector(".amount-result");

let a = 1;
let old_url = changeHref.attributes['href'].nodeValue



addBtn.addEventListener("click", () => {
  a++;
  result.textContent = a;
  x = a;
  changeHref.attributes['href'].nodeValue = old_url + x + '/';
  addCart.attributes['count'].nodeValue = a;
})

minusBtn.addEventListener("click", () => {
  if (a > 1) {
    a--;
    result.textContent = a;
    x = a;
    changeHref.attributes['href'].nodeValue = old_url + x + '/';
    addCart.attributes['count'].nodeValue = a;
  }
})