(function(Library) {

  Library.Model = Backbone.Model.extend({

    urlRoot: "/tests"

  });

  Library.Views.Library = Backbone.View.extend({

    el: "#test-library",

    events: {

      "click .btn": "updateTestLibrary"
    },

    initialize: function() {


    },

    updateTestLibrary: function() {

      var library = $(this.el).find("input").val();

      if (library) {

        app.router.navigate("library/" + library, {trigger: true});
      } else {

        // TODO
        // error state
      }
    },

    fetchTestsForLibrary: function(library) {

      if (this.model !== undefined) {
        this.model.off();
      }

      this.model = new Library.Model({id: library});
      this.model.bind("change", this.render, this);
      this.model.fetch();
    },

    render: function() {

      var tests = this.model.attributes;

      _.each(tests, function(test) {

        if (test.length === 3) {

          var module = test[1];
          var testName = test[2];

          var moduleParts = module.split(".");
          var packageName = moduleParts[moduleParts.length - 1];
        }
      });
    }

  });

})(testRunner.module("library"));
