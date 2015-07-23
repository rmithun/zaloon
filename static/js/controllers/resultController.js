noqapp.filter('startFrom', function () {
    return function (input, start) {
        if (input) {
            start = +start;
            return input.slice(start);
        }
        return [];
    };
});





noqapp.controller('resultCtrl', function ($scope, $compile, $filter,$cookies,lodash,httpServices,sessionService) {
    $scope.studio = [];
    $scope.filteredstudio = [];
    $scope.servicelist = [];
    $scope.selectedstudio = {};
    $scope.searchdata={};
    $scope.serviceprice;    
    $scope.morefilter = false;
    $scope.stariconset={1:'star1',2:'star2',3:'star3',4:'star4',5:'star5'}
    $scope.studiotype = [{ name: "Spa", active: false, icon: "icon icon-medical-19" }, { name: "Studio", active: false, icon: "icon icon-shopping-23" }, { name: "Saloon", active: false, icon: "fa fa-scissors" }];
    $scope.studiokind = [{ name: "Men", active: false, icon: "fa-mars" }, { name: "Women", active: false, icon: "fa-venus" }, { name: "Unisex", active: false, icon: "fa-venus-mars" }];
    $scope.studiostar = [{ star: 1, active: false }, { star: 2, active: false }, { star: 3, active: false }, { star: 4, active: false }, { star: 5, active: false }];
    $scope.studiosort = [{ property: "distance", value: "distanceasc", direction: false }, { property: "price", value: "priceasc", direction: false }, { property: "price", value: "pricedsc", direction: true }, { property: "rating", value: "ratingdsc", direction: true }];
    $scope.sortservice = $scope.studiosort[1].value;
    $scope.studioservice = [];
    $scope.studiotypefilter = [];
    $scope.studiokindfilter = [];
    $scope.studioratingfilter = [];
    $scope.studioservicefilter = [];
    $scope.is_logged = sessionService.isLogged();

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
    $scope.sampledestination = "Sholinganallur, Chennai, Tamil Nadu, India";
    $scope.shopdistance;
    $scope.reviewPage = 1;
    $scope.reviewtotalpage;
    $scope.totalItems;
    $scope.itemLimit = 2;
    $scope.currentPage = 1;
    var top;
    var data;
    $scope.searchdata=$cookies.getObject('searchdata');    
    data = $cookies.getObject('data');
    console.log(data);

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
        rating = Math.round(rating / studio.studio_review.length);
        $scope.studio[index].rating = rating;
        $scope.filteredstudio[index].rating = rating;
        $scope.studio[index].price = price;
        $scope.filteredstudio[index].price = price;        
        $scope.filteredstudio[index].staricon=$scope.stariconset[rating];
        $scope.studio[index].staricon=$scope.stariconset[rating];
    }

        //Google Maps    
    var imagUrls = {
        oneOn: 'http://maps.google.com/mapfiles/kml/pal3/icon47.png',
        oneOff: 'http://maps.google.com/mapfiles/kml/pal3/icon39.png'
        //oneOff: 'assets/img/blue24.png',
        //oneOn: 'assets/img/green24.png'
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
        var compiled = $compile('<div class="noscrollbar" style="background:white;"><div style="color: #FC8638;">' + studio.name + '</div><div><span>₹ ' + studio.price + '</span></div></div>')($scope);
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
                console.log(response.routes[0].legs[0].distance.text);
                directionsDisplay.setDirections(response);
            }
        });
    }

