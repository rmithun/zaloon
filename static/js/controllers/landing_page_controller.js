noqapp.controller('landingpagecontroller',function($scope, landingServices){

	$scope.formsubmit=false;
	$scope.inviteflag = null;


	$scope.invite=function(form)
	{
		$scope.formsubmit=true;
		console.log(form.$valid)
		if(form.$valid)
		{
			var data = {email:$scope.emailid};
			landingServices.invite(data).then(function(res)
			{
				$scope.inviteflag = 1;
			}, 
			function(res)
			{
				$scope.inviteflag = 0;
				console.log("Error inviting")
			})
		}
	}
});