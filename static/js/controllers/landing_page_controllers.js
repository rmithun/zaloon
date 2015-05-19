accountsApp.controller('landingpagecontroller',function($scope, $window, httpServices){

	$scope.fblogin = function(dummy)
	{
		httpServices.login_to_fb(dummy).then(function(data)
		{
		  console.log(data)
		  if(data['access_token'].data['access_token'] != null)
		  {
		  	$window.location.href = "/account/home/"
		  }
		},
		{
		   //cannot login to fb try again
		});
	}
	$scope.getData

});