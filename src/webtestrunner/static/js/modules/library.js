(function(Library) {

  Library.Model = Backbone.Model.extend({

  });

  Library.Views.Library = Backbone.View.extend({

    el: "#test-library",

    events: {

      "click #submit-library": "updateTestLibrary"
    },

    initialize: function() {

      $(this.el).modal({backdrop: true});
    },

    updateTestLibrary: function() {

      var library = $(this.el).find("input").val();

      if (library) {

        app.router.navigate("library/" + library, {trigger: true});
        $(this.el).modal("hide");
      } else {

        // TODO
        // error state
      }
    }

  });

})(testRunner.module("library"));
