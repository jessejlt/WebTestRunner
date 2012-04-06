(function(Library) {

  Library.Model = Backbone.Model.extend({

  });

  Library.Views.Library = Backbone.View.extend({

    el: "#test-library",

    events: {

      "click .btn": "updateTestLibrary"
    },

    updateTestLibrary: function() {

      var library = $(this.el).find("input").val();

      if (library) {

        app.router.navigate("library/" + library, {trigger: true});
      } else {

        // TODO
        // error state
      }
    }

  });

})(testRunner.module("library"));
