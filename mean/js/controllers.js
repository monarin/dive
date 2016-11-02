var todoControllers = angular.module('todoControllers', []);

todoControllers.controller('TodoController', ['$scope', 'Todos', function ($scope, Todos) {
  $scope.todos = Todos;
}])

todoControllers.controller('TodoDetailCtrl', ['$scope', '$routeParams', 'Todos', function ($scope, $routeParams, Todos) {
  $scope.todo = Todos[$routeParams.id];
}])