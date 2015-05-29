accountsApp.controller('landingpagecontroller',function($scope, $window, httpServices,sessionService){

	$scope.fbLogin = function(dummy)
	{
		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  console.log(data)
		  if(data)
		  {
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(data)
		  	{
		  		console.log(data)
		  	}, function()
		  	{
		  		console.log("Error getting user data")
		  	})
		  	$window.location.href = "/account/home/"
		  }
		},function()
		{
		   //cannot login to fb try again
		   console.log("Cannot login to FB")
		});
	}

});