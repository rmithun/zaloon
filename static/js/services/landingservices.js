accountURL = 'account/'
studioURL = '/studios/'

noqapp.factory('landingServices', function($http,$q) 
{	
	var landingData = {}
	landingData.invite = function(data){	
		var email_invite =  $http.post(accountURL+'invite_user/',data);
		return $q.all({'email_invite':email_invite})
	}

	landingData.getAllAreaStudios = function()
	{
		var allstudios = $http.get(studioURL+"all_studios/")
		return $q.all({'allstudios':allstudios})	
	}
    return landingData;
});