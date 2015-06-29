noqapp.controller('accountscontroller',function($scope, httpServices){

    $scope.active_booking_count = 10;
	$scope.getBookings = function()
	{
		httpServices.getDetails().then(function(data)
		{
			$scope.user_details = data.user_details.data[0]
			$scope.booking_details = data.booking.data
			httpServices.splitBookings($scope.booking_details).then(function(data)
			{
				$scope.active_bookings = data.active_booking
				$scope.expired_bookings = data.inactive_booking
			},
			function()
			{
				console.log("Error splitting bookings")
			});
		},
		function()
		{
			console.log("Error getting user Details and booking")	
		})
	}

	$scope.getBookings();

	$scope.booking_cancel = function(id)
	{
		httpServices.cancelBooking(id).then(function(data)
		{
			$scope.getBookings();
			console.log("Booking successfully cancelled")
		},
		function()
		{
			console.log("Logout Error")	
		})
	}

	$scope.change_usr_details = function()
	{
		$scope.usr_data = null
		httpServices.updateUserProfile($scope.usr_data).then(function(data)
		{
			console.log("Details updated")
		},
		function()
		{
			console.log("Could not update try again.")	
		})
	}

	$scope.add_review = function()
	{
		$scope.review_data = null
		httpServices.addReview($scope.review_data).then(function(data)
		{
			console.log("Review added")
		},
		function()
		{
			console.log("Error occurred;Please,Try again.")	
		})
	}
});
	