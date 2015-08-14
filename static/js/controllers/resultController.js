noqapp.filter('startFrom', function () {
    return function (input, start) {
        if (input) {
            start = +start;
            return input.slice(start);
        }
        return [];
    };
});





noqapp.controller('resultCtrl', function ($scope, $compile,$location, $filter,$cookies,$window,lodash,httpServices,sessionService,putResultService) {
    
    $scope.studio = [];
    $scope.filteredstudio = [];
    $scope.servicelist = [];
    $scope.selectedstudio = {};
    $scope.searchdata={};
    $scope.serviceprice;    
    $scope.morefilter = false;
    $scope.stariconset={1:'star1',2:'star2',3:'star3',4:'star4',5:'star5'};
    $scope.studiotype = [{ name: "Spa", active: false, icon: "icon icon-medical-19" }, { name: "Studio", active: false, icon: "icon icon-shopping-23" }, { name: "Saloon", active: false, icon: "fa fa-scissors" }];
    $scope.studiokind = [{ name: "Men", active: false, icon: "fa-mars" }, { name: "Women", active: false, icon: "fa-venus" }, { name: "Unisex", active: false, icon: "fa-venus-mars" }];
    $scope.studiostar = [{ star: 1, active: false }, { star: 2, active: false }, { star: 3, active: false }, { star: 4, active: false }, { star: 5, active: false }];
    $scope.studiosort = [{ property: "distance", value: "distanceasc", direction: false,name:"Distance" }, { property: "price", value: "priceasc", direction: false ,name:"Price"}, { property: "price", value: "pricedsc", direction: true,name:"Price dsc" }, { property: "rating", value: "ratingdsc", direction: true,name:"Rating" }];
    $scope.orderProp = 'price';
    $scope.direction = false;    
    $scope.studioservice = [];
    $scope.studiotypefilter = [];
    $scope.studiokindfilter = [];
    $scope.studioratingfilter = [];
    $scope.studioservicefilter = [];
    $scope.tempstudiotypefilter=[];
    $scope.tempstudiokindfilter = [];
    $scope.tempstudioratingfilter = [];
    $scope.tempstudioservicefilter = [];
    $scope.is_logged = sessionService.isLogged();
    $scope.selected_service = [];
    $scope.to_booking_flag = 0;
    var acService = new google.maps.places.AutocompleteService();
    var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer();
    var infoWindow = new google.maps.InfoWindow();
    var mapOptions = {
        zoom: 4,
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
    $scope.markers = [];
    var latlongcollection = [];
    $scope.shopdistance;
    $scope.reviewPage = 1;
    $scope.reviewtotalpage;
    $scope.totalItems;
    $scope.itemLimit = 2;
    $scope.currentPage = 1;
    var top;
    var data;    
    
     $scope.getservice = function (studio) {
        angular.forEach(studio.studio_detail_for_activity, function (value, key) {
            if ($scope.studioservice.indexOf(value.service.service_name) == -1) {
                $scope.studioservice.push(value.service.service_name);
            }
        });
    };

    $scope.timeFilter =  function (value) {
        if(typeof value != 'undefined')
        {            
            var split = value.split(':');
            if (split[0] - 12 > 0) {
                returnval = split[0] - 12 + ":" + split[1] + " PM";
            }
            else {
                returnval = split[0] + ":" + split[1] + " AM";
            }                
            return returnval;
        }
        else
        {
            return ""
        }
    }

    $scope.getprice_rating = function (index, studio) {
        var price, rating = 0;
        for (var i = 0; i < studio.studio_detail_for_activity.length; i++) {
            if (studio.studio_detail_for_activity[i].service.service_name == $scope.searchdata.service) {
                price = studio.studio_detail_for_activity[i].price;
                break;
            }
        }
        for (var j = 0; j < studio.studio_review.length; j++) {
            rating = rating + studio.studio_review[j].rating;
        }        
        if(rating!=0){
            rating = Math.round(rating / studio.studio_review.length);            
        }
        console.log(rating);
        $scope.studio[index].rating = rating;
        $scope.filteredstudio[index].rating = rating;
        $scope.studio[index].price = price;
        $scope.filteredstudio[index].price = price;        
        $scope.filteredstudio[index].staricon=$scope.stariconset[rating];
        $scope.studio[index].staricon=$scope.stariconset[rating];
    }

        //Google Maps    
    var imagUrls = {
        //oneOn: 'http://maps.google.com/mapfiles/kml/pal3/icon47.png',
        //oneOff: 'http://maps.google.com/mapfiles/kml/pal3/icon39.png'
        oneOff: 'static/img/blue24.png',
        oneOn: 'static/img/green24.png'
    };
    var images = {
        oneOn: new google.maps.MarkerImage(imagUrls.oneOn),
        oneOff: new google.maps.MarkerImage(imagUrls.oneOff)
    };
    var bounds = new google.maps.LatLngBounds();
    var createmarker = function (studio) {
        var marker = new google.maps.Marker({
            map: $scope.map,
            position: new google.maps.LatLng(studio.latitude, studio.longitude),
            title: studio.name,
            icon: images.oneOff
        });        
        var compiled = $compile('<div class="map-tooltip-panel"><div class="details"><img class="image loaded" style="height: 100px;" alt="" src='+studio.thumbnail+'><div class="info"><div class="heading"><h4>'+ studio.name + '</h4></div><div class="landmark_details">'+ studio.address_1 +'</div><div class="sub-line-2"><span>'+ studio.distance +' KM</span><span class="price"><span class="icon-rupee rupee"></span><span class="info-rate">₹'+ studio.price +'</span></span></div></div></div></div>')($scope);        
        marker.content = compiled[0];
        google.maps.event.addListener(marker, 'click', function () {
            if (infoWindow) infoWindow.close();
            infoWindow.setContent(marker.content);
            infoWindow.open($scope.map, marker);
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
        google.maps.event.trigger(selectedmarker, 'mouseover');
    }
    $scope.hoverOut = function (studioname) {
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
        google.maps.event.trigger(selectedmarker, 'mouseout');
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
    function drawdirection(lat, lon) {        
        directionsDisplay.setMap($scope.map);
        var request = {
            origin: new google.maps.LatLng(lat, lon),
            destination: $scope.directionlocation,
            travelMode: google.maps.DirectionsTravelMode.DRIVING
        };
        directionsService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                $scope.distance = response.routes[0].legs[0].distance.text;
                $scope.$apply();                
                directionsDisplay.setDirections(response);
            }
        });
    }

$scope.bindstudio=function(data){    
    $scope.studio=[];
    $scope.filteredstudio=[];
    angular.forEach(data, function (value, key) {
            $scope.studio.push(value);
            $scope.filteredstudio.push(value);            
            $scope.getservice(value);
            $scope.getprice_rating(key, value);
            getdistance(key, value.latitude, value.longitude);
        });
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
        $scope.totalItems = $scope.filteredstudio.length;
    }


    function getdistance(key, lat, long) {
        var request = { origin: new google.maps.LatLng(lat, long), destination: $scope.searchdata.location, travelMode: google.maps.DirectionsTravelMode.DRIVING };
        directionsService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                console.log(response.routes[0].legs[0].distance.text);
                $scope.studio[key].distance = parseFloat(response.routes[0].legs[0].distance.text);
                $scope.$apply();
            }
        });
    }

    //Filter
    $scope.clkmore = function () {
        //$('#searchdevice').hide();
        $scope.searchicon=false;
        if($('#studiodetails').css('display') != 'none'){
            $scope.closeslider();
        } 
        if(!$scope.morefilter){            
            $scope.tempstudiotypefilter= [];
            $scope.tempstudiokindfilter = [];
            $scope.tempstudioratingfilter = [];
            $scope.tempstudioservicefilter = [];
            $scope.tempstudiotypefilter = angular.copy($scope.studiotypefilter);
            $scope.tempstudiokindfilter = angular.copy($scope.studiokindfilter);
            $scope.tempstudioratingfilter = angular.copy($scope.studioratingfilter);
            $scope.tempstudioservicefilter = angular.copy($scope.studioservicefilter);
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
        $scope.studioservicefilter = angular.copy($scope.tempstudioservicefilter);
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
        $('input:checkbox').removeAttr('checked');
        $('input[type=checkbox]').each(function () {  
            //Start Added          
            if ($scope.tempstudioservicefilter.indexOf($(this).next().text()) != -1) {                
                $(this).prop('checked', true);
            }
            //End Added
        });
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

    $scope.studioserviceclick = function (service) {
        if ($scope.studioservicefilter.indexOf(service) == -1) {
            $scope.studioservicefilter.push(service);
        }
        else {
            $scope.studioservicefilter.splice($scope.studioservicefilter.indexOf(service), 1);
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
        $scope.studioservicefilter = [];
        $('input:checkbox').removeAttr('checked');
        $scope.applyfilter();
    }

    $scope.customfilter = function (studio) {
        if ($scope.studiotypefilter.length != 0 || $scope.studiokindfilter.length != 0 || $scope.studioratingfilter.length != 0 || $scope.studioservicefilter.length != 0) {
            var returnvalue;
            returnvalue = $scope.checkstudiotype(studio);
            if (returnvalue) {
                returnvalue = $scope.checkstudiokind(studio);
            }
            if (returnvalue) {
                returnvalue = $scope.checkstudiorating(studio);
            }
            if (returnvalue) {
                returnvalue = $scope.checkstudioservice(studio);
            }
            return returnvalue;
        }
        else {
            return true;
        }
    }

    $scope.checkstudiotype = function (studio) {
        if ($scope.studiotypefilter.length != 0) {
            if ($scope.studiotypefilter.indexOf(studio.studio_type.type_desc) == -1) {
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
            if ($scope.studiokindfilter.indexOf(studio.studio_kind.kind_desc) == -1) {
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

    $scope.checkstudioservice = function (studio) {
        var returntype = true;
        angular.forEach($scope.studioservicefilter, function (service, index) {
            if (returntype) {
                if (lodash.findIndex(studio.studio_detail_for_activity, { service: { service_name: service } }) == -1) {
                    returntype = false;                    
                }
            }
        });
        return returntype;
    }


    

    $scope.sortchange=function(selectitem){        
        $scope.orderProp = selectitem.property;
        $scope.direction = selectitem.direction;
        removemarker();
        clearlatlongbound();
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
    }

    $scope.studiodetails = function (id) {
        var studio = lodash.where($scope.studio, { 'id': id });
        if (studio.length > 0) {
            $('.detail-tab').removeClass('active');
            $('.tab-street').addClass('active');
            $('#searchdevice').hide();
            $scope.searchicon=false;
            $scope.morefilter=false;
            $scope.selectedstudio = studio[0];
            $scope.selectedstudio['type_icon_class']  = lodash.where($scope.studiotype,{'name':$scope.selectedstudio.studio_type.type_desc})[0].icon;
            $scope.selectedstudio['kind_icon_class']  = lodash.where($scope.studiokind,{'name':$scope.selectedstudio.studio_kind.kind_desc})[0].icon;
            $scope.sortservicebyfilter();
            $('.header-tabs').removeClass('stick');
            $('#studiodetails').toggle('slide', { direction: 'right' }, 200);
            $scope.reviewPage = 1;
            $scope.directionlocation=$scope.searchdata.location;
            var page = Math.floor($scope.selectedstudio.studio_review.length / 10);            
            page = page + ($scope.selectedstudio.studio_review.length % 10 > 0 ? 1 : 0);                  
            $scope.reviewtotalpage = page;            
            $scope.shopdistance = $scope.selectedstudio.distance;            
            setTimeout(function(){
                removemarker();
                drawdirection($scope.selectedstudio.latitude, $scope.selectedstudio.longitude);
            },300);
            setTimeout(function () {                
                top = { 'street-info': $('.street-info').position().top, 'service-list': $('.service-list').position().top, 'review-detail': $('.review-detail').position().top, 'direction': $('.direction').position().top };                
                console.log(top);
            }, 1000);
        }
    }
    $scope.closeslider = function () {        
        $('#studiodetails').toggle('slide', { direction: 'right' }, 200);
        $scope.selected_service = [];
        setTimeout(function(){
            directionsDisplay.setMap(null);
            clearlatlongbound();
            $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
            autozoom();
        },300);                
    }
    $scope.easyscroll = function (clsname) {
        $('.list-detail-box').animate({
            scrollTop: top[clsname] - 157
        }, 200);
    }

    $scope.morereview = function () {
        $scope.reviewPage = $scope.reviewPage + 1;
    }

    $scope.firstreview = function()
    {
        $scope.reviewPage = 1;   
    }

    $scope.changedirection=function(){
        directionsDisplay.setMap(null);
        drawdirection($scope.selectedstudio.latitude, $scope.selectedstudio.longitude);
        var request = { origin: new google.maps.LatLng($scope.selectedstudio.latitude, $scope.selectedstudio.longitude), destination: $scope.directionlocation, travelMode: google.maps.DirectionsTravelMode.DRIVING };
        directionsService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {                
                $scope.shopdistance = parseFloat(response.routes[0].legs[0].distance.text);
                $scope.$apply();
            }
        });
        //$scope.shopdistance
    }

    $scope.sortservicebyfilter = function () {
        $scope.servicelist = [];
        var res = lodash.where($scope.selectedstudio.studio_detail_for_activity, { service: { service_name: $scope.searchdata.service } });
        $scope.servicelist.push({id:res[0].service.id, servicename: res[0].service.service_name, price: res[0].price, flag: true, duration:res[0].mins_takes  });
        $scope.selected_service.push($scope.servicelist[0]);
        $scope.serviceprice = res[0].price;
        angular.forEach($scope.studioservicefilter, function (service, key) {
            res = lodash.where($scope.selectedstudio.studio_detail_for_activity, { service: { service_name: service } });
            if (lodash.findIndex($scope.servicelist, { 'servicename': res[0].service.service_name }) == -1) {
                $scope.servicelist.push({id:res[0].service.id,servicename: res[0].service.service_name, price: res[0].price, flag: false , duration:res[0].mins_takes });
            }
        });
        angular.forEach($scope.selectedstudio.studio_detail_for_activity, function (service, key) {
            if (lodash.findIndex($scope.servicelist, { 'servicename': service.service.service_name }) == -1) {
                $scope.servicelist.push({id:service.service.id, servicename: service.service.service_name, price: service.price, flag: false, duration:service.mins_takes });
            }
        });
    }
    $scope.addservice = function (service) {       
        var index = lodash.findIndex($scope.servicelist, service);
        var flag = $scope.servicelist[index].flag;
        $scope.servicelist[index].flag = !$scope.servicelist[index].flag;
        if (flag) {            
            var inx=lodash.findIndex($scope.selected_service, { 'servicename': service.servicename });
            $scope.selected_service.splice(inx, 1);
            $scope.serviceprice = $scope.serviceprice - service.price;
        }
        else 
        {   
            $scope.selected_service.push(service);            
            $scope.serviceprice = $scope.serviceprice + service.price;
        }        
    }

    //Pagination
    $scope.pagechange = function () {    
        removemarker();
        clearlatlongbound();
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
    }
    //AutoComplete
    $scope.searchdata_ = {};    
    $scope.searchdata_['arealist'] = [];    
    var acService = new google.maps.places.AutocompleteService();
    $scope.areacomplete = function (val) {     
        if (val != "" && typeof val != 'undefined') {
            acService.getPlacePredictions({
                input: val,
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
                    $scope.searchdata_['arealist'] = _places;     
                }
            });
        }
    }
    //Get All Services    
    $scope.searchdata_['servicelist']='';
    httpServices.getService().then(function(data)
        {           
            $scope.searchdata_['servicelist'] = data['service_details'].data;

        },function()
        {
            console.log("Try again to get service")
        });    

    //Search Studio Details Event    
    $scope.onserviceselect = function ($item, $model, $label) {     
        $scope.searchdata.service=$item.service_name;    
    };
    $scope.onlocationselect = function ($item, $model, $label) {
        $scope.searchdata.location=$label;
    };
    $scope.ondirectionselect = function ($item, $model, $label) {
        $scope.directionlocation=$label;
    };
    $scope.searchservicestudio=function(){
        $('#searchdevice').hide();
        $scope.searchicon=false;
        var obj={'service':$scope.searchdata.service,'location':$scope.searchdata.location};
        httpServices.getstudioDetails(obj).then(function(data)
        {
            $scope.bindstudio(data.studio_details.data);
            $cookies.putObject('searchdata',obj,{path:'/'});         
            $cookies.putObject('data',data.studio_details.data,{path:'/'});
        },function()
        {
            console.log("Try again to get service")
        });
    }

    $scope.searchdata=$cookies.getObject('searchdata');    
    if(typeof $scope.searchdata == "undefined"){
        $location.path("/");
    }
    else
    {
        if(putResultService.getresult().length ==0){
            httpServices.getstudioDetails($scope.searchdata).then(function(res)
                {       
                    //console.log(res.studio_details.data);
                    data=res.studio_details.data;
                    putResultService.setresult(res.studio_details.data);  
                    $scope.bindstudio(data);                              
                },function()
                {
                    console.log("Try again to get service");
                    $location.path("/");
                });
        }
        else{
           data=putResultService.getresult(); 
           $scope.bindstudio(data);
        }
    }

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
        var booking_data = {'studio':$scope.selectedstudio,'services':$scope.selected_service,  
        'user_details':$scope.user_details}
        putResultService.setSelectedservice(booking_data)
        $location.path('/booking')
    }
}

//fb keys

httpServices.getFBKey().then(function(data)
{
    $scope.fb_key = data['fb_key'].data
});

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
                $scope.user_details = dataz['user_details'].data[0]
                $scope.user_name = $scope.user_details.user_acc['first_name']
                $('#signupmodel').modal('hide');
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
        $scope.user_details = dataz['user_details'].data[0]
        console.log($scope.user_details)
        $scope.user_name = $scope.user_details.user_acc['first_name']
    }, function()
    {
        console.log("Error getting user data")  
    })  
}


