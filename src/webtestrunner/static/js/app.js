
(function() {

    window.onbeforeunload = function(e) {

        $.get("/exit");
    }

    var $ = jQuery;

    if (window.app === undefined) window.app            = {};
    if (app.models === undefined) app.models            = {};
    if (app.collections === undefined) app.collections  = {};
    if (app.ui === undefined) app.ui                    = {};

    app.VERSION = '0.0.1';

    app.init = function(options) {

        var defaults = {
            callbacks : {

            }
        };

        this.options            = _.extend({}, defaults, options);
        app.events              = _.extend({}, Backbone.Events);

        var router              = testRunner.module("router");
        var status              = testRunner.module("status");
        var library             = testRunner.module("library");
        var tests               = testRunner.module("tests");

        app.router              = new router.Routes();

        app.ui.status           = new status.Views.Status();
        app.ui.library          = new library.Views.Library();
        app.ui.tests            = new tests.Views.Tests();
        app.ui.errors           = new tests.Views.Error();

        Backbone.history.start();

        return this;
    };

    app.init();

})();













