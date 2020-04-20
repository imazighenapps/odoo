odoo.define('z_debranding.dashboard', function (require) {
"use strict";

    var dashboard = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/web_settings_dashboard');
    dashboard.Dashboard.include({
        start: function(){
            this.all_dashboards = _.without(this.all_dashboards, 'share');

            // remove Share section completly
            this.$('.o_web_settings_dashboard_share').parent().remove();

            var self = this;
            return this._super().then(function(){
                // Remove bottom of Apps settion (links to odoo apps store)
                self.$('.o_browse_apps').parent().nextAll().remove();
            });
        },
    });
});