$scope.logOut = function()
    {   
        httpServices.logOut().then(function(logout_data)
        {
            //alert("Here")
            //$cookies.remove('token')
            //$scope.is_logged = sessionService.isLogged()
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
    $scope.rp_service_txt = $scope.serviceschosen['services'][0].servicename +" & "+String(($scope.serviceschosen['services'].length) - 1) +' more services'
    
}
else
{
    $scope.rp_service_txt = $scope.serviceschosen['services'][0].servicename   
}
console.log($scope.rp_service_txt)
$scope.user_details = $scope.serviceschosen['user_details']
console.log($scope.user_details)
$scope.mobileno = $scope.user_details.mobile
$scope.total_duration=lodash.sum($scope.serviceschosen.services,'duration');
$scope.total_amount = lodash.sum($scope.serviceschosen.services,'price');
$scope.selected_services = lodash.pluck($scope.serviceschosen.services, 'id');
$scope.promo_amount = 0
$scope.amount_to_pay = $scope.total_amount - $scope.promo_amount

console.log($scope.serviceschosen.studio);
angular.forEach($scope.serviceschosen.studio.studio_closed_details, function(value, key) {    
    $scope.closed_days.push(value.closed_on.id-1);    
});
if ($scope.start_date.getHours() > 11)
{
    $scope.start_date.setDate($scope.start_date.getDate() + 1);
}
$scope.end_date = angular.copy($scope.start_date)
$scope.end_date.setDate($scope.start_date.getDate() + 30);


 $scope.avail = []



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
    console.log(is_today.getDate())
    console.log(is_today.getMonth())
    console.log(today.getDate())
    console.log(today.getMonth())
    console.log(today.getHours())
    if(is_today.getDate() == today.getDate() && is_today.getMonth() == today.getMonth() && (parseInt(today.getHours()) > 4))
    {
        $scope.day_crossed = 0;
    }
    slot_data['services'] = $scope.selected_services
    slot_data['date'] = $scope.date_selected
    slot_data['duration'] = $scope.total_duration
    slot_data['studio_id'] = $scope.serviceschosen.studio.id
    httpServices.getSlots(slot_data).then(function(sdata)
    {
        $('html, body').animate({scrollTop: $('#collapseTwo').offset().top }, 'slow');
        $scope.avail = sdata.available_slots.data;        
    },function()
    {
        console.log("Not slots available.Try another date")
    })
    $scope.$apply()
});


