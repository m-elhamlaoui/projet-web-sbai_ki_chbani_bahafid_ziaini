$(document).ready(function(){

    load_cart_data();


function load_cart_data()
	{
		$.ajax({
			url:"./../fetch_cart/",
			method:"POST",
			dataType:"json",
			success:function(data)
			{
				$('#cart_details').html(data.cart_details);
				$('.total_price').text(data.total_price);
				$('.badge').text(data.total_item);
			}
		});
	}

$(document).on('click', '.add_to_cart', function(){
		var product_id = $(this).attr("id");
		var product_name = $('#name'+product_id+'').val();
		var product_price = $('#price'+product_id+'').val();
		var product_photo = $('#photo'+product_id).val();
        var product_quantity = $('#quantity'+product_id).val();
		var action = "add";

			$.ajax({
				url:"./../gestion_panier/",
				method:"POST",
				data:{product_id:product_id, product_name:product_name, product_price:product_price, product_quantity:product_quantity,product_photo:product_photo, action:action},
				success:function(data)
				{
					load_cart_data();
				}
			});

	});

});

 

function load_cart_data()
	{
		$.ajax({
			url:"./../fetch_cart/",
			method:"POST",
			dataType:"json",
			success:function(data)
			{
				$('#cart_details').html(data.cart_details);
				$('.total_price').text(data.total_price);
				$('.badge').text(data.total_item);
			}
		});
	}

	$(document).on('click', '.delete', function(){
		var product_id = $(this).attr("id");
		var action = 'remove';
		
			$.ajax({
				url:"./../gestion_panier/",
				method:"POST",
				data:{product_id:product_id, action:action},
				success:function()
				{
					load_cart_data();
				}
			})
	});

    $(document).on('click', '.ajouter', function(){
		var product_id = $(this).attr("id");
		var action = 'ajouter';
		{
			$.ajax({
				url:"./../gestion_panier/",
				method:"POST",
				data:{product_id:product_id, action:action},
				success:function()
				{
					load_cart_data();
				}
			})
		}

	});
    $(document).on('click', '.moins', function(){
		var product_id = $(this).attr("id");
		var action = 'moins';
		{
			$.ajax({
				url:"./../gestion_panier/",
				method:"POST",
				data:{product_id:product_id, action:action},
				success:function()
				{
					load_cart_data();
				}
			})
		}

	});

	$(document).on('click', '#clear_cart', function(){
		var action = 'empty';
		$.ajax({
			url:"./../gestion_panier/",
			method:"POST",
			data:{action:action},
			success:function()
			{
				load_cart_data();
			}
		});
	});
    


