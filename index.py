
<html>
<head>
</head>
<body>
    <div id="container">
        <header>
            <div id="logo">
                <h1>Dream Jeju</h1>
            </div>
            <nav>
                <ul id="topMenu">
                    <li><a href="./index.html">메인 화면</a></li>
                    <li><a href="travel.html">제주 여행</a></li>
                    <li><a href="product.html">레드향 소개</a></li>
                    <li><a href="#">갤러리</a></li>
                    <li><a href="#">문의하기</a></li>
                </ul>
            </nav>
        </header>
       
            <section id="slideShow">
                <div class="slides">
                    <img src="./images/photo-1.jpg"  alt="풍경3">
                    <img src="./images/photo-2.jpg"  alt="풍경3">
                    <img src="./images/photo-3.jpg"  alt="풍경3">
                    <button id="prev">&lang;</button>
                    <button id="next">&rang;</button>
                
            </div>
               
            </section>
            <section id="intro">
                <h1>Welcome~ <strong>제주</strong>에 놀러 오세요 !!</h1>
                <p id="demo"></p>
                
            </section>
        
            
      
        <footer>
            <ul id="bottomMenu">
               
                <li><a href="#">회사 소개</a></li>
                <li><a href="#">개인정보 처리방침</a></li>
                <li><a href="#">여행 약관</a></li>
                <li><a href="#">사이트맵</a></li>
            </ul>
        </footer>
    </div>
    <script src="./slideshow.js"></script>
    <script>
        setInterval(myWatch, 1000);

        function myWatch(){
        var date = new Date();
        var now = date.toLocaleTimeString();
        document.getElementById("demo").innerHTML = now;
        }
    </script>
</body>
</html>