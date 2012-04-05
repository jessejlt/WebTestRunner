(function(Router) {

  Router.Routes = Backbone.Router.extend({

    routes: {
      "library/:library": "testLibrary"
    },

    testLibrary: function(library) {

      app.ui.library.fetchTestsForLibrary(library);
    }

  });


})(testRunner.module("router"));
