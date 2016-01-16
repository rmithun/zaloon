noqapp.filter('startFrom', function () {
    return function (input, start) {
        if (input) {
            start = +start;
            return input.slice(start);
        }
        return [];
    };
});





noqapp.controller('resultCtrl', function ($scope, $compile,$location, $filter,$cookies,$window,$facebook,lodash,httpServices,sessionService,putResultService,gService) {
    
    //detect device    
    $scope.device = navigator.platform
    //console.log($scope.device)
    //console.log(navigator.userAgent)
    if($scope.device.indexOf("iPhone") != -1 || $scope.device.indexOf("iPod") != -1 || $scope.device.indexOf("iPad") != -1)
    {
        $scope.which_device = 1
    }
    else if(navigator.userAgent.indexOf("Android") != -1 || navigator.userAgent.indexOf("android") != -1)
    {
          $scope.which_device = 2
    }
    else
    {
        $scope.which_device = 0
    }
    $scope.studio = [];
    $scope.filteredstudio = [];
    $scope.servicelist = [];
    $scope.sergroup={};    
    $scope.selectedstudio = {};
    $scope.searchdata={};
    $scope.searchplace={};
    $scope.studioservicegroup=[];
    $scope.studioactiveservice=[];
    $scope.studiolocation=[];
    $scope.serviceprice = 0;  
    $scope.serviceduration=0;  
    $scope.morefilter = false;
    $scope.stariconset={1:'star1',2:'star2',3:'star3',4:'star4',5:'star5'};
    $scope.studiotype = [{ id:1, name: "Salon", active: false, icon: "cus-icon-salon" }, { id:2, name: "Spa", active: false, icon: "cus-icon-spa" }, { id:3, name: "Beauty parlor", active: false, icon: "cus-icon-women" }];
    $scope.studiokind = [{ id:1, name: "Men", active: false, icon: "fa-mars" }, {id:2, name: "Women", active: false, icon: "fa-venus" }, {id:3, name: "Unisex", active: false, icon: "fa-venus-mars" }];
    $scope.servicefor = [{id:0, name: "All", active:true},{id:1, name: "Men", active:false},{id:2, name: "Women", active:false}]
    $scope.studiostar = [{ star: 1, active: false }, { star: 2, active: false }, { star: 3, active: false }, { star: 4, active: false }, { star: 5, active: false }];
    $scope.studiosort = [{ property: "distance", value: "distanceasc", direction: false,name:"Distance" }, { property: "min_price", value: "priceasc", direction: false ,name:"Price"}, { property: "min_price", value: "pricedsc", direction: true,name:"Price dsc" }, { property: "rating", value: "ratingdsc", direction: true,name:"Rating" }];
    $scope.orderProp = 'min_price';
    $scope.direction = false;    
    $scope.studiotypefilter = [];
    $scope.studiokindfilter = [];
    $scope.studioratingfilter = [];    
    $scope.tempstudiotypefilter=[];
    $scope.tempstudiokindfilter = [];
    $scope.tempstudioratingfilter = [];    
    $scope.is_logged = sessionService.isLogged();
    $scope.selected_service = [];
    $scope.to_booking_flag = 0;
    $scope.serviceforselect= 0;
    var acService = new google.maps.places.AutocompleteService();
    var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer();
    var mdirectionsDisplay = new google.maps.DirectionsRenderer();
    var infoWindow = new google.maps.InfoWindow();
    var geocoder =  new google.maps.Geocoder();
    var mapOptions = {
        zoom: 4,
        scrollwheel: false,
        center: new google.maps.LatLng(40.0000, -98.0000),
        mapTypeId: google.maps.MapTypeId.TERRAIN,
        disableDefaultUI: true,
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.SMALL,
            position: google.maps.ControlPosition.LEFT_CENTER
        }
    }
    $scope.map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);
    //$scope.mobilemap = new google.maps.Map(document.getElementById('mobgooglemap'), mapOptions);
    $scope.mobilemap;
    $scope.markers = [];
    $scope.dirmarkers=[];
    $scope.mdirmarkers=[];
    var latlongcollection = [];
    $scope.shopdistance;
    $scope.reviewPage = 1;
    $scope.reviewtotalpage;
    $scope.totalItems;
    $scope.itemLimit = 10;
    $scope.currentPage = 1;
    $scope.directionlocation='';
    $scope.arealocation=['Porur, Chennai, Tamil Nadu, India','Ramapuram, Chennai, Tamil Nadu, India','Iyappanthangal, Chennai, Tamil Nadu, India','Valasaravakkam, Chennai, Tamil Nadu, India'];
    $scope.showpromo=false;
    var top;
    var serviceheight;
    var data;        

    $scope.timeFilter =  function (value) {
        if(typeof value != 'undefined')
        {            
            var split = value.split(':');
            if (split[0] - 12 > 0) {
                returnval = split[0] - 12 + ":" + split[1] + " PM";
            }
            else if((split[0] - 12 < 0)) {
                returnval = split[0] + ":" + split[1] + " AM";
            }                
            else
            {
                returnval = split[0] + ":" + split[1] + " PM";
            }
            return returnval;
        }
        else
        {
            return ""
        }
    }

    $scope.getprice_rating = function (index, studio) {  
        var rating=studio.avg_rating;   
        if(studio.avg_rating!=0 || studio.avg_rating!=null){
            rating = Math.round(studio.avg_rating);            
        }        
        $scope.studio[index].rating = rating;
        $scope.filteredstudio[index].rating = rating;            
        $scope.filteredstudio[index].staricon=$scope.stariconset[rating];
        $scope.studio[index].staricon=$scope.stariconset[rating];        
    }

        //Google Maps    
    var imagUrls = {                
        iconsaloon:'../static/img/saloon.png',
        iconparlor:'../static/img/beautyparlor.png',
        iconspa:'../static/img/spa.png',
        iconuser:'../static/img/user.png',
        iconsaloonselect:'../static/img/saloon-select.png',
        iconparlorselect:'../static/img/beautyparlor-select.png',
        iconspaselect:'../static/img/spa-select.png',
        iconuserselect:'../static/img/user-select.png'
    };
    var images = {        
        iconsaloon: new google.maps.MarkerImage(imagUrls.iconsaloon),
        iconparlor: new google.maps.MarkerImage(imagUrls.iconparlor),
        iconspa: new google.maps.MarkerImage(imagUrls.iconspa),
        iconuser:new google.maps.MarkerImage(imagUrls.iconuser),
        iconsaloonselect: new google.maps.MarkerImage(imagUrls.iconsaloonselect),
        iconparlorselect: new google.maps.MarkerImage(imagUrls.iconparlorselect),
        iconspaselect: new google.maps.MarkerImage(imagUrls.iconspaselect),
        iconuserselect:new google.maps.MarkerImage(imagUrls.iconuserselect)
    };
    var bounds = new google.maps.LatLngBounds();
    var createmarker = function (studio) {        
        var mousein,mouseout;
        if(studio.type_desc=="Salon"){
            mousein=images.iconsaloonselect;
            mouseout=images.iconsaloon;
        }
        else if(studio.type_desc=="Spa"){
            mousein=images.iconspaselect;
            mouseout=images.iconspa;
        }
        else{
            mousein=images.iconparlorselect;
            mouseout=images.iconparlor;
        }
        var marker = new google.maps.Marker({
            map: $scope.map,
            position: new google.maps.LatLng(studio.latitude, studio.longitude),
            title: studio.name,            
            icon: mouseout,
            mover:mousein,
            mout:mouseout
        });
        var compiled;
        if(typeof studio.distance !="undefined"){
            compiled = $compile('<div class="map-tooltip-panel"><div class="details"><img class="image loaded" style="height: 100px;" alt="" src='+studio.thumbnail+'><div class="info"><div class="heading"><h4>'+ studio.name + '</h4></div><div style="color: #4c4c4c;font-size: 12px;width: 150px;line-height: 17px;">'+ studio.address_1 +'</div><div class="sub-line-2"><span>'+ studio.distance +' km</span><span class="price"><span class="icon-rupee rupee"></span><span class="info-rate"><i class="fa fa-inr"></i>'+ studio.min_price +'+</span></span></div></div></div></div>')($scope);            
        }        
        else{
            compiled = $compile('<div class="map-tooltip-panel"><div class="details"><img class="image loaded" style="height: 100px;" alt="" src='+studio.thumbnail+'><div class="info"><div class="heading"><h4>'+ studio.name + '</h4></div><div style="color: #4c4c4c;font-size: 12px;width: 150px;line-height: 17px;">'+ studio.address_1 +'</div><div class="sub-line-2"><span class="price"><span class="icon-rupee rupee"></span><span class="info-rate"><i class="fa fa-inr"></i>'+ studio.min_price +'+</span></span></div></div></div></div>')($scope);
        }
        marker.content = compiled[0];
        google.maps.event.addListener(marker, 'click', function () {
            if (infoWindow) infoWindow.close();
            infoWindow.setContent(marker.content);
            infoWindow.open($scope.map, marker);
        });
        google.maps.event.addListener(marker, 'mouseover', function (event) {            
            this.setIcon(marker.mover);
        });
        google.maps.event.addListener(marker, 'mouseout', function (event) {
            this.setIcon(marker.mout);
        });
        $scope.markers.push(marker);
        var latlong = new google.maps.LatLng(studio.latitude, studio.longitude);
        latlongcollection.push(latlong);
    }
    $scope.addmarker = function (start, end) {
        google.maps.event.trigger($scope.map, 'resize');
        var sortfilter = $filter('orderBy')($scope.filteredstudio, $scope.direction ? '-' + $scope.orderProp : $scope.orderProp);
        if (sortfilter.length > 0) {
            for (i = start ; i < end; i++) {
                if (i < sortfilter.length) {
                    createmarker(sortfilter[i]);
                }
            }
        }
        $scope.map.fitBounds(bounds);
    }
    $scope.hoverIn = function (studioname) {
        var selectedmarker;
        var keepgoing = true;
        angular.forEach($scope.markers, function (marker) {
            if (keepgoing) {
                if (marker.title == studioname) {
                    keepgoing = false;
                    selectedmarker = marker;
                }
            }
        });
        if(typeof selectedmarker !='undefined'){
            google.maps.event.trigger(selectedmarker, 'mouseover');
        }  
    }
    $scope.hoverOut = function (studioname) {
        if($('#studiodetails').css('display') == 'block')
        {
           return false
        }
        var selectedmarker;
        var keepgoing = true;
        angular.forEach($scope.markers, function (marker) {
            if (keepgoing) {
                if (marker.title == studioname) {
                    keepgoing = false;
                    selectedmarker = marker;
                }
            }
        });
        if(typeof selectedmarker !='undefined'){
            google.maps.event.trigger(selectedmarker, 'mouseout');
        }        
    }
    function removemarker() {
        angular.forEach($scope.markers, function (marker) {
            marker.setMap(null);
        });
        var end = $scope.markers.length;
        for (var i = 0; i < end; i++) {
            $scope.markers.splice(0, 1);
        }
    }
    function removedirmarker() {
        angular.forEach($scope.dirmarkers, function (marker) {
            marker.setMap(null);
        });
        var end = $scope.dirmarkers.length;
        for (var i = 0; i < end; i++) {
            $scope.dirmarkers.splice(0, 1);
        }
        angular.forEach($scope.mdirmarkers, function (marker) {
            marker.setMap(null);
        });
        end = $scope.mdirmarkers.length;
        for (var i = 0; i < end; i++) {
            $scope.mdirmarkers.splice(0, 1);
        }        
    }
    function autozoom() {
        var latlngbounds = new google.maps.LatLngBounds();
        for (var i = 0; i < latlongcollection.length; i++) {
            latlngbounds.extend(latlongcollection[i]);
        }
        $scope.map.fitBounds(latlngbounds);
        $scope.map.panToBounds(latlngbounds);
    }
    function clearlatlongbound() {
        var end = latlongcollection.length;
        for (var i = 0; i < end; i++) {
            latlongcollection.splice(0, 1);
        }
    }
    function drawdirection(studiotype, lat, lon) {           
        $scope.mobilemap = new google.maps.Map(document.getElementById('mobgooglemap'), mapOptions);  
        directionsDisplay.setMap($scope.map);
        directionsDisplay.setOptions({ suppressMarkers: true });
        mdirectionsDisplay.setMap($scope.mobilemap);
        mdirectionsDisplay.setOptions({ suppressMarkers: true });
        var request = {
            origin: new google.maps.LatLng(lat, lon),
            destination: $scope.directionlocation,
            travelMode: google.maps.DirectionsTravelMode.DRIVING
        };
        directionsService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                var starticon;
                $scope.distance = response.routes[0].legs[0].distance.text;                
                if(studiotype=="Salon"){
                    starticon=images.iconsaloon;
                }
                else if(studiotype=="Spa"){
                    starticon=images.iconspa;
                }
                else{
                    starticon=images.iconparlor;
                }
                makeMarker(response.routes[0].legs[0].start_location, starticon);
                makeMarker(response.routes[0].legs[0].end_location, images.iconuser);                
                $scope.$apply();                
                directionsDisplay.setDirections(response);                
                mdirectionsDisplay.setDirections(response);                    
            }
        });
    }
    function makeMarker(position, icon) {
        var marker=new google.maps.Marker({
            position: position,
            map: $scope.map,
            icon: icon        
        });        
        $scope.dirmarkers.push(marker)
        $scope.mdirmarkers.push(new google.maps.Marker({position: position,map: $scope.mobilemap,icon: icon}));
    }