$scope.bindstudio=function(data){
    console.log(data);
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
        $scope.morefilter = !$scope.morefilter;
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
        console.log($scope.studioservicefilter);
    }

    $scope.applyfilter = function () {
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

    //Sort
    $scope.$watch('sortservice', function () {
        angular.forEach($scope.studiosort, function (sort, key) {
            if (sort.value == $scope.sortservice) {
                $scope.orderProp = sort.property;
                $scope.direction = sort.direction;
            }
        });
        removemarker();
        clearlatlongbound();
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
    });

    $scope.studiodetails = function (id) {
        var studio = lodash.where($scope.studio, { 'id': id });
        if (studio.length > 0) {
            $scope.selectedstudio = studio[0];
            $scope.selectedstudio['type_icon_class']  = lodash.where($scope.studiotype,{'name':$scope.selectedstudio.studio_type.type_desc})[0].icon;
            $scope.selectedstudio['kind_icon_class']  = lodash.where($scope.studiokind,{'name':$scope.selectedstudio.studio_kind.kind_desc})[0].icon;
            $scope.sortservicebyfilter();
            $('.header-tabs').removeClass('stick');
            $('#studiodetails').toggle('slide', { direction: 'right' }, 200);
            $scope.reviewPage = 1;
            $scope.directionlocation=$scope.searchdata.location;
            var page = Math.round($scope.selectedstudio.studio_review.length / 5);
            page = page + ($scope.selectedstudio.studio_review.length % 5 > 0 ? 1 : 0);            
            $scope.reviewtotalpage = page;            
            $scope.shopdistance = $scope.selectedstudio.distance;
            removemarker();
            drawdirection($scope.selectedstudio.latitude, $scope.selectedstudio.longitude);
            setTimeout(function () {
                top = { 'street-info': $('.street-info').position().top, 'service-list': $('.service-list').position().top, 'review-detail': $('.review-detail').position().top, 'direction': $('.direction').position().top };
                console.log(JSON.stringify(top));
            }, 1000);

        }
    }
    $scope.closeslider = function () {
        $('#studiodetails').toggle('slide', { direction: 'right' }, 100);
        directionsDisplay.setMap(null);
        clearlatlongbound();
        $scope.addmarker((($scope.currentPage - 1) * $scope.itemLimit), (($scope.currentPage - 1) * $scope.itemLimit) + $scope.itemLimit);
        autozoom();
    }
    $scope.easyscroll = function (clsname) {
        $('.list-detail-box').animate({
            scrollTop: top[clsname] - 140
        }, 200);
    }

    $scope.morereview = function () {
        $scope.reviewPage = $scope.reviewPage + 1;
    }

    $scope.changedirection=function(){
        directionsDisplay.setMap(null);
        drawdirection($scope.selectedstudio.latitude, $scope.selectedstudio.longitude);
        var request = { origin: new google.maps.LatLng($scope.selectedstudio.latitude, $scope.selectedstudio.longitude), destination: $scope.directionlocation, travelMode: google.maps.DirectionsTravelMode.DRIVING };
        directionsService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                console.log(response.routes[0].legs[0].distance.text);
                $scope.shopdistance = parseFloat(response.routes[0].legs[0].distance.text);
                $scope.$apply();
            }
        });
        //$scope.shopdistance
    }

    $scope.sortservicebyfilter = function () {
        $scope.servicelist = [];
        var res = lodash.where($scope.selectedstudio.studio_detail_for_activity, { service: { service_name: $scope.searchdata.service } });
        $scope.servicelist.push({ servicename: res[0].service.service_name, price: res[0].price, flag: true });
        $scope.serviceprice = res[0].price;
        angular.forEach($scope.studioservicefilter, function (service, key) {
            res = lodash.where($scope.selectedstudio.studio_detail_for_activity, { service: { service_name: service } });
            if (lodash.findIndex($scope.servicelist, { 'servicename': res[0].service.service_name }) == -1) {
                $scope.servicelist.push({ servicename: res[0].service.service_name, price: res[0].price, flag: false });
            }
        });
        angular.forEach($scope.selectedstudio.studio_detail_for_activity, function (service, key) {
            if (lodash.findIndex($scope.servicelist, { 'servicename': service.service.service_name }) == -1) {
                $scope.servicelist.push({ servicename: service.service.service_name, price: service.price, flag: false });
            }
        });
    }
    $scope.addservice = function (service) {
        console.log(service);
        var index = lodash.findIndex($scope.servicelist, service);
        var flag = $scope.servicelist[index].flag;
        $scope.servicelist[index].flag = !$scope.servicelist[index].flag;
        if (flag) {
            $scope.serviceprice = $scope.serviceprice - service.price;
        }
        else {
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
    $scope.bindstudio(data);
});