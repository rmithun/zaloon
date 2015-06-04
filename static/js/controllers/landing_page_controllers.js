accountsApp.controller('landingpagecontroller',function($scope, $window, httpServices,sessionService){


$scope.is_logged = null;
	$scope.fbLogin = function(dummy)
	{

		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  console.log(data)
		  if(data)
		  {
		  	$scope.is_logged = sessionService.isLogged()
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(data)
		  	{
		  		$scope.user_name = data['user_details'].data[0].user_acc.first_name
		  	}, function()
		  	{
		  		console.log("Error getting user data")
		  	})
		  	//$window.location.href = "/account/home/"
		  }
		},function()
		{
		   //cannot login to fb try again
		   console.log("Cannot login to FB")
		});
	}

});