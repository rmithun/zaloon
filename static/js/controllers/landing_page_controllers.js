accountsApp.controller('landingpagecontroller',function($scope, $window, httpServices,sessionService){
$scope.is_logged = sessionService.isLogged()
	$scope.fbLogin = function(dummy)
	{

		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  console.log(data)
		  if(data)
		  {
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(dataz)
		  	{
		  		console.log(dataz)
		  		$scope.user_name = dataz['user_details'].data[0].user_acc.first_name
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

if($scope.is_logged == 1)
{
httpServices.getUsrDetails().then(function(dataz)
{
	console.log(dataz)
	$scope.user_name = dataz['user_details'].data[0].user_acc.first_name
}, function()
{
	console.log("Error getting user data")
})	
}
});