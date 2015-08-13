  var noqapp = angular.module('accountApp', ['ngCookies','ngRoute','ui.bootstrap','ngLodash','ui.editable']);

noqapp.run(function($http,$cookies,sessionService) {

	$http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');

});

// configure our routes
noqapp.config(function($routeProvider,$httpProvider) {

	$httpProvider.interceptors.push('authInterceptor');
  

		$routeProvider
			// route for the home page
			.when('/', {
				templateUrl : '/home/',
				controller  : 'homepagecontroller'
			})
			
			.when('/search', {
				templateUrl : '/search/',
				controller  : 'resultCtrl'
			})

			.when('/my_account', {
				templateUrl : '/account/user_account/',
				controller  : 'accountscontroller'
			})

			.when('/home', {
				templateUrl : '/home/',
				controller  : 'homepagecontroller'
			})

			.when('/booking', {
				templateUrl : '/booking/booking_page/'
			})

});

angular.module("ui.editable", []).directive('txtEditable', function (httpServices) {
   return {
       restrict: 'E',
       scope: {
           editableModel: '=',
           editableKey: '@'
       },
       template: '<span ng-show="show" ng-model="editableModel" style="font-weight:400 !important;" class="ng-scope ng-binding editable editable-click">{{editableModel || "empty"}}</span>' +
                           '&nbsp;<i ng-show="show" ng-click="editshow()" style="cursor:pointer;" class="glyphicon glyphicon-pencil"></i>' +
                           '<div ng-show="!show" class="editable-controls form-group">' +
                               '<input type="text" class="editable-has-buttons editable-input form-control" ng-model="txtval" />' +
                               '<span class="editable-buttons" style="margin-top:2px">' +
                                   '<button type="submit" class="btn btn-primary" ng-click="editableok()">' +
                                       '<span class="glyphicon glyphicon-ok"></span>' +
                                   '</button>' +
                                   '<button type="button" class="btn btn-default" ng-click="editablecancel()">' +
                                       '<span class="glyphicon glyphicon-remove"></span>' +
                                   '</button></span></div>',
       controller: function ($scope) {
           $scope.show = true;
           $scope.editshow = function () {
               $scope.show = false;
               $scope.txtval = $scope.editableModel;
               $scope.oldval = angular.copy($scope.editableModel);
           }
           $scope.editableok = function () {
               $scope.editableModel = $scope.txtval;
               $scope.show = true;
               obj = {}
               obj[$scope.editableKey] =  $scope.editableModel
        	   httpServices.updateUserProfile(obj).then(function(data)
        	   	{
        	   		console.log("Updated successfully")
        	   		console.log(data)
        	   		//message as updated
        	   	},function()
        	   	{
        	   		$scope.editableModel = $scope.oldval
        	   		//error message that it is not updated
        	   	});

           }
           $scope.editablecancel = function () {
               $scope.show = true;
           }
       }
   };
});

noqapp.directive('clearIcon', ['$compile', function($compile) { 
  return { 
    restrict : 'A', 
    link : function(scope, elem, attrs) { 
      var model = attrs.ngModel; var template = '<span ng-click=\"clearText(\'' + model + '\')\" class="clearIcon" style="display:none;">x</span>'; 
      elem.parent().append($compile(template)(scope)); 
      var clearIconToggle = function(toggleParam) { 
        if(elem.val().trim().length) 
          elem.next().css("display", "inline"); 
        else { 
          if(elem.next().css("display") == "inline") 
            elem.next().css("display", "none"); 
        } 
      }; 
      var clearText = function(clearParam) { 
        elem.val(''); 
        clearIconToggle(clearParam); 
      }; 
      elem.on("focus", function(event) { 
        clearIconToggle(model); 
      }); 
      elem.on("keyup", function(event) { 
        clearIconToggle(model); 
      }); 
      elem.next().on("click", function(event) { 
        elem.val(''); elem.next().css("display", "none"); 
      }); 
    } 
  }; 
}]);
