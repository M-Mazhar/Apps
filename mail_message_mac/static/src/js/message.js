/** @odoo-module **/

import {
    registerClassPatchModel,
    registerFieldPatchModel,
} from '@mail/model/model_core';
import { attr } from '@mail/model/model_field';

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





