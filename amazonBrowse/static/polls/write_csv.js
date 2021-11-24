document.getElementById("btn").addEventListener('click', function(){
  console.log("ok");
  let xhr = new XMLHttpRequest()
  xhr.open('GET', 'http://127.0.0.1:8000/amazonBrowse/')
});
