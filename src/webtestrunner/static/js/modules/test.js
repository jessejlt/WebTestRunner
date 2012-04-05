(function(Tests) {

  Tests.Model = Backbone.Model.extend({

    url: "/status"

  });

  Tests.Views.Tests = Backbone.View.extend({

    initialize: function() {

      this.model = new this.model();
      this.model.bind("change", this.render, this);

      this.model.fetch();
    },

    render: function() {

      var status = this.model.get("status");
      var template = _.template('<div class="alert alert-error"><strong>Initialization error... </strong> <%= errorMessage %></div>');

      if (status !== true) {

        $(this.el).append(template(this.model.attributes));
      }
    }

  });

})(testRunner.module("test"));
