noqapp.controller('landingpagecontroller',function($scope, landingServices){
	$scope.inviteflag=0;
	$scope.invite=function(){
		var data={emailid:$scope.mailid};
		landingServices.invite.success(function(res){
			if(res=500){
				$scope.inviteflag=1;
			}
		}).error(function(res){

		});
	}
});