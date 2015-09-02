noqapp.controller('homepagecontroller',function($scope, $cookies,$window, $location,httpServices,sessionService,putResultService){
$scope.is_logged = sessionService.isLogged();
$scope.formsubmit=false;

 function getFBKey()
 {
 	$scope.fb_key = httpServices.getFBKey()
 	/*
	httpServices.getFBKey().then(function(data)
	{
		$scope.fb_key = data['fb_key'].data
	}, function()
	{
		console.log("Error getting FB key")
	});*/
 }
getFBKey()

	$scope.fbLogin = function(dummy)
	{
		$('.loader-overlay').show();
		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  $('.loader-overlay').hide();
		  if(data)
		  {
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(dataz)
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		$scope.user_name = dataz['user_details'].data[0].user_acc['first_name']
		  		//$('#signupmodel').modal('hide');
		  	}, function()
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		console.log("Error getting user data")
		  	})
		  	
		  }
		},function()
		{
		   //cannot login to fb try again
		   $scope.is_logging = 1
		   console.log("Cannot login to FB")
		});
	}

if(sessionService.isLogged())
{
httpServices.getUsrDetails().then(function(dataz)
{
	$scope.user_name = dataz['user_details'].data[0].user_acc['first_name']
}, function()
{
	console.log("Error getting user data")	
})	
}


	$scope.logOut = function()
	{	
		httpServices.logOut().then(function(logout_data)
		{
			var cookies = $cookies.getAll();
            angular.forEach(cookies, function (v, k) {
                $cookies.remove(k,{path:'/'});
            });
            console.log("Logged out successfully")
            $scope.is_logged = sessionService.isLogged();
            $window.location.href = "/"
		},
		function()
		{
			console.log("Logout Error")
		})
	}


	//AutoComplete
	$scope.searchdata_ = {};	
	$scope.searchdata_['arealist'] = [];	
	var acService = new google.maps.places.AutocompleteService();
	$scope.areacomplete = function () {				
    	if ($scope.searchdata_['searchlocation'] != "" && typeof $scope.searchdata_['searchlocation'] != 'undefined') {
            acService.getPlacePredictions({
                input: $scope.searchdata_['searchlocation'],
                types: ['(regions)'],
                componentRestrictions: { 'country': 'in' }
            }, function (places, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {                    
                    var _places = [];                    
                    for (var i = 0; i < places.length; ++i) {
                    	_places.push({
                        	id: places[i].place_id,
                        	value: places[i].description,
                        	label: places[i].description
                    	});
                	}                	
                	if(_places.length>0){           	
                		$scope.searchdata_['arealist'] = _places;     
                	}                	
            	}
            	else{
            		$scope.searchdata_['arealist'] =[{'label':null,'value':null}];
            	}
        	});
    	}
    }
    //Get All Services    
    $scope.searchdata_['servicelist']='';
    httpServices.getServiceType().then(function(data)
    	{    
    		console.log(data['service_details'].data.length)		
    		$scope.searchdata_['servicelist'] = data['service_details'].data;
    		

    	},function()
    	{
    		console.log("Try again to get service")
    	});    

    //Search Studio Details Event
    $scope.searchstudio=function(form){
    	$scope.formsubmit=true;
    	if(form.$valid)
		{ 			
			var obj={'service':$scope.searchdata_.service_name,'location':$scope.searchdata_.searchlocation};
			$('.finder-overlay').show();
			 httpServices.getstudioDetails(obj).then(function(data)
		    	{		
		    		$cookies.putObject('searchdata',obj,{path:'/'})    	
		    		//console.log(data.studio_details.data)	
		    		//$cookies.putObject('data',data.studio_details.data,{path:'/'})
		    		putResultService.setresult(data.studio_details.data);
		    		$location.path("/search");		    		
		    	},function()
		    	{
		    		console.log("Try again to get service")
		    	});
		}
    }
    $scope.onserviceselect = function ($item, $model, $label) {    	
	    $scope.searchdata_.service_name=$item.service_name;	   
	};
	$scope.onlocationselect = function ($item, $model, $label) {
		$scope.searchdata_.searchlocation=$label;
	};
});