let accordions = document.getElementsByClassName("sss-title");

for (let i = 0; i < accordions.length; i++) {
  accordions[i].addEventListener("click", function () {
    // Diğer tüm akordiyonları kapat
    closeAllAccordions(accordions, this);

    // İkonu güncelle
    updateIcon(this);

    // Açılıp kapanma işlemini gerçekleştir
    toggleAccordionContent(this);
  });
}

function closeAllAccordions(accordions, currentAccordion) {
  for (let i = 0; i < accordions.length; i++) {
    // Şu anki akordiyon dışındakileri kapat
    if (accordions[i] !== currentAccordion) {
      let content = accordions[i].nextElementSibling;
      accordions[i].childNodes[1].classList.remove("fa-times");
      accordions[i].childNodes[1].classList.add("fa-plus");
      content.style.maxHeight = null;
    }
  }
}

function updateIcon(accordion) {
  if (accordion.childNodes[1].classList.contains("fa-plus")) {
    accordion.childNodes[1].classList.remove("fa-plus");
    accordion.childNodes[1].classList.add("fa-times");
  } else {
    accordion.childNodes[1].classList.remove("fa-times");
    accordion.childNodes[1].classList.add("fa-plus");
  }
}

function toggleAccordionContent(accordion) {
  let content = accordion.nextElementSibling;
  if (content.style.maxHeight) {
    content.style.maxHeight = null;
  } else {
    content.style.maxHeight = content.scrollHeight + "px";
  }
}
