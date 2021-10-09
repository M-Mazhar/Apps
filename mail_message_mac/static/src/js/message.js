odoo.define('mail_message_mac/static/src/js/message.js', function (require) {
'use strict';

const {
    registerInstancePatchModel,
    registerFieldPatchModel,
    registerClassPatchModel,
} = require('mail/static/src/model/model_core.js');
const { attr, many2many, many2one, one2many } = require('mail/static/src/model/model_field.js');


registerFieldPatchModel('mail.message', 'mail_message_mac/static/src/js/message.js', {
    /**
     * New field added.
     */
     mac_address: attr({
            default: "View Profile",
        }),
});

registerClassPatchModel('mail.message', 'mail_message_mac/static/src/js/message.js', {
    /**
     * @override
     To add to get data into new field
     */
    convertData(data) {
        const data2 = this._super(data);
        if ('mac_address' in data) {
            data2.mac_address = data.mac_address;
        }
        return data2;
    },
});

/*if you need to override the function other than static, you have to patch the Instance not registerInstancePatchModel*/

});




