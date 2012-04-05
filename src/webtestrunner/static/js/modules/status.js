(function(Status) {

  Status.Model = Backbone.Model.extend({

    url: "/status"

  });

  Status.Views.Status = Backbone.View.extend({

    model: Status.Model,
    el: "#init-message",

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

})(testRunner.module("status"));
