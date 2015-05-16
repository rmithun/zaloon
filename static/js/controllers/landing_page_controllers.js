accountsApp.controller('landingpagecontroller',function($scope, $window, httpServices){

	$scope.fblogin = function(dummy)
	{
		httpServices.login_to_fb(dummy).then(function(data)
		{
		  console.log(data)
		},
		{
		   //cannot login to fb try again
		});
	}
	$scope.getData

});