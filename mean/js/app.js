angular.module('app', [
  'ngRoute',
  'todoControllers'])
    //---------------
    // Services
    //---------------
    .factory('Todos', function(){
      return [
        { name: 'AngularJS Directives', completed: true, note: 'add notes...' },
        { name: 'Data binding', completed: true, note: 'add notes...' },
        { name: '$scope', completed: true, note: 'add notes...' },
        { name: 'Controllers and Modules', completed: true, note: 'add notes...' },
        { name: 'Templates and routes', completed: true, note: 'add notes...' },
        { name: 'Filters and Services', completed: false, note: 'add notes...' },
        { name: 'Get started with Node/ExpressJS', completed: false, note: 'add notes...' },
        { name: 'Setup MongoDB database', completed: false, note: 'add notes...' },
        { name: 'Be awesome!', completed: false, note: 'add notes...' },
      ];
    })
    //---------------
    // Routes
    //---------------
    .config(['$routeProvider', function ($routeProvider) {
      $routeProvider
        .when('/', {
          templateUrl: '/todos.html',
          controller: 'TodoController'
        })
        .when('/:id', {
          templateUrl: '/todoDetails.html',
          controller: 'TodoDetailCtrl'
       });
    }]);