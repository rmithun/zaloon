noqapp.controller('accountscontroller',function($scope, httpServices){

    $scope.active_booking_count = 10;
	$scope.getBookings = function()
	{
		httpServices.getDetails().then(function(data)
		{
			console.log(data)
		},
		function()
		{
			console.log("Logout Error")	
		})
	}

	$scope.getBookings();

	$scope.booking_cancel = function()
	{
		httpServices.cancelBooking().then(function(data)
		{
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
