noqapp.directive('facebook', function($http,httpServices) {
  return {
    restrict: 'A',
    scope: true,
    controller: function($scope, $attrs) {
      // Load the SDK Asynchronously
      (function(d){
        var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement('script'); js.id = id; js.async = true;
        js.src = "https://connect.facebook.net/en_US/all.js"; 
        ref.parentNode.insertBefore(js, ref);
      }(document));

      function login() {
        FB.login(function(response) {
          if (response.authResponse) {
            console.log(response)
            $scope.login_status =  response.status
            $scope.fbLogin(response.authResponse.accessToken)
            console.log('FB.login connected');
          } else {
            console.log('FB.login cancelled');
          }
          }, { scope: 'email,user_location,user_birthday' }
        );
      };

    
      $scope.fetch = function() {
        console.log($scope.login_status)
        if ($scope.login_status != 'connected') {
          login();
          return false
         } 
      };
    },
    link: function(scope, element, attrs, controller) {
      // Additional JS functions here
      window.fbAsyncInit = function() {
        FB.init({
          appId      : attrs.facebook, // App ID
          channelUrl : '//localhost:8000/static/js/channel.html', // Channel File
          //channelUrl : '//zaloon.in/static/js/channel.html', // Channel File
          status     : true, // check login status
          cookie     : true, // enable cookies to allow the server to access the session
          xfbml      : true  // parse XFBML
        });
      }; // end of fbAsyncInit
    }
  }
});



// Phone Number Formatting Directive
noqapp.directive("phoneformat", function() {
    return {
        restrict: "A",
        require: "ngModel",
        link: function(scope, element, attr, ngModelCtrl) {
            var phoneParse = function(value) {
                var numbers = value && value.replace(/-/g, "");
                if (/^\d{10}$/.test(numbers)) {
                    return numbers;
                }

                return undefined;
            }
            var phoneFormat = function(value) {
                var numbers = value && value.replace(/-/g, "");
                var matches = numbers && numbers.match(/^(\d{3})(\d{3})(\d{4})$/);

                if (matches) {
                    return matches[1] + "-" + matches[2] + "-" + matches[3];
                }

                return undefined;
            }
            ngModelCtrl.$parsers.push(phoneParse);
            ngModelCtrl.$formatters.push(phoneFormat);

            element.bind("blur", function() {
                var value = phoneFormat(element.val());
                var isValid = !!value;
                if (isValid) {
                    ngModelCtrl.$setViewValue(value);
                    ngModelCtrl.$render();
                }

                ngModelCtrl.$setValidity("mobileno", isValid);
                scope.$apply();
            });
        }
    };
});

