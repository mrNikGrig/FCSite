src="https://code.jquery.com/jquery-3.6.0.min.js"

function getValue() {
alert("sending...")
    var name = document.getElementById('myInput').value;
    $.ajax({
          url: '/quantity',
          type: 'POST',
          data: {
            var1: name,
            var2: quantityVar
          },
          success: function(response) {
            // Обработка успешного ответа от сервера
          }
        });
      });
    });
}