$scope.applyPromo = function()
{
    var coupon_data = {};
    coupon_data['coupon_code'] = $scope.coupon_code
    coupon_data['studio_id']  = $scope.serviceschosen.studio.id
    coupon_data['amount'] = $scope.total_amount
    httpServices.applyCoupon(coupon_data).then(function(cdata)
    {
        $scope.promo_amount = parseInt(cdata.apply_coupon.data)
        $scope.coupon_resp = "Coupon applied"
        $scope.amount_to_pay = $scope.total_amount - $scope.promo_amount
        //$scope.promo_amount = cdata.
    },function(cdata)
    {   
        $scope.coupon_resp = cdata.data;
        $scope.coupon_code="";
        console.log("Error applying coupon data")
    })
}
//Start Added
$scope.focus=function(){
    $scope.coupon_resp="";
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
            $scope.isdisable=true;
            var booking_data = {}
            booking_data['appnt_date'] = $scope.date_selected
            booking_data['appnt_time'] = $scope.from_time
            booking_data['actual_amount'] = $scope.total_amount
            booking_data['purchase_amount'] = $scope.amount_to_pay
            booking_data['mobile_no'] = $scope.mobileno
            booking_data['services'] = $scope.selected_services
            booking_data['studio'] = $scope.serviceschosen.studio.id
            booking_data['promo_code'] = $scope.coupon_code
            var options = {
                "key": "rzp_test_bKVgZ668B7jtSR",
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
                        console.log(booking_data)
                        booking_data['has_booked'] = 1
                        booking_data['razorpay_payment_id'] = null
                        putResultService.putBookingData(booking_data)
                        $('#processingmodal').modal('hide')
                        $location.path("/my_account");
                    }, function()
                    {
                        alert("Failed") //hide and show rzrpay again
                        $('#processingmodal').modal('hide')
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
        if(typeof value != 'undefined')
        {            
            var split = value.split(':');
            var min = split[1] =="0"? "00":split[1];
            if (split[0] - 12 > 0) {

                returnval = split[0] - 12 + ":" + min + " PM";
            }
            else {
                returnval = split[0] + ":" + min + " AM";
            }                
            return returnval;
        }
        else
        {
            return ""
        }
    }


});

