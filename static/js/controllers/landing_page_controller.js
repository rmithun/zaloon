noqapp.controller('landingpagecontroller',function($scope, landingServices){

	$scope.formsubmit=false;
	$scope.inviteflag = null;
    $scope.lp_invited = false;
    var mapOptions = {
        zoom: 10,
        scrollwheel: false,
        center: new google.maps.LatLng(13.0827, 80.2707),
        mapTypeId: google.maps.MapTypeId.TERRAIN,
        disableDefaultUI: true,
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.SMALL,
            position: google.maps.ControlPosition.LEFT_CENTER
        }
    }
    $scope.map = new google.maps.Map(document.getElementById('googleMap1'), mapOptions);
    var latlongcollection = [];
    $scope.markers = [];
    var bounds = new google.maps.LatLngBounds();
    var imagUrls = {        
        //oneOff: '../static/img/blue24.png',
        //oneOn: '../static/img/green24.png'
        iconsaloon:'../static/img/saloon.png',
        iconparlor:'../static/img/beautyparlor.png',
        iconspa:'../static/img/spa.png',
        iconuser:'../static/img/user.png'
    };
    var images = {
        //oneOn: new google.maps.MarkerImage(imagUrls.oneOn),
        //oneOff: new google.maps.MarkerImage(imagUrls.oneOff)
        iconsaloon: new google.maps.MarkerImage(imagUrls.iconsaloon),
        iconparlor: new google.maps.MarkerImage(imagUrls.iconparlor),
        iconspa: new google.maps.MarkerImage(imagUrls.iconspa),
        iconuser:new google.maps.MarkerImage(imagUrls.iconuser)
    };
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

	$scope.getAllAreaStudios = function()
	{
		landingServices.getAllAreaStudios().then(function(data)
		{
			$scope.studios = data.allstudios.data
			angular.forEach($scope.studios, function (studio, key) {				
				createmarker(studio);								
			});
			$scope.map.fitBounds(bounds);
            autozoom();
		},function()
		{
			console.log("Not getting studios")
		})
	}
	var createmarker = function (studio) {
		//console.log(studio)
        var icon;
        if(studio.type_desc=="Salon"){
            icon=images.iconsaloon;            
        }
        else if(studio.type_desc=="Spa"){
            icon=images.iconspa;            
        }
        else{
            icon=images.iconparlor;            
        }
        var marker = new google.maps.Marker({
            map: $scope.map,
            position: new google.maps.LatLng(studio.latitude, studio.longitude),            
            icon: icon            
        });        
        $scope.markers.push(marker);
        var latlong = new google.maps.LatLng(studio.latitude, studio.longitude);
        latlongcollection.push(latlong);
    }    
    function autozoom() {
        var latlngbounds = new google.maps.LatLngBounds();
        for (var i = 0; i < latlongcollection.length; i++) {
            latlngbounds.extend(latlongcollection[i]);
        }
        $scope.map.fitBounds(latlngbounds);
        $scope.map.panToBounds(latlngbounds);
        $scope.map.setZoom(13);         
    }
$scope.getAllAreaStudios();
});