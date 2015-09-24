noqapp.controller('landingpagecontroller',function($scope, landingServices){

	$scope.formsubmit=false;
	$scope.inviteflag = null;
    $scope.lp_invited = false;
    var mapOptions = {
        zoom: 10,
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
        oneOff: '../static/img/blue24.png',
        oneOn: '../static/img/green24.png'
    };
    var images = {
        oneOn: new google.maps.MarkerImage(imagUrls.oneOn),
        oneOff: new google.maps.MarkerImage(imagUrls.oneOff)
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
		console.log(studio)
        var marker = new google.maps.Marker({
            map: $scope.map,
            position: new google.maps.LatLng(studio.latitude, studio.longitude),            
            icon: images.oneOff
        });        
        google.maps.event.addListener(marker, 'mouseover', function (event) {
            this.setIcon(images.oneOn);
        });
        google.maps.event.addListener(marker, 'mouseout', function (event) {
            this.setIcon(images.oneOff);
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