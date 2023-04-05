// product_detail.js
$(document).ready(function() {
    $('.add-to-cart').click(function(event) {
        event.preventDefault();
        var productId = $(this).data('product-id');
        $.ajax({
            url: '/add_to_cart/' + productId + '/',
            type: 'GET',
            success: function(data) {
                $('#cart-count').text(data.cart_count);
                alert(data.message);
            },
            error: function() {
                alert('An error occurred.');
            }
        });
    });
});




  