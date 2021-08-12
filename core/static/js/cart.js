//source: https://www.youtube.com/watch?v=woORrr3QNh8&t=1961s
console.log("Cart Javascript loaded")
var updateButtons = document.getElementsByClassName('update-cart')

//get all the buttons for "add to cart"
//go through each button
for (let i = 0; i < updateButtons.length; i++) {
	updateButtons[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log()
		console.log(productId, 'Action:', action)
		console.log('User',user)
			updateUserOrder(productId, action)
		})}


function updateUserOrder(productId, action){
	console.log('User is authenticated, transferring data')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				//token from main page
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId, 'action':action})
		})

		.then((response) => {
		   return response.json();

		})
		.then((data) => {
			console.log('data',data)
			location.reload()
		});
}
