odoo.define('z_debranding.bot', function (require) {
    "use strict";

    require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/z_debranding.dialog');
    var Message = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/mail.model.Message');
    var session = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/web.session');
    var MailBotService = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/mail_bot.MailBotService');
    var core = require('../../../../../z_debranding12/ns_web_debranding/static/src/js/node_modules/web.core');
    var _t = core._t;

    Message.include({
        _getAuthorName: function () {
            if (this._isOdoobotAuthor()) {
                return "Bot";
            }
            return this._super.apply(this, arguments);
        },
        getAvatarSource: function () {
            if (this._isOdoobotAuthor()) {
                return '/web/binary/company_logo?company_id=' + session.company_id;
            }
            return this._super.apply(this, arguments);
        }
    });

    MailBotService.include({
        getPreviews: function (filter) {
            var previews = this._super.apply(this, arguments);
            previews.map(function(preview)  {
                if (preview.title == _t("OdooBot has a request")) {
                    preview.title = _t("Bot has a request");
                }
                if (preview.imageSRC == "/mail/static/src/img/odoobot.png") {
                    preview.imageSRC = '/web/binary/company_logo?company_id=' + session.company_id;
                }
                return preview;
            });
            return previews;
        },
    });

});
