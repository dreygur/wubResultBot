
var submit = document.getElementById("submit");
var body = document.getElementById("body");

submit.onclick = function () {
    var keyword = document.getElementById("search").value;
    var url = "https://cors-anywhere.herokuapp.com/https://wubresult.herokuapp.com/result/2884"

    fetch(url).then( (res) => {
        return res.json();
    }).then( (data) => {
        // var result = JSON.parse(data);
        var result = JSON.stringify(data);
        var resultText = document.createElement(`<div> ${result} </div>`);
        body.insertBefore(resultText, body);
        // console.log(result)
    })
    // console.log(keyword);
}