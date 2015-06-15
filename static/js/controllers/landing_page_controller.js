noqapp.controller('landingpagecontroller',function($scope, landingServices){

	$scope.emailid = null;
	$scope.inviteflag = null;

	$scope.invite=function(){

		var data = {email:$scope.emailid};
		landingServices.invite(data).then(function(res)
		{
			$scope.inviteflag = 1;
		}, 
		function()
		{
			$scope.inviteflag = 0;
			console.log("Error inviting")
		})
	}
});