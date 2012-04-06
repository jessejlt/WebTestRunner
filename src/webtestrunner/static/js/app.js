
(function() {

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
        app.errorModalEl        = "#error-message";

        var router              = testRunner.module("router");
        var status              = testRunner.module("status");
        var library             = testRunner.module("library");
        var tests               = testRunner.module("tests");

        app.router              = new router.Routes();

        app.ui.status           = new status.Views.Status();
        app.ui.library          = new library.Views.Library();
        app.ui.tests            = new tests.Views.Tests();

        Backbone.history.start();

        return this;
    };

    app.init();
    $(app.errorModalEl).modal({show: false});
    $(app.errorModalEl).hide();
    $(app.errorModalEl).find(".modal-footer button").click(function() {
        $(app.errorModalEl).hide();
    });

})();













