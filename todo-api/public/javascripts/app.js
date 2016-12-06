var myApp = angular.module('myApp', [
  'ngRoute', 
  'ngResource',
  'todoControllers']);

myApp.factory('Todos', ['$resource', function($resource){
  return $resource('/todos/:id', null, {
    'update': { method:'PUT' }
  });
}]);

myApp.config(['$routeProvider', function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: '/todos.html',
      controller: 'TodoController'
    })
    .when('/:id', {
      templateUrl: '/todoDetails.html',
      controller: 'TodoDetailCtrl'
   }).
  otherwise({
    redirectTo: '/'
  });
}]);