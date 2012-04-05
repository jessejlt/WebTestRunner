// Change *namespace* to your namespace!
// This contains the module definition factory function, application state,
// events, and the router.
this.testRunner = {
  // Assist with code organization, by breaking up logical components of code
  // into modules.
  module: function() {
    // Internal module cache.
    var modules = {};

    // Create a new module reference scaffold or load an existing module.
    return function(name) {
      // If this module has already been created, return it.
      if (modules[name]) {
        return modules[name];
      }

      // Create a module and save it under this name
      return modules[name] = { Views: {} };
    };
  }(),

  // This is useful when developing if you don't want to use a
  // build process every time you change a template.
  //

  // Keep active application instances namespaced under an app object.
  app: _.extend({}, Backbone.Events)
};
