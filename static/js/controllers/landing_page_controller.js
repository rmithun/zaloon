noqapp.controller('landingpagecontroller',function($scope, landingServices){

	$scope.formsubmit=false;
	$scope.inviteflag = null;

    $scope.lp_invited = false;
	$scope.invite=function(form)
	{
		$scope.formsubmit=true;
		console.log(form.$valid)
		if(form.$valid)
		{
            $scope.lp_invited = true;
			//$scope.lp_invited = false;
			var data = {email:$scope.emailid};
			landingServices.invite(data).then(function(res)
			{
				$scope.inviteflag = 1;
			}, 
			function(res)
			{
				$scope.lp_invited = false;
				$scope.inviteflag = 0;
				console.log("Error inviting")
			})
		}
	}

	function getAllAreaStudios = function()
	{
		httpServices.getAllStudios().then(function(data)
		{
			$scope.studios = data.allstudios.data
		},function()
		{
			console.log("Not getting studios")
		})
	}

});