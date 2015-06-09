noqapp.controller('landingpagecontroller',function($scope, $cookies, $window,httpServices,sessionService){
$scope.is_logged = sessionService.isLogged()
	$scope.fbLogin = function(dummy)
	{

		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  if(data)
		  {
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(dataz)
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		$scope.user_name = dataz['user_details'].data[0].first_name
		  	}, function()
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		console.log("Error getting user data")
		  	})
		  	
		  }
		},function()
		{
		   //cannot login to fb try again
		   console.log("Cannot login to FB")
		});
	}

if(sessionService.isLogged())
{
httpServices.getUsrDetails().then(function(dataz)
{
	$scope.user_name = dataz['user_details'].data[0].first_name
}, function()
{
	console.log("Error getting user data")	
})	
}


	$scope.logOut = function()
	{	
		httpServices.logOut().then(function(logout_data)
		{
			$cookies.remove('token')
			//$scope.is_logged = sessionService.isLogged()
			console.log("Logged out successfully")
			$window.location.href = "/"
		},
		function()
		{
			console.log("Logout Error")
		})
	}


	$scope.getDetails = function()
	{
		httpServices.getBookings().then(function(booking)
		{
			console.log(booking)
		},
		function()
		{
			console.log("Logout Error")	
		})
	}

});