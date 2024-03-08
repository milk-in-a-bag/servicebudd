/*document.addEventListener("DOMContentLoaded", function () {
  const categoryParagraph = document.getElementById("categoryParagraph");

  categoryParagraph.addEventListener("click", function () {
    const categoryData = categoryParagraph.getAttribute("data-category");

    // Make an AJAX request to your Django view
    /*fetch("http://127.0.0.1:8000/result", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
      body: JSON.stringify({ categoryData: categoryData }),
    })
      .then((response) => response.json())
      .then((data) => console.log("Response from Django:", data))
      .catch((error) => console.error("Error:", error));
  });
});*/

const data = {
  title: "This is a title",
  body: "This is a body",
  userId: "This is a user id",
};

$(document).ready(() => {
  $.ajax({
    type: "POST",
    url: "https://jsonplaceholder.typicode.com/posts",
    data: JSON.stringify(data),
    success: (data) => {
      console.log(data);
    },
    error: (response) => {
      alert("An error occured");
    },
  });
});

/*$(document).ready(function () {
  $("button").click(function () {
    $.post(
      "http://127.0.0.1:8000/result",
      {
        name: "Donald Duck",
        city: "Duckburg",
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      function (data, status) {
        alert("Data: " + data + "\nStatus: " + status);
      }
    );
  });
});*/

/*const xhr = new XMLHttpRequest();

xhr.onload = function () {
  const serverResponse = document.getElementById("serverResponse");
  serverResponse.innerHTML = this.responseText;
};

xhr.open("POST", "http://127.0.0.1:8000/result");
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
xhr.setRequestHeader("X-CSRFToken", csrfToken);
xhr.send("name=dominic");*/

/*fetch("https://jsonplaceholder.typicode.com/users")
  .then(function (res) {
    return res.json();
  })
  .then(function (data) {
    console.log(data);
  });

const data = {
  title: "This is a title",
  body: "This is a body",
  userId: "This is a user id",
};

fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  body: JSON.stringify(data),
  headers: {
    "Content-Type": "application/json",
  },
})
  .then((res) => res.json())
  .then((data) => console.log(data));*/
