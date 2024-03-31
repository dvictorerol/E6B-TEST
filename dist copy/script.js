
document.body.addEventListener("keyup", function(event) {
  if (event.key == 'Enter'){
    var inputValue = document.getElementById('input').value
    console.log(inputValue)
    anime({
      targets: '.rect',
      height: inputValue,
    })
  }
});