$scope.bindstudio=function(data){ 
    $scope.studio=[];
    $scope.filteredstudio=[];     
    if(data.length>0){  
        $scope.totalItems=data.length;    
        var random=randomIntFromInterval(1,5);    
        angular.forEach(data, function (value, key) {                       
            $scope.studio.push(value);            
            $scope.filteredstudio.push(value);            
            $scope.getprice_rating(key, value);
            var kind=lodash.where($scope.studiokind,{'id':value.studio_kind})[0];
            var type=lodash.where($scope.studiotype,{'id':value.studio_type})[0];
            $scope.studio[key].kind_icon = kind.icon;
            $scope.studio[key].kind_desc = kind.name;
            $scope.studio[key].type_icon = type.icon;
            $scope.studio[key].type_desc = type.name;  
            $scope.studio[key].showpromo=$scope.showpromo;
            $scope.studio[key].zaloonoffer=0;
            if(!$scope.showpromo){
                if((key%5)+1==random){
                    $scope.studio[key].zaloonoffer=$scope.studio[key].commission_percent-3;
                }                 
            }                                
        });           
        getgeocode($scope.searchdata.location); 
        $scope.totalItems = $scope.filteredstudio.length;        
    }
    else{
        getlatlong($scope.searchdata.location)    
        $scope.totalItems = $scope.filteredstudio.length;    
    }
    
}

    function getlatlong(location){
        var obj={};
        //var geocoder =  new google.maps.Geocoder();
        geocoder.geocode( { 'address': location}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                obj['latitude']=results[0].geometry.location.lat();
                obj['longitude']=results[0].geometry.location.lng();
                plotmarker(obj.latitude,obj.longitude)              
            }
            else{
                geocoder.geocode( { 'address': "India"}, function(res, stu) {
                    if (stu == google.maps.GeocoderStatus.OK) {
                        obj.latitude=res[0].geometry.location.lat();
                        obj.longitude=res[0].geometry.location.lng();
                    }
                });
            }
        });
        
    }
    function plotmarker(latitude,longitude){
        google.maps.event.trigger($scope.map, 'resize');
        var marker = new google.maps.Marker({
                map: $scope.map,
                position: new google.maps.LatLng(latitude, longitude)            
            });        
            $scope.markers.push(marker);
            var latlong = new google.maps.LatLng(latitude, longitude);
            latlongcollection.push(latlong);
            $scope.map.fitBounds(bounds);
            autozoom();
    }

    function getdistance(key, lat, lon) {        
        var studiogeo = new google.maps.LatLng(lat, lon);
        var searchgeo = new google.maps.LatLng($scope.searchplace['lat'], $scope.searchplace['lon']); 
        $scope.studio[key].distance =parseFloat(google.maps.geometry.spherical.computeDistanceBetween(searchgeo, studiogeo)/1000).toFixed(2);       
    }

    function getgeocode(place){        
        //var geocoder =  new google.maps.Geocoder();
        geocoder.geocode( { 'address': place}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                $scope.searchplace['lat']=results[0].geometry.location.lat();
                $scope.searchplace['lon']=results[0].geometry.location.lng();                
                angular.forEach($scope.studio, function (value, key) {
                    getdistance(key, value.latitude, value.longitude); 
                });
                $scope.$apply();
                $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
                autozoom();               
            }
        });
    }

    //Filter
    $scope.clkmore = function () {
        if($('#devicefilter').css('display') == 'none'){
            $('#searchdevice').hide();
        }
        $scope.searchicon=false;
        if($('#studiodetails').css('display') != 'none'){
            $scope.closeslider();
        } 
        if(!$scope.morefilter){            
            $scope.tempstudiotypefilter= [];
            $scope.tempstudiokindfilter = [];
            $scope.tempstudioratingfilter = [];            
            $scope.tempstudiotypefilter = angular.copy($scope.studiotypefilter);
            $scope.tempstudiokindfilter = angular.copy($scope.studiokindfilter);
            $scope.tempstudioratingfilter = angular.copy($scope.studioratingfilter);            
        }
        else{            
            $scope.undofilter();
        }
        $scope.morefilter = !$scope.morefilter;
    }

    $scope.undofilter=function(){
        $scope.studiotypefilter = angular.copy($scope.tempstudiotypefilter);
        $scope.studiokindfilter = angular.copy($scope.tempstudiokindfilter);
        $scope.studioratingfilter = angular.copy($scope.tempstudioratingfilter);        
        angular.forEach($scope.studiotype,function(val,index){
            $scope.studiotype[index].active=false;                
            if ($scope.studiotypefilter.indexOf(val.name) != -1) {
                $scope.studiotype[index].active=true;
            }                
        })
        angular.forEach($scope.studiokind,function(val,index){
            $scope.studiokind[index].active=false;                
            if ($scope.studiokindfilter.indexOf(val.name) != -1) {
                $scope.studiokind[index].active=true;
            }                
        })
        angular.forEach($scope.studiostar,function(val,index){
            $scope.studiostar[index].active=false;                
            if ($scope.studioratingfilter.indexOf(val.star) != -1) {
                $scope.studiostar[index].active=true;
            }                
        })        
    }

    $scope.studiotypeclick = function (type, index) {
        $scope.studiotype[index].active = !$scope.studiotype[index].active;
        if ($scope.studiotypefilter.indexOf(type) == -1) {
            $scope.studiotypefilter.push(type);
        }
        else {
            $scope.studiotypefilter.splice($scope.studiotypefilter.indexOf(type), 1);
        }
    }

    $scope.studiokindclick = function (kind, index) {
        $scope.studiokind[index].active = !$scope.studiokind[index].active;
        if ($scope.studiokindfilter.indexOf(kind) == -1) {
            $scope.studiokindfilter.push(kind);
        }
        else {
            $scope.studiokindfilter.splice($scope.studiokindfilter.indexOf(kind), 1);
        }
    }

    $scope.studioreviewclick = function (star, index) {
        $scope.studiostar[index].active = !$scope.studiostar[index].active;
        if ($scope.studioratingfilter.indexOf(star) == -1) {
            $scope.studioratingfilter.push(star);
        }
        else {
            $scope.studioratingfilter.splice($scope.studioratingfilter.indexOf(star), 1);
        }
    }    

    $scope.applyfilter = function () {
        if($('#studiodetails').css('display') == 'block')
        {
            $scope.closeslider();
        }        
        var tempfilter = [];
        angular.forEach($scope.studio, function (studio, key) {
            var isfilter;
            isfilter = $scope.customfilter(studio);
            if (isfilter) {
                tempfilter.push(studio);
            }
        });
        $scope.filteredstudio = tempfilter;
        $scope.totalItems = $scope.filteredstudio.length;
        removemarker();
        clearlatlongbound();
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
        $scope.morefilter = !$scope.morefilter;
    }

    $scope.resetfilter = function () {        
        angular.forEach($scope.studiotype, function (value, index) {
            value.active = false;
        });
        angular.forEach($scope.studiokind, function (value, index) {
            value.active = false;
        });
        angular.forEach($scope.studiostar, function (value, index) {
            value.active = false;
        });
        $scope.studiotypefilter = [];
        $scope.studiokindfilter = [];
        $scope.studioratingfilter = [];        
        $('input:checkbox').removeAttr('checked');
        $scope.applyfilter();
    }

    $scope.customfilter = function (studio) {
        if ($scope.studiotypefilter.length != 0 || $scope.studiokindfilter.length != 0 || $scope.studioratingfilter.length != 0 ) {
            var returnvalue;
            returnvalue = $scope.checkstudiotype(studio);
            if (returnvalue) {
                returnvalue = $scope.checkstudiokind(studio);
            }
            if (returnvalue) {
                returnvalue = $scope.checkstudiorating(studio);
            }            
            return returnvalue;
        }
        else {
            return true;
        }
    }

    $scope.checkstudiotype = function (studio) {
        if ($scope.studiotypefilter.length != 0) {
            if ($scope.studiotypefilter.indexOf(studio.type_desc) == -1) {
                return false;
            }
            else {
                return true;
            }
        }
        else {
            return true;
        }
    }

    $scope.checkstudiokind = function (studio) {
        if ($scope.studiokindfilter.length != 0) {
            if ($scope.studiokindfilter.indexOf(studio.kind_desc) == -1) {
                return false;
            }
            else {
                return true;
            }
        }
        else {
            return true;
        }
    }

    $scope.checkstudiorating = function (studio) {
        if ($scope.studioratingfilter.length != 0) {
            if ($scope.studioratingfilter.indexOf(studio.rating) == -1) {
                return false;
            }
            else {
                return true;
            }
        }
        else {
            return true;
        }
    }    

    $scope.sortchange=function(selectitem){        
        if(selectitem!=null){
            $scope.orderProp = selectitem.property;
            $scope.direction = selectitem.direction;
        } 
        else{
            $scope.orderProp = 'min_price';
            $scope.direction = false;    
        }
        removemarker();
        clearlatlongbound();
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
    }

    $scope.confirm=function(id){
        if(typeof $scope.selectedstudio.id != "undefined"){
            if($scope.selectedstudio.id!=id && $scope.selected_service.length>0){
                $scope.confirmid=id;
                $('#confirmmodal').modal('show');
            }
            else{
                $scope.studiodetails(id);
            }
        }
        else
        {
            $scope.studiodetails(id);
        }
    }

    $scope.confirmok=function(id){
        $('#confirmmodal').modal('hide');
        $scope.studiodetails(id);
    }

    $scope.studiodetails = function (id) {    
        var windowWidth = $(window).width();
        if (windowWidth >= 993) {
            var tut2=$cookies.get('tut2cookie');
            if(typeof tut2 == 'undefined'){
                $('#tutorialslideroverlay').addClass('tutorialoverlay');
                $('#tutorialslideroverlay').show();
                console.log("Remove later")
            }
            else{
                $('#tutorialslideroverlay').removeClass('tutorialoverlay');
                $('#tutorialslideroverlay').hide();
            }    
        }
        var samestudio=false;          
        $('.service-overlay').show();         
        if(typeof $scope.selectedstudio.id != "undefined"){
            if($scope.selectedstudio.id!=id){
                $scope.selected_service = [];  
                $scope.serviceprice = 0;  
                $scope.serviceduration=0;            
            }  
            else{
                samestudio=true;
            }
        }            
        $scope.servicelist = [];
        $scope.selectedstudio = {};
        $scope.sergroup={};
        var studio = lodash.where($scope.studio, { 'id': id });        
        if (studio.length > 0) {
            $('.detail-tab').removeClass('active');
            $('.tab-street').addClass('active');
            if($('.navsearch').css('display') != "none"){
               $('#searchdevice').hide();
            }
            serviceheight=0;            
            $scope.searchicon=false;
            $scope.morefilter=false;
            $scope.selectedstudio = studio[0];       
            console.log($scope.selectedstudio)     
            $scope.has_online_payment = $scope.selectedstudio.has_online_payment;            
            //$scope.sortservicebyfilter();
            $('.header-tabs').removeClass('stick');
            $('.header-tabs').removeClass('stick-mobile');
            $('.header-tabs').removeClass('stick-tablet');
            $('.header-tabs').removeClass('stick-lap');
            $('#studiodetails').toggle('slide', { direction: 'right' }, 200);
            $scope.reviewPage = 1;            
            $scope.directionlocation=$scope.searchdata_.searchlocation;
            serviceheight= $('.service-list').height();            
            $scope.shopdistance = $scope.selectedstudio.distance;   
            if($scope.selectedstudio.daily_studio_closed_from == null){
                $scope.selectedstudio.daily_studio_duration=$scope.calculate($scope.selectedstudio.opening_at,$scope.selectedstudio.closing_at);
            }         
            else{
                var fn=$scope.calculate($scope.selectedstudio.opening_at,$scope.selectedstudio.daily_studio_closed_from);
                var an=$scope.calculate($scope.selectedstudio.daily_studio_closed_till,$scope.selectedstudio.closing_at);
                if(fn>an){
                    $scope.selectedstudio.daily_studio_duration=fn;
                }
                else{
                    $scope.selectedstudio.daily_studio_duration=an
                }
            }            
            setTimeout(function(){
                top = { 'street-info': $('.street-info').position().top, 'service-list': $('.service-list').position().top, 'review-detail': $('.review-detail').position().top, 'direction': $('.direction').position().top };
                //console.log(top);
                removemarker();                
                drawdirection($scope.selectedstudio.type_desc,$scope.selectedstudio.latitude, $scope.selectedstudio.longitude);                
            },300);
            setTimeout(function () {                                   
                httpServices.getServicebyid({id:id}).then(function(res)
                {                                     
                    $scope.sortservicebyfilter(res['service_details'].data[0].studio_detail_for_activity);                
                    $scope.selectedstudio.studio_review=res['service_details'].data[0].studio_review;
                    var page = Math.floor($scope.selectedstudio.studio_review.length / 5);                   
                    page = page + ($scope.selectedstudio.studio_review.length % 5 > 0 ? 1 : 0);                  
                    $scope.reviewtotalpage = page;                
                    if(samestudio){
                        $scope.updateselectedflag();
                    }        
                },function()
                {
                    console.log("Try again to get service")
                });
            }, 500);
             
        }
    }

    $scope.sortservicebyfilter = function (studioactivity) {        
        $scope.servicelist = [];         
        var res = lodash.where(studioactivity, { service: { service_type: $scope.searchdata.service } });
        var stugroup =lodash.groupBy($scope.studioservicegroup, 'id');             
        angular.forEach(res,function(service,key){            
            var sergroupname=stugroup[service.service.service_type][0].service_name;
            $scope.servicelist.push({id:service.service.id,servicename: service.service.service_name, price: service.price, flag: false , duration:service.mins_takes,isactive:service.is_active, servicegroupid:service.service.service_type, servicegroupname:sergroupname, servicefor : service.service.service_for });
        });        
        angular.forEach(studioactivity, function (service, key) {       
            if (lodash.findIndex($scope.servicelist, { 'id': service.service.id }) == -1) {
                var sergroupname=stugroup[service.service.service_type][0].service_name;
                $scope.servicelist.push({id:service.service.id, servicename: service.service.service_name, price: service.price, flag: false, duration:service.mins_takes,isactive:service.is_active, servicegroupid:service.service.service_type ,servicegroupname:sergroupname, servicefor : service.service.service_for});
            }
        });    
        $scope.sergroup=lodash.groupBy($scope.servicelist,'servicegroupname');             
        $('.service-overlay').hide();
        setTimeout(function () {           
            var tempheight=serviceheight;                     
            serviceheight=$('.service-list').height();            
                top = { 'street-info': top['street-info'], 'service-list': top['service-list'], 'review-detail': ((top['review-detail']-75)+serviceheight), 'direction': ((top['direction']-75)+serviceheight) };                
            }, 2000);             
    }

    $scope.updateselectedflag=function(){       
        angular.forEach($scope.selected_service,function(service,key){            
            var index=lodash.findIndex($scope.servicelist, { 'id': service.id });            
            if(index!=-1){
                $scope.servicelist[index].flag=true;
            }
        });
    }

    $scope.easyscroll = function (clsname,tab) {    
        if($(window).width() <= 480){            
            $('.list-detail-box').animate({
                scrollTop: top[clsname] - 92
            }, 100);
        }        
        else if($(window).width() >= 481 && $(window).width() <= 767){            
            $('.list-detail-box').animate({
                scrollTop: top[clsname] - 100
            }, 100);
        }
        else if($(window).width() >= 768 && $(window).width() <= 991){            
            $('.list-detail-box').animate({
                scrollTop: top[clsname] - 105
            }, 200);
        }
        else{            
            $('.list-detail-box').animate({
                scrollTop: top[clsname] - 140
            }, 200);
        } 
        setTimeout(function(){
            $('.detail-tab').removeClass('active');
            $('.'+tab).addClass('active');   
        },250);        
    }

    //function to open maps app in touch devices
    $scope.openMap = function()
    {
        var start_add = $scope.directionlocation
        var lat = $scope.selectedstudio.latitude
        var longt = $scope.selectedstudio.longitude
        if($scope.which_device ==1 ) //open apple maps in apple devices
        {
            //http://www.google.com/maps/place/49.46800006494457,17.11514008755796/@49.46800006494457,17.11514008755796,17z
            window.open("http://maps.apple.com/?z=12&q="+lat+","+longt)
            //window.open("comgooglemaps://?saddr="+lat+","+longt);
            //window.open("comgooglemaps://?saddr=Google+Inc,+8th+Avenue,+New+York,+NY&daddr=John+F.+Kennedy+International+Airport,+Van+Wyck+Expressway,+Jamaica,+New+York&directionsmode=transit");
        }
        else if($scope.which_device ==2) //open google maps in android
        {
            window.open("comgooglemaps://?saddr="+lat+","+longt+"&amp;ll=");
        }
        else
        {
            return false
        }
        
    
    }
    $scope.closeslider = function () {     
        //$scope.selectedstudio = {}   
        $('#studiodetails').toggle('slide', { direction: 'right' }, 200);
        //$scope.selected_service = [];
        $scope.servicelist = []; 
        setTimeout(function(){
            directionsDisplay.setMap(null);
            mdirectionsDisplay.setMap(null);
            removedirmarker();
            clearlatlongbound();
            $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
            autozoom();
        },300);                
    }

    $scope.servicecart=function(){                
        if($scope.selected_service.length == 0){
            $scope.has_online_payment=true;
            $scope.bookdisable=true;
        }
        else{
            $scope.bookdisable=false;
        }
        $('#cartmodal').modal('show');
    }

    $scope.removeselectedservice=function(service){        
        var idx = lodash.findIndex($scope.servicelist, service);       
        var index = lodash.findIndex($scope.selected_service, service);
        $scope.selected_service.splice(index, 1);
        //$scope.servicelist.splice(idx, 1);
        $scope.servicelist[idx].flag = false;
        $scope.serviceprice = $scope.serviceprice - service.price;
        $scope.serviceduration=$scope.serviceduration-service.duration; 
        if($scope.selected_service.length == 0){
            $scope.has_online_payment=true;
            $scope.bookdisable=true;
        }   
        else{
            $scope.bookdisable=false;
        }  
    }

    $scope.filterfor = function(service) {
        //console.log(service)
        if($scope.serviceforselect == 0) {
            return true;
        }
        else {
            if(service.servicefor == $scope.serviceforselect){
                return true;
            }
            else{
                return false;
            }
        }
    }

    $scope.serviceforclick = function(id) {        
        angular.forEach($scope.servicefor,function(service,key){          
            $scope.servicefor[key].active=false;
        });
        $scope.servicefor[id].active = true;
        $scope.serviceforselect = id;
    }

    $scope.morereview = function () {
        $scope.reviewPage = $scope.reviewPage + 1;
    }

    $scope.firstreview = function()
    {
        $scope.reviewPage = 1;   
    }

    $scope.changedirection=function(studiotype){        
        directionsDisplay.setMap(null);
        mdirectionsDisplay.setMap(null);
        removedirmarker();
        drawdirection(studiotype ,$scope.selectedstudio.latitude, $scope.selectedstudio.longitude);        
        geocoder.geocode( { 'address': $scope.directionlocation}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {                
                var studiogeo = new google.maps.LatLng($scope.selectedstudio.latitude, $scope.selectedstudio.longitude);
                var searchgeo = new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng()); 
                $scope.shopdistance = parseFloat(google.maps.geometry.spherical.computeDistanceBetween(searchgeo, studiogeo)/1000).toFixed(2);                
                $scope.$apply();
            }
        });        
    }
    
    $scope.addservice = function (from,service) {       
        var index = lodash.findIndex($scope.servicelist, service);
        var flag = $scope.servicelist[index].flag;
            
        if (flag) {                        
            var inx=lodash.findIndex($scope.selected_service, { 'servicename': service.servicename });
            $scope.servicelist[index].flag = !$scope.servicelist[index].flag;   
            $scope.selected_service.splice(inx, 1);
            $scope.serviceprice = $scope.serviceprice - service.price;
            $scope.serviceduration=$scope.serviceduration-service.duration;
        }
        else 
        {   
            if($scope.selectedstudio.daily_studio_duration>=$scope.serviceduration+service.duration){
                $scope.servicelist[index].flag = !$scope.servicelist[index].flag;   
                $scope.selected_service.push(service);            
                $scope.serviceprice = $scope.serviceprice + service.price;
                $scope.serviceduration=$scope.serviceduration+service.duration;
            }  
            else{
                if(from=="slider"){
                    $('#serviceinfomodal').modal('show');
                    return false;   
                }
                else{
                        $('#serviceinfomodal').modal('show');
                    return false;  
                }
            }          
        } 
        //console.log($scope.sergroup)         
    }

    $scope.calculate=function(start,closed) {        
         var time1 = start.split(':'), time2 = closed.split(':');
         var hours1 = parseInt(time1[0], 10), 
             hours2 = parseInt(time2[0], 10),
             mins1 = parseInt(time1[1], 10),
             mins2 = parseInt(time2[1], 10);
         var hours = hours2 - hours1, mins = 0;
         if(hours < 0) hours = 24 + hours;
         if(mins2 >= mins1) {
             mins = mins2 - mins1;
         }
         else {
             mins = (mins2 + 60) - mins1;
             hours--;
         }
         mins = mins / 60; // take percentage in 60
         hours += mins;
         hours = hours.toFixed(2);
         hours=hours*60
         return hours;
     }

    //Pagination
    $scope.pagechange = function () {      
        removemarker();
        clearlatlongbound();        
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
    }
    //AutoComplete    
    $scope.areacomplete = function (val) { 
         return gService.getPlace(val).then(function (data) {           
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
    $scope.ondirectionselect = function ($item, $model, $label) {
        if($label!="Notfound"){
            $scope.directionlocation=$label;
        }
        else{           
            $scope.directionlocation="";
        }        
    };
    $scope.searchservicestudio=function(){    
        var idx=lodash.findIndex($scope.studioservicegroup, { service_name: $scope.searchdata_.servicename.trim() });        
        if (idx != -1) {
            if($('.navsearch').css('display') != "none"){
                $('#searchdevice').hide();
            }            
            $scope.searchicon=false;        
            removemarker();
            removedirmarker();
            clearlatlongbound();
            var obj={'service':$scope.studioservicegroup[idx].id,'location':$scope.searchdata_.searchlocation,'servicename':$scope.studioservicegroup[idx].service_name};
            $('#lister').hide();
            $('#loading').show();
            $('#lister1').hide();
            httpServices.getstudioDetails(obj).then(function(data)
            {            
                $cookies.putObject('searchdata',obj,{path:'/'});   
                $scope.searchdata=obj;                  
                putResultService.setresult(data.studio_details.data);
                $scope.studiotypefilter = [];
                $scope.studiokindfilter = [];
                $scope.studioratingfilter = [];        
                $('input:checkbox').removeAttr('checked');
                $scope.bindstudio(data.studio_details.data); 
                setTimeout(function(){
                    $('#lister').show();
                    $('#loading').hide();
                    $('#lister1').show();
                },500);                                
            },function()
            {
                console.log("Try again to get service")
            });
            if($('#studiodetails').css('display') != 'none'){
                $('#studiodetails').hide();
                directionsDisplay.setMap(null);
                mdirectionsDisplay.setMap(null);
                clearlatlongbound();
            }            
        }        
    }

    $scope.searchdata=$cookies.getObject('searchdata');    
    $scope.searchdata_ = {};    
    $('.finder-overlay').hide();
    if(typeof $scope.searchdata == "undefined"){
        $location.path("/");
    }
    else
    {
        $scope.searchdata_.servicename=$scope.searchdata.servicename;
        $scope.searchdata_.searchlocation=$scope.searchdata.location;
        if(putResultService.getresult().length ==0){
            $('.finder-overlay').show();
            httpServices.getstudioDetails($scope.searchdata).then(function(res)
                {                           
                    data=res.studio_details.data;
                    putResultService.setresult(res.studio_details.data);  
                    $scope.bindstudio(data);                                                  
                    $('.finder-overlay').hide();
                    var windowWidth = $(window).width();
                    if (windowWidth >= 993) {
                        var tut1=$cookies.get('tut1cookie');
                        if(typeof tut1 == 'undefined'){
                            $('#tutorialoverlay').addClass('tutorialoverlay');
                            $('#tutorialoverlay').show();
                        }
                        else{
                            $('#tutorialoverlay').removeClass('tutorialoverlay');
                            $('#tutorialoverlay').hide();
                        }
                    }
                },function()
                {
                    console.log("Try again to get service");
                    $('.finder-overlay').hide();
                    $location.path("/");
                });
        }
        else{            
            data=putResultService.getresult(); 
            $scope.bindstudio(data);
            var windowWidth = $(window).width();
            if (windowWidth >= 993) {
                var tut1=$cookies.get('tut1cookie');
                if(typeof tut1 == 'undefined'){
                    $('#tutorialoverlay').addClass('tutorialoverlay');
                    $('#tutorialoverlay').show();
                }
                else{
                    $('#tutorialoverlay').removeClass('tutorialoverlay');
                    $('#tutorialoverlay').hide();
                }
            }
        }
    }

$(document).click(function(e) {              
    if ($(e.target).is('#tutorialoverlay')) {            
        var now = new Date(),exp = new Date(now.getFullYear(), now.getMonth(), now.getDate()+1);
        var exp = new Date();
        exp.setTime(exp.getTime() + (24*60*60*1000));    
        $cookies.put('tut1cookie','tut1',{path:'/',expires: exp}); 
        $('#tutorialoverlay').removeClass('tutorialoverlay');
        $('#tutorialoverlay').hide();
    }
    else if ($(e.target).is('#tutorialslideroverlay')) {        
        var now = new Date(),exp = new Date(now.getFullYear(), now.getMonth(), now.getDate()+1);
        var exp = new Date();
        exp.setTime(exp.getTime() + (24*60*60*1000));    
        $cookies.put('tut2cookie','tut2',{path:'/',expires: exp}); 
        $('#tutorialslideroverlay').removeClass('tutorialoverlay');
        $('#tutorialslideroverlay').hide();
    }
});

$scope.inviteflag = null
$scope.emailid = null
$scope.lp_invited = false
$scope.formsubmit=false;
$scope.notify_user = {}
$scope.notify_user['email'] = null
$scope.invite = function(form)
{

    $scope.formsubmit=true;
    if(form.$valid)
    {
        $scope.lp_invited = true;
        $scope.notify_user['area'] = $scope.searchdata.location
        httpServices.userAreaInterest($scope.notify_user).then(function(res)
        {
            //successfully added
            $scope.inviteflag = 1
        }, function()
        {
            //cant add error
            $scope.lp_invited = false
            $scope.inviteflag = 0
        })
    }
}


$scope.su_booking = false
//set booking details
$scope.book = function()
{
    if($scope.selected_service.length == 0)
    {
        $('#infomodal').modal('show');
        return false;    
    }
    $scope.to_booking_flag = 1;
    $('#servicemodel').modal('hide');
    if($scope.is_logged != 1)
    {
        $('#signupmodel').modal('show');
        //emit booking services and studio details
    }
    else
    {
        $scope.su_booking = true
        var booking_data = {'studio':$scope.selectedstudio,'services':$scope.selected_service,  
        'user_details':$scope.user_details}        
        putResultService.setSelectedservice(booking_data)        
        $location.path('/booking')
        //$scope.su_booking = false
    }
}

$scope.closemodel=function(){
    $('#signupmodel').modal('hide');
    $('#cartmodal').modal('hide');
    $('#servicemodelbox').modal('hide');
}

//fb keys
$scope.fb_key = httpServices.getFBKey() 
/*
httpServices.getFBKey().then(function(data)
{
    $scope.fb_key = data['fb_key'].data
});*/
$scope.login = function() {
    $facebook.login().then(function() {
      refresh();
    });
  }
  function refresh() {
    $facebook.api("/me").then( 
      function(response) {  
        $('#signupmodel').modal('hide');
        $('#cartmodal').modal('hide');
        $('#servicemodelbox').modal('hide');        
        var token=$facebook.getAuthResponse();
        $scope.fbLogin(token.accessToken);        
        $scope.user_name =response.name;
      },
      function(err) {
        $scope.welcomeMsg = "Please log in";
      });
  }  
$scope.fbLogin = function(dummy)
{    
    $('.loader-overlay').show();
    //$('#signupmodel').modal('hide');
    //$('#cartmodal').modal('hide');
    //$('#servicemodelbox').modal('hide');
    httpServices.loginUsingFB(dummy).then(function(data)
    {
        if(data)
        {
            sessionService.setAuthToken(data)
            httpServices.getUsrDetails().then(function(dataz)
            {
                $scope.is_logged = sessionService.isLogged()
                $scope.logging_out = false
                $scope.user_details = dataz['user_details'].data[0]
                $scope.user_name = $scope.user_details.user_acc['first_name']
                $('.loader-overlay').hide();
                //redirect to booking page if clicked book
                if ($scope.to_booking_flag == 1)
                {
                    var booking_data = {'studio':$scope.selectedstudio,'services':$scope.selected_service,  
                'user_details':$scope.user_details}
                    putResultService.setSelectedservice(booking_data)
                    $location.path('/booking')
                }

            }, function()
            {
                $scope.is_logged = sessionService.isLogged()
                $('.loader-overlay').hide();
                $('#signuperrormodal').modal('show');
                console.log("Error getting user data")
            })
        }
    },function()
    {
        //cannot login to fb try again
        $('.loader-overlay').hide();
        $('#signupmodel').modal('hide')
        $('#signuperrormodal').modal('show');
        console.log("Cannot login to FB")
    });
}

function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}

if(sessionService.isLogged())
{
    $scope.logging_out = false
    httpServices.getUsrDetails().then(function(dataz)
    {
        $scope.user_details = dataz['user_details'].data[0]        
        $scope.user_name = $scope.user_details.user_acc['first_name']
    }, function()
    {
        console.log("Error getting user data")  
    })  
}



$scope.logOut = function()
    {   
        $scope.logging_out = true
        httpServices.logOut().then(function(logout_data)
        {
            $cookies.remove('token',{path:'/'});
            $cookies.remove('expiretime',{path:'/'});
            $cookies.remove('refreshtoken',{path:'/'})
            $cookies.remove('client_id',{path:'/'})
            $cookies.remove('client_secret',{path:'/'})
            window.location.reload()
            //$scope.is_logged = sessionService.isLogged();
            
        },
        function()
        {
            console.log("Logout Error")
        })
    }


$scope.searchicon=false;
    $scope.showsearch=function(){
        if($('#searchdevice').css('display') == 'none')
        {
            $('#searchdevice').show();
            $scope.searchicon=true;
        }
        else{
            $('#searchdevice').hide();
            $scope.searchicon=false;
        }
        $scope.morefilter=false;
        if($('#studiodetails').css('display') != 'none'){
            $scope.closeslider();
        }        
    }

    $scope.reloadpage = function()
    {
       //reload page when login error occurs
       window.location.reload() 
    }

    $(document).click(function(e) {  
        if($scope.morefilter){      
            if (!$(e.target).is('#morefilter, #morefilter *')) {        
                $scope.morefilter=false;
                $scope.undofilter();
                $scope.$apply();
            }
        }
    });

});

