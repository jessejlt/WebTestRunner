(function(Tests) {

  Tests.Model = Backbone.Model.extend({


    url: function() {

      return "/test/name/" + this.get("name") + "/module/" + this.get("module");
    }
  });

  Tests.Collection = Backbone.Collection.extend({

    model: Tests.Model,

    setLibrary: function(library) {
      this.library = library;
    },

    url: function() {
      return "/tests/" + this.library;
    },

    parse: function(response) {

      return response.tests;
    }

  });

  Tests.Views.Tests = Backbone.View.extend({

    el: "#tests",

    events: {

      "click td > input[type=checkbox]": "selectTest",
      "click th > input[type=checkbox]": "selectAllTests",
      "click tfoot button": "executeSelectedTests",
      "click tr[teststatus=false]": "showTestError",
      "click tr[teststatus=true]": "showTestError"
    },

    initialize: function() {

      app.events.bind("fetch-tests", this.fetchTestsForLibrary, this);
      this.tests = new Tests.Collection();
      this.tests.on("reset", this.render, this);
      this.tests.on("change", this.testUpdate, this);
      this.numSelectedTests = 0;
    },

    showTestError: function(e) {

      // TODO stop this from being activated on checkbox click
      var id = $(e.currentTarget).data("id");
      var test = this.tests.get(id);

      app.events.trigger("show-error", test);
    },

    testUpdate: function(test) {

      if (test.has("pass") === false) {
        return;
      }

      $(this.el).find("tr[data-id=" + test.id + "]").attr("testStatus", test.get("pass"));
    },

    executeSelectedTests: function() {

      var tests = this.tests.where({testPending: true});
      if (tests.length === 0) {
        return false;
      }

      this.initProgressBar(tests.length);
      _.each(tests, function(test) {

        test.fetch();
      });
    },

    initProgressBar: function(numTests) {

    },

    selectTest: function(e) {

      var id = $(e.currentTarget).parents("tr").data("id");
      var model = this.tests.get(id);
      var swapLogic = true;

      // Okay, so if we arrive here via a user-click, then
      // e.isTrigger is undefined, and variable <swapLogic>
      // is set to true, in essence, none of the is(":checked")
      // logic changes; however, if we arrive here via a jQuery.click
      // event, then e.isTrigger is defined, and e.is(":checked") is
      // actually still false, because the dom is still updating, so we
      // swap the is(":checked") logic to accomodate
      if (e.isTrigger === true) {

        swapLogic = false;
      } else {

        swapLogic = true;
      }

      if ($(e.currentTarget).is(":checked") === swapLogic) {

        model.set("testPending", true);
        this.numSelectedTests += 1;
      } else {

        model.set("testPending", false);
        this.numSelectedTests -= 1;
      }

      // $(this.el).find("th.tests-selection").text("selected tests = " + this.numSelectedTests);
    },

    selectAllTests: function(e) {

      // .click() gives us the click event, but will toggle any
      // checkboxes, but we don't want to toggle, we want to set,
      // so first we overwrite all checkboxes with the opposite of
      // the requested state, then we .click()
      if ($(e.currentTarget).is(":checked")) {

        $(this.el).find("tbody input[type=checkbox]").removeAttr("checked");
      } else {

        $(this.el).find("tbody input[type=checkbox]").attr("checked", true);
      }

      $(this.el).find("tbody input[type=checkbox]").click();
    },

    fetchTestsForLibrary: function(library) {

      if (library) {

        this.tests.setLibrary(library);
        this.tests.fetch();
      }
    },

    render: function() {

      var template = _.template('<tr data-id="<%= id %>"><td><input type="checkbox" value="option1"></td><td><%= module %></td><td><%= name %></td></tr>');
      var models = this.tests.models;
      var tbody = $(this.el).find("tbody");

      _.each(models, function(model) {

        $(tbody).append(template(model.attributes));
      });

      $("#tests-progress").hide();
      $(this.el).show();
    }

  });

  Tests.Views.Error = Backbone.View.extend({

    el: "#error-message",

    initialize: function() {

      app.events.on("show-error", this.onError, this);
      this.template = _.template('<div class="alert alert-block alert-error fade in"><a class="close" data-dismiss="alert" href="#">×</a><h4 class="alert-heading"><%= module %>:<%= name %></h4><pre><code data-language="python"><%= stack %></code></pre></div>');

    },

    onError: function(test) {

      var testPassed = test.get("pass");

      $(this.el).empty();
      if (testPassed !== false) {
        return;
      }

      $(this.el).html(this.template(test.attributes));
      $(this.el).find(".alert").alert();
    }

  });

})(testRunner.module("tests"));