noqapp.controller('accountscontroller',function($scope,httpServices,putResultService){

    $scope.active_booking_count = 10;

    $scope.new_booking = putResultService.getBookingData()
    console.log($scope.new_booking)
    if($scope.new_booking)
    {
        if(($scope.new_booking['has_booked'] == 1) && ($scope.new_booking['razorpay_payment_id'] == null))
        {
            $scope.$on('$routeChangeStart', function(scope, next, current)
            {
                if(next['templateUrl'] ='/booking/booking_page/')
                {
                    window.location.href = "http://localhost:8000";
                    //window.location.href = "http://www.zaloon.in";                
                }
                
            });
            $('#bookingconfirm').modal('show')
        }
    }
    $scope.getBookings = function()
    {
        httpServices.getDetails().then(function(data)
        {
            $scope.user_details = data.user_details.data[0]
            $scope.location = $scope.user_details.area
            $scope.phoneno = $scope.user_details.mobile
            $scope.booking_details = data.booking.data
            httpServices.splitBookings($scope.booking_details).then(function(data)
            {
                $scope.active_bookings = data.active_booking
                $scope.expired_bookings = data.inactive_booking
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

    $scope.booking_cancel = function(id)
    {
        $('#cancelmodal').modal('hide')
        httpServices.cancelBooking(id).then(function(data)
        {
            $('#notificationmodal').modal('show')
            $scope.titleMsg = 'Success'; 
            $scope.bodyMsg = 'Your booking successfully cancelled.'; 
            $scope.getBookings();
            console.log("Booking successfully cancelled")
        },
        function()
        {
            $('#notificationmodal').modal('show')
            $scope.titleMsg = 'Failed'; 
            $scope.bodyMsg = 'Could not cancel your booking.Contact support@zaloon.in'; 
            console.log("Logout Error") 
        })
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

    $scope.add_review = function()
    {
        $scope.review_data = null
        httpServices.addReview($scope.review_data).then(function(data)
        {
            console.log("Review added")
        },
        function()
        {
            console.log("Error occurred;Please,Try again.") 
        })
    }

    $scope.timeFilter =  function (value) {
        if(typeof value != 'undefined')
        {
            var split = value.split(':');
            if (split[0] - 12 > 0) {
                returnval = split[0] - 12 + ":" + split[1] + " PM";
            }
            else {
                returnval = split[0] + ":" + split[1] + " AM";
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
    }
    //For location
    $scope.location = "";
    $scope.locationshow = true;
    $scope.editlocation = function () {
        $scope.locationshow = !$scope.locationshow;
        $scope.txtlocation = $scope.location;
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
     $scope.$apply()
    });  

$scope.add_review = function()
{
    var review_data = {}
    review_data['comment'] = $scope.comment
    review_data['rating'] = $scope.rate
    review_data['booking_id'] = $scope.booking_id
    httpServices.addReview(review_data).then(function(rdata)
    {
        $('#reviewmodal').modal('hide')
        $('#notificationmodal').modal('show')
        $scope.titleMsg = 'Successfully added review'; 
        $scope.bodyMsg = 'Your rating and review successfully noted'; 
        console.log(rdata)
    },function()
    {
        $('#reviewmodal').modal('hide')
        $('#notificationmodal').modal('show')
        $scope.titleMsg = 'Review not added'; 
        $scope.bodyMsg = 'Could not add review try again'; 
        console.log("Could not add review.")
    })
}
});
    