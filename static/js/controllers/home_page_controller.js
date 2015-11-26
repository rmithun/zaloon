noqapp.controller('homepagecontroller',function($scope, $cookies,$window, $timeout, $location,$facebook,lodash,httpServices,sessionService,putResultService,gService){
$scope.is_logged = sessionService.isLogged();
//$scope.is_logged=false;
$scope.formsubmit=false;
$scope.iswrongservice=false;
$scope.studioservicegroup=[];
$scope.studioactiveservice=[];
$scope.studiolocation=[];
$scope.arealocation=['Porur, Chennai, Tamil Nadu, India','Ramapuram, Chennai, Tamil Nadu, India','Iyappanthangal, Chennai, Tamil Nadu, India','Valasaravakkam, Chennai, Tamil Nadu, India'];
$scope.isLoggedIn = true;
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
$scope.login = function() {
    $facebook.login().then(function() {
      refresh();
    });
  }
  function refresh() {
    $facebook.api("/me").then( 
      function(response) {      	
      	var token=$facebook.getAuthResponse();
      	$scope.fbLogin(token.accessToken);        
        $scope.user_name =response.name;
      },
      function(err) {
        $scope.welcomeMsg = "Please log in";
      });
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

$scope.logging_out = false
$scope.logOut = function()
	{	
		$scope.logging_out = true
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
	$scope.areacomplete = function (val) { 
		console.log(val)
    	 return gService.getPlace(val).then(function (data) {     
    	 console.log(data.location)      
            return data.location;
        });
    }
    //Get All Services    
    httpServices.getServiceType().then(function(data) {        		
    	$scope.studioservicegroup = data['service_details'].data;    
    	$scope.studioactiveservice = lodash.pluck(lodash.where(data['service_details'].data, { 'is_active': true }),'service_name');    	
    },function() {
    	console.log("Try again to get service")
    });    

    //Search Studio Details Event
    $scope.searchstudio=function(form){
    	$scope.formsubmit=true;
    	$scope.iswrongservice=false;
    	if(form.$valid)
		{				
    		var idx=lodash.findIndex($scope.studioservicegroup, { service_name: $scope.searchdata_.servicename.trim() });
    		console.log(idx)
    		if (idx != -1) {
    			var obj={'service':$scope.studioservicegroup[idx].id,'location':$scope.searchdata_.searchlocation,'servicename':$scope.studioservicegroup[idx].service_name};    			
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
    			$scope.searchdata_.servicename ="";
    			$scope.iswrongservice=true;
    			$scope.formsubmit=false;
    		}    				
		}
    }
    $scope.onserviceselect = function ($item, $model, $label) {    	 	
    	$scope.searchdata_.servicename =$label;	    	   
	    $scope.iswrongservice=false;
	};
	$scope.onlocationselect = function ($item, $model, $label) {		
		if($label!="Notfound"){
			$scope.searchdata_.searchlocation=$label;
		}
		else{			
			$scope.searchdata_.searchlocation="";
		}
	};	
});