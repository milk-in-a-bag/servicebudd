const categoryParagraphs = document.querySelectorAll(".cat");
const locationParagraphs = document.querySelectorAll(".loc");
const priceParagraphs = document.querySelectorAll(".pri");

categoryParagraphs.forEach((categoryParagraph) => {
  categoryParagraph.addEventListener("click", () => {
    const categoryData = categoryParagraph.getAttribute("data-category");
    const data = {
      category: categoryData,
    };

    fetch("http://127.0.0.1:8000/filter/47", {
      method: "PUT",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
    })
      .then((res) => res.json())
      .then((data) => console.log(data));
  });
});

locationParagraphs.forEach((locationParagraph) => {
  locationParagraph.addEventListener("click", () => {
    const locationData = locationParagraph.getAttribute("data-location");
    const data = {
      location: locationData,
    };

    fetch("http://127.0.0.1:8000/filter/47", {
      method: "PUT",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
    })
      .then((res) => res.json())
      .then((data) => console.log(data));
  });
});

priceParagraphs.forEach((priceParagraph) => {
  priceParagraph.addEventListener("click", () => {
    const priceData = priceParagraph.getAttribute("data-price");
    const data = {
      starting_price: priceData,
    };

    fetch("http://127.0.0.1:8000/filter/47", {
      method: "PUT",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
    })
      .then((res) => res.json())
      .then((data) => console.log(data));
  });
});
