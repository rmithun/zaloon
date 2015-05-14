accountsApp.controller('landingpagecontroller',function($scope, httpServices){

	$scope.fblogin = function()
	{
		httpServices.login_to_fb().then(function(data)
		{
		  //get token and login	
		  console.log(data)
		},
		{
		   //cannot login to fb try again
		});
	}
});