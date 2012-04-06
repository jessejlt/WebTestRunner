(function(Router) {

  Router.Routes = Backbone.Router.extend({

    routes: {
      "library/:library": "testLibrary"
    },

    testLibrary: function(library) {

      app.events.trigger("fetch-tests", library);
    }

  });


})(testRunner.module("router"));
