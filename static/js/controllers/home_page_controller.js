noqapp.controller('homepagecontroller',function($scope, $cookies,$window, $timeout, $location,lodash,httpServices,sessionService,putResultService){
$scope.is_logged = sessionService.isLogged();
$scope.formsubmit=false;
$scope.iswrongservice=false;

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
$scope.getAllAreaStudios = function()
{
	httpServices.getAllStudios().then(function(data)
	{
		$scope.studios = data.allstudios.data
	},function()
	{
		console.log("Not getting studios")
	})
}

getFBKey()

	$scope.fbLogin = function(dummy)
	{
		$('.loader-overlay').show();
		httpServices.loginUsingFB(dummy).then(function(data)
		{
		  if(data)
		  {
		  	sessionService.setAuthToken(data)
		  	httpServices.getUsrDetails().then(function(dataz)
		  	{
		  		$scope.is_logged = sessionService.isLogged()
		  		$scope.user_name = dataz['user_details'].data[0].user_acc['first_name']
		  		//$('#signupmodel').modal('hide');
		  		$('.loader-overlay').hide();

		  	}, function()
		  	{
		  		$('.loader-overlay').hide();
		  		$scope.is_logged = sessionService.isLogged()
		  		$('#signuperrormodal').modal('show');
		  		console.log("Error getting user data")
		  	})
		  	
		  }
		},function()
		{
		   //cannot login to fb try again
		   $('.loader-overlay').hide();
		   $('#signuperrormodal').modal('show');
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
            window.location.reload()
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
    		$scope.searchdata_['servicelist'] = data['service_details'].data;    		
    	},function()
    	{
    		console.log("Try again to get service")
    	});    

    //Search Studio Details Event
    $scope.searchstudio=function(form){
    	$scope.formsubmit=true;
    	$scope.iswrongservice=false;
    	if(form.$valid)
		{			
    		if(typeof $scope.searchdata_.service != "undefined"){    			
    			var servicename=$scope.searchdata_.service_name;
    			servicename=servicename.trim();
    			if (lodash.findIndex($scope.searchdata_['servicelist'], { service_name: $scope.searchdata_.service_name.trim() }) != -1) {
    				var obj={'service':$scope.searchdata_.service.id,'location':$scope.searchdata_.searchlocation,'servicename':$scope.searchdata_.service.service_name};					
					$('.finder-overlay').show();
			 		httpServices.getstudioDetails(obj).then(function(data) {		
		    			$cookies.putObject('searchdata',obj,{path:'/'})		    		
		    			putResultService.setresult(data.studio_details.data);		    			    	
		    			$location.path("/search");		    		
		    		},function() {
		    			console.log("Try again to get service")
		    		});
    			}
    			else{
    				$scope.searchdata_.service_name ="";
    				$scope.iswrongservice=true;
    				$scope.formsubmit=false;
    			}
    		}
    		else{
    			$scope.searchdata_.service_name ="";
    			$scope.iswrongservice=true;
    			$scope.formsubmit=false;
    		}			
		}
    }
    $scope.onserviceselect = function ($item, $model, $label) {    
    	$scope.searchdata_.service_name =$label;
	    $scope.searchdata_.service=$model;	   
	    $scope.iswrongservice=false;
	};
	$scope.onlocationselect = function ($item, $model, $label) {
		$scope.searchdata_.searchlocation=$label;
	};
	$scope.onFocus = function (e) {		
		var textbox=$(event.target);
		console.log(textbox)
		textbox.find('#service_id').attr('aria-expanded', true);
		//textbox['aria-expanded']=true;
		//console.log(textbox)
        $timeout(function () {             
          $(e.target).trigger('input');          
          $(e.target).trigger('change'); // for IE
        });
      };
      $scope.stateComparator = function (state, viewValue) {
      	//console.log(state)
      	//console.log(viewValue)
        return viewValue === secretEmptyKey || (''+state).toLowerCase().indexOf((''+viewValue).toLowerCase()) > -1;
      };
});