odoo.define('z_debranding.dialog', function(require) {

    require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/z_debranding.base');
    var core = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/web.core');
    var QWeb = core.qweb;
    var session = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/web.session');
    var _t = core._t;

    var Dialog = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/web.Dialog');
    Dialog.include({
        init: function (parent, options) {
            var debranding_new_name = odoo.debranding_new_name;
            var debranding_new_website = odoo.debranding_new_website;
            options = options || {};
            if (options.title && options.title.replace){
                var title = options.title.replace(/Odoo/ig, debranding_new_name);
                options.title = title;
            } else {
                options.title = debranding_new_name;
            }
            if (options.$content){
                if (!(options.$content instanceof $)){
                    options.$content = $(options.$content);
                }
                var content_html = options.$content.html();
                content_html = content_html.replace(/Odoo.com/ig, debranding_new_website);
                content_html = content_html.replace(/Odoo/ig, debranding_new_name);
                options.$content.html(content_html);
            }
            this._super(parent, options);
        },
    });
});
