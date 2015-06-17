noqapp.controller('homepagecontroller',function($scope, $cookies, $window,httpServices,sessionService){
$scope.is_logged = sessionService.isLogged();

 function getFBKey()
 {
	httpServices.getFBKey().then(function(data)
	{
		$scope.fb_key = data['fb_key'].data
	});
 }
getFBKey()

	$scope.fbLogin = function(dummy)
	{

		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  if(data)
		  {
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(dataz)
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		$scope.user_name = dataz['user_details'].data[0].first_name
		  		$('#signupmodel').modal('hide');
		  	}, function()
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		console.log("Error getting user data")
		  	})
		  	
		  }
		},function()
		{
		   //cannot login to fb try again
		   console.log("Cannot login to FB")
		});
	}

if(sessionService.isLogged())
{
httpServices.getUsrDetails().then(function(dataz)
{
	$scope.user_name = dataz['user_details'].data[0].first_name
}, function()
{
	console.log("Error getting user data")	
})	
}


	$scope.logOut = function()
	{	
		httpServices.logOut().then(function(logout_data)
		{
			$cookies.remove('token')
			//$scope.is_logged = sessionService.isLogged()
			console.log("Logged out successfully")
			$window.location.href = "/"
		},
		function()
		{
			console.log("Logout Error")
		})
	}


	$scope.getDetails = function()
	{
		httpServices.getBookings().then(function(booking)
		{
			console.log(booking)
		},
		function()
		{
			console.log("Logout Error")	
		})
	}

	//AutoComplete
	$scope.location_ = {};
	$scope.location_['area'] = '';
	
	$scope.location_['arealist'] = [];
	$
	var acService = new google.maps.places.AutocompleteService();
	$scope.areacomplete = function () {
    	if ($scope.location_['area'] != "") {
            acService.getPlacePredictions({
                input: $scope.location_['area'],
                types: ['(regions)'],
                componentRestrictions: { 'country': 'in' }
            }, function (places, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
                    //console.log(places);
                    var _places = [];
                    for (var i = 0; i < places.length; ++i) {
                    	_places.push({
                        	id: places[i].place_id,
                        	value: places[i].description,
                        	label: places[i].description
                    	});
                	}                	
                	$scope.location_['arealist'] = _places;
                	//console.log($scope.location_['arealist']);
            	}
        	});
    	}
    }
    //Service
    $scope.location_['service']='';
    $scope.location_['servicelist']='';
    httpServices.getService().then(function(data)
    	{
    		$scope.location_['servicelist'] = data['service_details'].data;

    	},function()
    	{
    		console.log("Try again to get service")
    	});    
    $scope.hoverIn = function(){
    	console.log('hai');
	};
});