const grid = document.getElementById("container")

fetch("../scraped-data.json")
.then(response=>response.json())
.then(data=>{
    console.log(data)
    data.forEach((item)=>{
        let cart = document.createElement("div")
        cart.className = "product-cart"

        grid.appendChild(cart)

        let img = document.createElement("img")
        img.setAttribute("src",item.img)
        cart.appendChild(img)

        let title = document.createElement("div")
        title.textContent = item.title
        cart.appendChild(title)
        
    })
})
.catch(error=>console.error(error))