noqapp.controller('paymentcontroller', function ($scope, $cookies, $location, $window, $sce, lodash, putResultService, httpServices) {
$scope.serviceschosen = [];
$scope.total_duration;
$scope.closed_days = []
var closed_days = $scope.closed_days
$scope.start_date = new Date()
$scope.continueclick=false;
$scope.isdisable = false;
//Added
$scope.coupon_code="";
$("body").css("overflow-x", "hidden");
$("body").css("overflow-y", "scroll");
if(putResultService.getSelectedservice().length !=0){
    $scope.serviceschosen = putResultService.getSelectedservice();
}
else{
    if(typeof $cookies.getObject('searchdata') == "undefined"){
        $location.path("/");
    }
    else{
        $location.path("/search");
    }
}
if ($scope.serviceschosen['services'].length > 1)
{
    $scope.rp_service_txt = $scope.serviceschosen['services'][0].servicename +"+"+String(($scope.serviceschosen['services'].length) - 1) +' services'
    
}
else
{
    $scope.rp_service_txt = $scope.serviceschosen['services'][0].servicename   
}
$scope.user_details = $scope.serviceschosen['user_details']
$scope.mobileno = $scope.user_details.mobile
$scope.total_duration=lodash.sum($scope.serviceschosen.services,'duration');
$scope.total_amount = lodash.sum($scope.serviceschosen.services,'price');
$scope.selected_services = lodash.pluck($scope.serviceschosen.services, 'id');
$scope.promo_amount = 0
$scope.amount_to_pay = $scope.total_amount - $scope.promo_amount
$scope.service_tax = 0
$scope.zaloonoffer=0;
if ($scope.serviceschosen.studio['has_service_tax'] > 0)
{
    $scope.service_tax = Math.round(($scope.amount_to_pay * 14)/100)
}
if(!$scope.serviceschosen.studio['showpromo']){
    if($scope.serviceschosen.studio['zaloonoffer']!=0){
        $scope.zaloonoffer = Math.round(($scope.amount_to_pay * $scope.serviceschosen.studio['zaloonoffer'])/100)
    }
}
$scope.amount_to_pay = ($scope.amount_to_pay + $scope.service_tax)-$scope.zaloonoffer;

angular.forEach($scope.serviceschosen.studio.studio_closed_details, function(value, key) {    
    $scope.closed_days.push(value.closed_on.id-1);    
});
/*if ($scope.start_date.getHours() > 11)
{
    $scope.start_date.setDate($scope.start_date.getDate() + 1);
}*/
$scope.end_date = angular.copy($scope.start_date)
$scope.end_date.setDate($scope.start_date.getDate() + 30);


 $scope.avail = {}


$scope.date_accordion = "accordion-toggle"
$scope.booking_accordion = "accordion-toggle collapsed"
$scope.service_accordion  = "accordion-toggle collapsed"
$scope.openToggle = function(which_toggle)
{
    if($scope.isdisable == true)
    {
        return false;
    }
    if((which_toggle == 'collapseThree') && !($scope.date_selected) && !($scope.from_time))
    {
        return false
    }
    if((which_toggle == 'collapseFour') && !($scope.mobileno))
    {
        return false
    }
    if((which_toggle == 'collapseFour') && ($scope.mobileno))
    {
        val = $scope.makepayment()
        return val
    }
    $('#'+which_toggle).collapse('toggle');
    $('.panel-collapse.in').collapse('hide');
    
    if(which_toggle == 'collapseOne')
    {
        if($scope.service_accordion == "accordion-toggle collapsed")
        {
            $scope.service_accordion  = "accordion-toggle"
        }
        else
        {
            $scope.service_accordion = "accordion-toggle collapsed"   
        }
        $scope.date_accordion = "accordion-toggle collapsed"   
        $scope.booking_accordion = "accordion-toggle collapsed"
        //$scope.payment_accordion = "accordion-toggle"
    }
    if(which_toggle == 'collapseTwo')
    {
        if($scope.date_accordion == "accordion-toggle collapsed")
        {
            $scope.date_accordion  = "accordion-toggle"
        }
        else
        {
            $scope.date_accordion = "accordion-toggle collapsed"   
        }
        $scope.service_accordion = "accordion-toggle collapsed"
        $scope.booking_accordion = "accordion-toggle collapsed"
        //$scope.payment_accordion = "accordion-toggle"
    }
    if(which_toggle == 'collapseThree')
    {
        if($scope.booking_accordion == "accordion-toggle collapsed")
        {
            $scope.booking_accordion  = "accordion-toggle"
        }
        else
        {
            $scope.booking_accordion = "accordion-toggle collapsed"   
        }
        $scope.date_accordion = "accordion-toggle collapsed"
        $scope.service_accordion = "accordion-toggle collapsed"
        //$scope.payment_accordion = "accordion-toggle"
    }

}


var disabled_dates = [];
                $('#datepicker').datepicker({
                   
                    format: "yyyy-mm-dd",
                    startDate: $scope.start_date,
                    endDate: $scope.end_date,
                    daysOfWeekDisabled: $scope.closed_days,
                });

//console.log($('.payment-wrapper').position().top);
$("#datepicker").on("changeDate", function(event) {
    $scope.date_selected = $("#datepicker").datepicker('getFormattedDate')
    var slot_data = {}
    is_today = new Date($scope.date_selected)
    today = new Date()
    $scope.day_crossed = 1;
    if(is_today.getDate() == today.getDate() && is_today.getMonth() == today.getMonth() && (parseInt(today.getHours()) > 4))
    {
        $scope.day_crossed = 0;
    }
    slot_data['services'] = $scope.selected_services
    slot_data['date'] = $scope.date_selected
    slot_data['duration'] = $scope.total_duration
    slot_data['studio_id'] = $scope.serviceschosen.studio.id
    $('.available').removeClass('active'); 
    $scope.from_time='';
    $scope.booking_class1 = "panel panel-default bookingdetails panel-closed"
    $scope.booking_class2 = ""
    $scope.booking_class3 = "panel-heading"
    $('#loading').show();
    $('#slotter').hide();
    $('html, body').animate({
       scrollTop: $('#scrollhere').offset().top + ($(window).height() - $('#scrollhere').outerHeight(true)) 
   }, 200);
    httpServices.getSlots(slot_data).then(function(sdata)
    {
        $('#loading').hide();
        $('#slotter').show();
        $scope.avail = sdata.available_slots.data;  
        $scope.slots_is = 0
       for(key in $scope.avail)
       {
           if($scope.avail[key].length != 0)
           {
               $scope.slots_is = 1
               break
           }
       }      
        //$('html, body').animate({scrollTop: $('#scrollhere').offset().top }, 'slow');
         $('html, body').animate({
        scrollTop: $('#scrollhere').offset().top + ($(window).height() - $('#scrollhere').outerHeight(true)) 
    }, 200);
    },function()
    {
        console.log("Not slots available.Try another date")
    })
    $scope.$apply()

});

$scope.su_couponing = false
$scope.applyPromo = function()
{
    var coupon_data = {};
    coupon_data['coupon_code'] = $scope.coupon_code
    coupon_data['studio_id']  = $scope.serviceschosen.studio.id
    coupon_data['amount'] = $scope.total_amount
    $scope.su_couponing = true
    httpServices.applyCoupon(coupon_data).then(function(cdata)
    {
        $scope.su_couponing = false
        $scope.promo_amount = parseInt(cdata.apply_coupon.data)
        $scope.coupon_resp = "Coupon applied"
        $scope.amount_to_pay = ($scope.total_amount - $scope.promo_amount)
        if ($scope.serviceschosen.studio['has_service_tax'] > 0)
        {
            $scope.service_tax = Math.round(($scope.amount_to_pay * 14)/100)
        }
        if(!$scope.serviceschosen.studio['showpromo']){
            if($scope.serviceschosen.studio['zaloonoffer']!=0){
                $scope.zaloonoffer = Math.round(($scope.amount_to_pay * $scope.serviceschosen.studio['zaloonoffer'])/100)
            }
        }
        $scope.amount_to_pay = ($scope.amount_to_pay + $scope.service_tax)-$scope.zaloonoffer;
        //$scope.promo_amount = cdata.
    },function(cdata)
    {   
        $scope.su_couponing = false
        $scope.coupon_resp = cdata.data;
        $scope.promo_amount = 0
        $scope.total_amount = lodash.sum($scope.serviceschosen.services,'price');
        if ($scope.serviceschosen.studio['has_service_tax'] > 0)
        {
            $scope.service_tax = Math.round(($scope.amount_to_pay * 14)/100)
        }
        $scope.amount_to_pay = $scope.total_amount + $scope.service_tax 
        $scope.coupon_code="";
        console.log("Error applying coupon data")
    })
}
//Start Added
$scope.focus=function(){
    if($scope.promo_amount < 1)
    {
        $scope.coupon_resp="";
    }
}
//End Added

$scope.booking_class1 = "panel panel-default bookingdetails panel-closed"
$scope.booking_class2 = ""
$scope.booking_class3 = "panel-heading"
$scope.selectTime = function(hour,min)
{
    $scope.from_time = hour+":"+min
    if ($.inArray(min, $scope.avail[hour]) == -1)
    {
        return false;
    }
    if ($scope.from_time && $scope.date_selected)
    {
        $scope.booking_class1 = "panel panel-default"
        $scope.booking_class2 = "panel-open"
        $scope.booking_class3 = "panel-heading progress-done"
        $('#collapseThree').collapse('toggle');
        $('.panel-collapse.in').collapse('hide');
        $scope.date_accordion = "accordion-toggle collapsed"
        $scope.service_accordion = "accordion-toggle collapsed"
        $scope.booking_accordion = "accordion-toggle"
    }

}
$scope.payment_class1 = "panel panel-default panel-closed"
$scope.payment_class2 = ""
$scope.payment_class3 = "panel-heading"

$scope.makepayment = function(bookingForm)
{
    console.log($scope.serviceschosen);
    $scope.continueclick=true;
    if (!bookingForm.$invalid) {
        if ($scope.from_time && $scope.date_selected && $scope.mobileno)
        {
            //$scope.isdisable=true;
            var booking_data = {}
            booking_data['appnt_date'] = $scope.date_selected
            booking_data['appnt_time'] = $scope.from_time
            booking_data['actual_amount'] = $scope.total_amount 
            booking_data['purchase_amount'] = $scope.amount_to_pay
            booking_data['service_tax'] =  $scope.service_tax
            booking_data['discount'] = $scope.promo_amount
            booking_data['mobile_no'] = $scope.mobileno
            booking_data['services'] = $scope.selected_services
            booking_data['studio'] = $scope.serviceschosen.studio.id
            booking_data['studio_name'] = $scope.serviceschosen.studio.name
            booking_data['promo_code'] = $scope.coupon_code
            booking_data['serviceschosen'] = $scope.serviceschosen['services']
            var options = {
                //test key
                //"key": "rzp_test_bKVgZ668B7jtSR", 
                //live key
                "key": "rzp_live_RYXktqbBE8xIJb", 
                "amount": ($scope.amount_to_pay * 100),
                "name": $scope.user_details.user_acc['first_name'], //inser user name here
                "description": $scope.rp_service_txt,
                "image": "static/img/logo.png",
                "handler": function (response){
                    console.log(response)
                    //modal showing processing your payment dont click
                    $('#processingmodal').modal('show')
                    booking_data['razorpay_payment_id'] = response.razorpay_payment_id
                    httpServices.newBooking(booking_data).then(function(paydata)
                    {
                        console.log(paydata.new_booking.data)
                        resp = JSON.parse(paydata.new_booking.data)
                        booking_data['has_booked'] = 1
                        booking_data['booking_code'] = resp['code']
                        booking_data['razorpay_payment_id'] = null
                        putResultService.putBookingData(booking_data)
                        $location.path("/my_account");
                        //$('#processingmodal').modal('hide')
                    }, function()
                    {                        
                        $('#processingmodal').modal('hide');
                        $('#bookingfailedmodal').modal('show');
                        //$scope.isdisable=false;
                    });
            },
                "prefill": {
                "name": $scope.user_details.user_acc['first_name'], //user name
                "email": $scope.user_details.user_acc['email'], // user email
                "contact" : $scope.mobileno
                },
                "notes": {
                "address": $scope.user_details.user_acc['email']
                }
                }
                var rzp1 = new Razorpay(options);
                rzp1.open();
                //e.preventDefault();

                /*$scope.payment_frame = $sce.trustAsHtml($scope.paymentresponse);
                $scope.payment_class1 = "panel panel-default"
                $scope.payment_class2 = "panel-open"
                $scope.payment_class3 = "panel-heading progress-done"
                $('#collapseFour').collapse('toggle');
                $('.panel-collapse.in').collapse('hide');*/
                return true
            
            
        }
        else
        {
            return false;
        }
    }
}

//am/pm convertor

$scope.timeFilter =  function (value) {    
        if(typeof value != 'undefined' && value!="")
        {            
            var split = value.split(':');
            var min = split[1] =="0"? "00":split[1];            
            if (split[0] - 12 > 0) {

                returnval = split[0] - 12 + ":" + min + " PM";
            }
            else if((split[0] - 12 < 0)) {
                if(min=="00"){
                    returnval = split[0] + ":" + min + " AM";
                }
                else{
                    returnval = split[0] + ":" + split[1] + " AM";
                }
            }                
            else
            {
                returnval = split[0] + ":" + min + " PM";
            }
            //console.log(value+" - "+min+" - "+returnval);
            return returnval;
        }
        else
        {
            return ""
        }
    }

    //function check slot
    $scope.checkslot=function(col,slot){  
        var flag=false;      
        if(slot=="morning"){
            var array=lodash.range(1,12);
            angular.forEach(array, function(value, key){
                if(!flag){                
                    if(typeof col[value] != "undefined"){
                        flag=true;
                    } 
                }
            });
        }
        else if(slot=="noon"){
            var array=lodash.range(12,16);
            angular.forEach(array, function(value, key){
                if(!flag){                
                    if(typeof col[value] != "undefined"){
                        flag=true;
                    } 
                }
            });
        }
        else if(slot=="evening"){
            var array=lodash.range(16,24);
            angular.forEach(array, function(value, key){
                if(!flag){                
                    if(typeof col[value] != "undefined"){
                        flag=true;
                    } 
                }
            });
        }
        console.log(slot+" - "+flag);
        return flag;        
    }
});


