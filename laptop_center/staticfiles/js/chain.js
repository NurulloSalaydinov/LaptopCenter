function addToCart(id, qty)
{
    const formData = {
        product_id: id,
        qty: qty
    }
    fetch('/cart/add_to_cart/', {
        method: "POST",
        body: JSON.stringify(formData), 
    })
        .then(response => response.json())
        .then(data =>
        {
            if (data.status == 200)
            {
                var old_count = parseInt(document.getElementById('cart-count').innerHTML)
                var new_count = old_count + parseInt(qty)
                document.getElementById('cart-count').innerHTML = new_count
                var alert = document.createElement('div');
                alert.style = `
                position: fixed;top: 100px;right: -100%;
                transition: all 0.4s;
                width: auto;
                height: auto;
                background: #00ff48;
                color: #fff;
                padding: 10px 40px;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 11111111;
                `
                alert.innerHTML = `<h2>Savatchaga qo'shildi</h2>`
                document.body.appendChild(alert)
                setTimeout(() =>
                {
                    alert.style.right = '10px'
                }, 500)
                setTimeout(() =>
                {
                    document.body.removeChild(alert)
                }, 3000)
                alert.onclick = () =>
                {
                    document.body.removeChild(alert)
                }
            }
        })
        .catch(err => console.log(err))
}




