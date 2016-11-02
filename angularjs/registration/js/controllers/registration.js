myApp.controller('RegistrationController',
  ['$scope', '$firebaseAuth',
  function($scope, $firebaseAuth) {

  var auth = $firebaseAuth();
  
  $scope.login = function() {
    $scope.firebaseUser = null;
    $scope.message = null;

    auth.$signInAnonymously().then(function(firebaseUser) {
    	$scope.firebaseUser = firebaseUser;
    }).catch(function(error) {
    	$scope.message = error;
    });
  }; //login

  $scope.register = function() {
    auth.$createUserWithEmailAndPassword($scope.email, $scope.password)
        .then(function(firebaseUser) {
          $scope.message = "User created with uid: " + firebaseUser.uid;
        }).catch(function(error) {
          $scope.message = error;
        }); // createUserWithEmailAndPassword
  }; // register

}]); // Controller