noqapp.controller('modalController', ['$scope','$modalInstance', function($scope, $modalInstance,book) {
console.log(book)
    $scope.cancel = function () {
    $modalInstance.dismiss('cancel')
  };
    
}]);
noqapp.controller('accountscontroller',function($scope,$cookies,lodash,httpServices,putResultService,sessionService,$window,$modal){

    $('.profile-overlay').show();
    $scope.new_booking = putResultService.getBookingData()
    var modalInstance = null;
    templates ='<div style=""   class="modal-header modal-register-header">'+
    '<button type="button" class="close"  ng-click="cancel()">&times;</button>'+
    '<h4 class="modal-title">Cheers! Your booking is successful.</h4>'+
    '</div><!-- /modal-header --><div class="modal-body register">'+    
    '<div class="col-md-12"><h4 style="margin-top: 0;">{{new_booking.studio_name}}</h4></div><br/>'+
    '<div class="col-md-3">Date & Time:</div>'+
    '<div class="col-md-4">{{new_booking.appnt_date| date: yyyy-mm-dd}} <span ng-bind="timeFilter(new_booking.appnt_time)"></span></div><br/>'+
    '<div class="col-md-3">Booking code:</div>'+
    '<div class="col-md-4">{{new_booking.booking_code}}</div><br/>'+
    '<div class="col-md-3">SMS sent to:</div>'+
    '<div class="col-md-4">{{new_booking.mobile_no}}</div><br/>'+
    '<div class="col-md-3">Total amount:</div>'+
    '<div class="col-md-4"><i class="fa fa-inr"></i> {{new_booking.purchase_amount}}</div><br/>'+
    '<div class="col-md-3">Services booked:</div>'+
    '<div class="col-md-9"><span ng-repeat="ser in new_booking.serviceschosen">{{$index + 1}} - {{ser.servicename}}<br/></span><br/></div><br/>'+
    '<div style="clear:both"> </div>'+
    '<div class="col-md-7 col-sm-6 col-xs-12 resetpanel" style="left: 0px;bottom:0px;">'+
    '<button ng-click="cancel()" class="rebookbtn btn apply-btn col-md-4 col-sm-6 col-xs-12">'+
    '<span>Ok</span></button></div><div style="clear:both"> </div>'
    if($scope.new_booking)
    {
        if(($scope.new_booking['has_booked'] == 1) && ($scope.new_booking['razorpay_payment_id'] == null))
        {
            //$('#bookingconfirm').modal('show')
            modalInstance = $modal.open({
                template: templates,
                controller: 'modalController',
                size:'md',
                backdrop: 'static',
                keyboard: false,
                scope:$scope,                
                resolve:{book:function()
                    {
                        return $scope.new_booking
                    }}
                })
            putResultService.clearData()
        }
    }

$scope.$on('$routeChangeStart', function(next, current) 
   { 
       if($scope.new_booking)
       {
           modalInstance.dismiss('cancel');
       }
   });

$scope.logging_out = false
$scope.logOut = function()
    {   
        $scope.logging_out = true
        httpServices.logOut().then(function(logout_data)
        {
            $cookies.remove('token',{path:'/'});
            $cookies.remove('expiretime',{path:'/'});
            $cookies.remove('refreshtoken',{path:'/'})
            $cookies.remove('client_id',{path:'/'})
            $cookies.remove('client_secret',{path:'/'})
            window.location.reload()
            $location.path('/')
            //$scope.is_logged = sessionService.isLogged();
            
            
        },
        function()
        {
            console.log("Logout Error")
        })
    }


 $scope.active_next = null
 $scope.expired_next = null
 $scope.active_loading_more = false
 $scope.inactive_loading_more = false
    $scope.loadMore = function(which)
    {
        if ($scope.active_next != null || $scope.expired_next != null)
        {
            if(which == 'active')
            {
                $scope.active_loading_more = true
                httpServices.getMoreBooking($scope.active_next).then(function(data)
                {
                    $scope.active_loading_more = false
                    $scope.active_bookings = $scope.active_bookings.concat(data.more_booking.data.results)
                    $scope.active_next = data.more_booking.data.next
                    console.log(data.more_booking.data)
                    console.log($scope.active_bookings.concat(data.more_booking.data.results))
                    if($scope.active_next != null)
                    {
                        $scope.loadMore('active')   
                    }
                });
            }
            else
            {
                    $scope.inactive_loading_more = true
                    httpServices.getMoreBooking($scope.expired_next).then(function(data)
                    {
                        $scope.inactive_loading_more = false
                        $scope.expired_bookings = $scope.expired_bookings.concat(data.more_booking.data.results)
                        $scope.expired_next = data.more_booking.data.next
                        if($scope.expired_next != null)
                        {
                            $scope.loadMore('inactive')   
                        }
                    });
                
            }
        }
    }


    $scope.getBookings = function()
    {
        
        httpServices.getDetails().then(function(data)
        {            
            $scope.user_details = data.user_details.data[0]
            $scope.location = $scope.user_details.area
            $scope.phoneno = $scope.user_details.mobile
            $scope.active_bookings = data.active_booking.data.results
            $scope.expired_bookings = data.expired_booking.data.results
            $scope.expired_next = data.expired_booking.data.next
            $scope.active_next = data.active_booking.data.next
            $scope.active_count = data.active_booking.data.count
            $scope.inactive_count = data.expired_booking.data.count
            $('.profile-overlay').hide();
            if($scope.active_next !=  null)
            {
                 $scope.loadMore('active')
            }
            if($scope.expired_next != null)
            {
                $scope.loadMore('inactive')   
            }
            httpServices.splitBookings($scope.active_bookings,$scope.expired_bookings).then(function(data)
            {
                $scope.expired_bookings = data.inactive_booking
                $scope.active_bookings = data.active_booking
                
                
            },  
            function()
            {
                console.log("Error splitting bookings")
            });
        },
        function()
        {
            console.log("Error getting user Details and booking")   
        })
    }

    $scope.getBookings();

    $(document).on("click", ".bookbtn", function () {
     var myBookId = $(this).data('id');
     $scope.cancel_booking_id = myBookId
     $scope.$apply()
    }); 
    $scope.is_cancelling = 0;
    $scope.has_cancelled = null
   
    $scope.booking_cancel = function(id)
    {        
        $scope.is_cancelling = 1;
        httpServices.cancelBooking(id).then(function(data)
        {
            $scope.has_cancelled = 1
            $scope.is_cancelling = null
            //$scope.getBookings();
            var index=lodash.findIndex($scope.active_bookings, 'id', id);
            var cancelstudio=$scope.active_bookings[index];
            $scope.active_bookings.splice(index, 1);
            cancelstudio.status_code="B003";
            $scope.expired_bookings.push(cancelstudio)
            console.log("Booking successfully cancelled")

        },
        function()
        {
            $scope.has_cancelled = 0
            $scope.is_cancelling = null
        })
    }
    $scope.clearcancel = function()
    {
        $scope.is_cancelling = 0;
        $scope.has_cancelled = null
        $('#cancelmodal').modal('hide')
    }
    $scope.change_usr_details = function()
    {
        $scope.usr_data = null
        httpServices.updateUserProfile($scope.usr_data).then(function(data)
        {
            console.log("Details updated")
        },
        function()
        {
            console.log("Could not update try again.")  
        })
    }

    $scope.timeFilter =  function (value) {
        if(typeof value != 'undefined')
        {
            var split = value.split(':');
            if (split[0] - 12 > 0) {
                returnval = split[0] - 12 + ":" + split[1] + " PM";
            }
            else if((split[0] - 12 < 0)) {
                returnval = split[0] + ":" + split[1] + " AM";
            }                
            else
            {
                returnval = split[0]  + ":" + split[1] + " PM";
            }
            return returnval;
        }
        else
        {
            return ""
        }
    }

    $scope.updateprofile=function(){
        
        var obj={area:$scope.user_details.area,mobile:$scope.user_details.mobile};
        console.log(obj);
    }

    //For mobile
    $scope.phoneno = "";
    $scope.phoneshow = true;
    $scope.editphone = function () {
        $scope.phoneshow = !$scope.phoneshow;
        $scope.txtphone = $scope.phoneno;
        $scope.locationshow=true;
    }
    $scope.pheditableok = function (formphone) {
        $scope.phonesubmit = true;
        if (!formphone.$invalid) {
            data = {}
            data['mobile'] = $scope.txtphone
            httpServices.updateUserProfile(data).then(function(pdata)
            {
                $scope.phoneshow = true;
                $scope.phoneno = $scope.txtphone;
            },function()
            {
                console.log("Cannot update phone no")
            })

        }
    }
    $scope.pheditablecancel = function () {
        $scope.phoneshow = true;
        $scope.phonesubmit=false;
    }
    //For location
    $scope.location = "";
    $scope.locationshow = true;
    $scope.editlocation = function () {
        $scope.locationshow = !$scope.locationshow;
        $scope.txtlocation = $scope.location;
        $scope.phoneshow=true;
    }
    $scope.loceditableok = function (formlocation) {
        $scope.locationsubmit = true;
        if (!formlocation.$invalid) {
            data = {}
            data['area'] = $scope.txtlocation
            httpServices.updateUserProfile(data).then(function(adata)
            {
                $scope.location = $scope.txtlocation;
                $scope.locationshow = true;
            },function()
            {
                console.log("Cannot update area")
            })

        }
    }
    $scope.loceditablecancel = function () {
        $scope.locationshow = true;
        $scope.locationsubmit=false;
    }
    //AutoComplete
    $scope.searchdata_ = {};    
    $scope.searchdata_['arealist'] = [];    
    var acService = new google.maps.places.AutocompleteService();
    $scope.areacomplete = function () {        
        if ($scope.txtlocation != "" && typeof $scope.txtlocation != 'undefined') {
            acService.getPlacePredictions({
                input: $scope.txtlocation,
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
                    console.log(_places); 
                    $scope.searchdata_['arealist'] = _places;     
                }
            });
        }
    }
    $scope.onlocationselect = function ($item, $model, $label) {
        $scope.txtlocation=$label;
    };

//rating & review
$(document).on("click", ".reviewbtn", function () {
     var myBookId = $(this).data('id');
     $scope.booking_id = myBookId
     $scope.is_adding = 0
     $scope.submitting = 0
     $scope.reviewstudio=$(this).data('studio');
     $scope.$apply()
    });  


$scope.review_data = {}
$scope.is_adding = 0
$scope.clearreviewdata = function()
{
    $scope.review_data['comment'] = ""
    $scope.review_data['rate'] = 0
    $scope.formsubmit=false;

}
$scope.titleMsg = 'Successfully added review'; 
$scope.review_message = 'That was cool! We’ve added your review. Many thanks for sharing your experience with us.';
$scope.is_adding = 0
$scope.submitting = 0
$scope.formsubmit=false;
$scope.add_review = function(form)
{
   $scope.formsubmit=true;
   $scope.review_data['booking_id'] = $scope.booking_id
   if(form.$valid)
    {
       $scope.submitting = 1
       httpServices.addReview($scope.review_data).then(function(rdata)
        {
            $scope.is_adding = 1
            $scope.submitting = 0
            //$('#reviewmodal').modal('hide')
            console.log(rdata)
            lodash.find($scope.expired_bookings,function(booking) 
                { if(booking['id'] == $scope.review_data['booking_id'])
                    {
                        booking['is_reviewed'] = 1
                    }
            });
            $scope.review_data = {}
            $('#notificationmodal').modal('show')
            $scope.titleMsg = 'Review added'; 
            $scope.review_message = 'Thanks your review has been added.'; 
        },function()
        {
            //$('#reviewmodal').modal('hide')
            $scope.is_adding = 1
            $scope.submitting = 0
            $('#notificationmodal').modal('show')
            $scope.titleMsg = 'Review not added'; 
            $scope.review_message = 'Could not add review try again'; 
            console.log("Could not add review.")
            
        })
    }
}


function toSeconds(time_str) {
    // Extract hours, minutes and seconds
    var parts = time_str.split(':');
    // compute  and return total seconds
    return parts[0] * 3600 + // an hour has 3600 seconds
    parts[1] * 60 + // a minute has 60 seconds
    +
    parts[2]; // seconds
}

//function which gives the duration of the booking
$scope.findDuration = function(start_time,end_time)
{
    var difference = Math.abs(toSeconds(start_time) - toSeconds(end_time));
    time = Math.abs(difference/60)
    //console.log(time)
    return time
}
//function which tells whether we can show cancel button for the booking
var today  = new Date()
$scope.has_cancel = function(start_time,appnt_date)
{
    var appnt_date =  new Date(appnt_date)
    var start_time = parseInt(start_time.substring(0,2))
    if(today.getDate() == appnt_date.getDate() && today.getMonth() == appnt_date.getMonth())
    {
       if(start_time < 13 && today.getHours() < 5)
       {
            return true
       } 
       else if(start_time >= 13 && today.getHours() < 12)
       {
            return true
       }
       else
       {
         return false
       }
    }
    else
    {
        return true
    }
}    

});
    