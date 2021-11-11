var customerNum = prompt("입장객은 몇 명인가요?"); 
var columnNum = prompt("한 줄에 몇명 앉나요?");    
var rowNum = 0;       

if(customerNum == null || columnNum == null){
    document.write("입력이 취소되었습니다.");
}
else{
    if(customerNum % columnNum == 0){
        rowNum = customerNum / columnNum;
    }
    else{
        rowNum = parseInt(customerNum / columnNum) + 1;
    }
}
document.write("<table>");
for(var i = 0; i < rowNum; i++){
    document.write("<tr");
    for(var j = 1; j <= columnNum; j++){
        var seatNum = i * columnNum + j;
        if(seatNum > customerNum) break;
        document.write("<td>좌석"+ seatNum + "</td>");
    }
    document.write("</tr>");
}
document.write("</table>");