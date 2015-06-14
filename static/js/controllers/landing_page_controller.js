noqapp.controller('landingpagecontroller',function($scope, landingServices){
	console.log('hai');
	$scope.emailid="jawahar";
	$scope.inviteflag=0;
	$scope.invite=function(){
		console.log('click');
		var data={emailid:$scope.mailid};
		landingServices.invite.success(function(res){
			if(res=500){
				$scope.inviteflag=1;
			}
		}).error(function(res){

		});
	}
});