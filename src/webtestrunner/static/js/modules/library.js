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
      app.events.bind("fetch-tests", this.closeModal, this);

      $(this.el).submit(function(e) {e.preventDefault();});
    },

    closeModal: function() {

      $(this.el).modal("hide");
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
