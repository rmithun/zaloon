var secretEmptyKey = '[$empty$]'
var noqapp = angular.module('accountApp', ['ngAnimate','ngCookies','ngRoute','ui.bootstrap','ngLodash','ui.editable','ngTouch','ui.bootstrap.setNgAnimate', 'am.resetField']);

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
                               '<span class="editable-buttons resetpanel" style="margin-top:2px">' +
                                   '<button type="submit" class="btn apply-btn" style="margin:0px 3px;" ng-click="editableok()">' +
                                       '<span class="glyphicon glyphicon-ok"></span>' +
                                   '</button>' +
                                   '<button type="button" class="btn reset-btn" style="margin:0px 3px;" ng-click="editablecancel()">' +
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

angular.module('ui.bootstrap.setNgAnimate', ['ngAnimate']).directive('disableNgAnimate', ['$animate', function ($animate) {
    return {
        restrict: 'A',
        link: function (scope, element) {
            $animate.enabled(false, element);
        }
    };
} ]);


noqapp.directive('focusMe', function($timeout, $parse) {
      return {
          //scope: true,   // optionally create a child scope
          link: function(scope, element, attrs) {
              var model = $parse(attrs.focusMe);
              scope.$watch(model, function(value) {
                  if(value === true) { 
                      $timeout(function() {
                          element[0].focus();
                      });
                  }
              });
          }
      };
    });

noqapp.directive('emptyTypeahead', function () {
      return {
        require: 'ngModel',
        link: function (scope, element, attrs, modelCtrl) {
          // this parser run before typeahead's parser
          modelCtrl.$parsers.unshift(function (inputValue) {
            var value = (inputValue ? inputValue : secretEmptyKey); // replace empty string with secretEmptyKey to bypass typeahead-min-length check
            modelCtrl.$viewValue = value; // this $viewValue must match the inputValue pass to typehead directive
            return value;
          });
          
          // this parser run after typeahead's parser
          modelCtrl.$parsers.push(function (inputValue) {
            return inputValue === secretEmptyKey ? '' : inputValue; // set the secretEmptyKey back to empty string
          });
        }
      }
    });

angular.module('am.resetField', []).directive('amResetField', ['$compile', '$timeout', function($compile, $timeout) {
  return {
    require: 'ngModel',
    scope: {
      resetclass:'='
    },
    link: function(scope, el, attrs, ctrl) {
      // limit to input element of specific types
      var inputTypes = /text|search|tel|url|email|password/i;
      if (el[0].nodeName !== "INPUT")
        throw new Error("resetField is limited to input elements");
      if (!inputTypes.test(attrs.type))
        throw new Error("Invalid input type for resetField: " + attrs.type);

      // compiled reset icon template
      var template = $compile('<i ng-show="enabled" ng-mousedown="reset()" class="fa fa-times" ng-class="resetclass"></i>')(scope);
      el.after(template);

      scope.reset = function() {
        ctrl.$setViewValue(null);
        ctrl.$render();
        $timeout(function() {
            el[0].focus();
        }, 0, false);
      };

      el.bind('input', function() {
        scope.enabled = !ctrl.$isEmpty(el.val());
      })
      .bind('focus', function() {
        scope.enabled = !ctrl.$isEmpty(el.val());
        scope.$apply();
      })
      .bind('blur', function() {
        scope.enabled = true;
        scope.$apply();
      });
    }
  };
}]);
