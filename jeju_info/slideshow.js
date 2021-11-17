//이미지 선택
var slides = document.querySelectorAll(".slides img");
let current= 0;
let next = document.getElementById("next");
let prev = document.getElementById("prev");

showSlides(current);
next.onclick = nextSlide;
prev.onclick = prevslide;

function showSlides(n){
    for(let i=0; i<slides.length; i++){
        slides[i].style.display = "none";
    }
    slides[n].style.display = "block";
}

function nextSlide(){
    if(current < slides.length -1)
    current += 1;
    else
    current = 0;
    showSlides(current);
}

function prevslide(){
    if(current > 0)
    current -= 1;
    else
    current = slides.length -1 ;
    showSlides(current);
}