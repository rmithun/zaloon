accountsApp.directive('facebook', function($http) {
  return {
    restrict: 'A',
    scope: true,
    controller: function($scope, $attrs) {
      // Load the SDK Asynchronously
      (function(d){
        var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement('script'); js.id = id; js.async = true;
        js.src = "//connect.facebook.net/en_US/all.js";
        ref.parentNode.insertBefore(js, ref);
      }(document));

      function login() {
        FB.login(function(response) {
          if (response.authResponse) {
            console.log(response)
            $scope.fbLogin(response.authResponse.accessToken)
            console.log('FB.login connected');
          } else {
            console.log('FB.login cancelled');
          }
          }, { scope: 'email,user_location,user_birthday' }
        );
      };

    
      $scope.fetch = function() {
        if ($scope.login_status != 'connected') {
          login()
        } 
      };
    },
    link: function(scope, element, attrs, controller) {
      // Additional JS functions here
      window.fbAsyncInit = function() {
        FB.init({
          appId      : attrs.facebook, // App ID
          //channelUrl : '//localhost:3000/channel.html', // Channel File
          status     : true, // check login status
          cookie     : true, // enable cookies to allow the server to access the session
          xfbml      : true  // parse XFBML
        });
      }; // end of fbAsyncInit
    }
  }
});