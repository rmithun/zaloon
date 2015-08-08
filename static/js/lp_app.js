var noqapp = angular.module('landingApp', ['ngCookies']);
noqapp.run(function($http,$cookies) {

	$http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');

});

