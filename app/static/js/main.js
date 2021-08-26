// var form = document.getElementById("form");

// form.addEventListener("submit", (event) => {
//     event.preventDefault();
// });

var submit = document.getElementById("submit");
var body = document.getElementById("body");
var search = document.getElementById("search");

submit.onclick = function () {
    var keyword = document.getElementById("search").value;
    var url = "https://eshikhon.herokuapp.com/web/";
    fetch(url + search.value).then((res) => {
        return res.json();
    }).then((data) => {
        // var result = JSON.parse(data);
        // var result = JSON.stringify(data);
        // body.innerText = data;
        console.log(data);

        Swal.fire({
            title: 'Result',
            html: data.replace(/\n/g, "<br />")
        });

    });
    // console.log(keyword);
    // result.replace(/\n/g, "<br />")
};
