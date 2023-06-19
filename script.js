document.getElementById('input-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    postData('/result', formData);
  });
  
  function updatePage(data) {
    
    document.getElementById('result-container').style.display = 'block';
  
    
    drawChart(data.x, data.psi_squared);
  }
  
  function postData(url, data) {
    fetch(url, {
      method: 'POST',
      body: data,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
    .then(response => response.json())
    .then(result => {
      
      updatePage(result);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  