odoo.define('barcode_tare',function(require) {
	"use strict";
	var screens = require('point_of_sale.screens');

	screens.ScreenWidget.include(
	{
		barcode_weight_action: function(code){
	        var self = this;
            var order = this.pos.get_order();
            var last_order_line = order.get_last_orderline();
            var total_weight = last_order_line.get_quantity();
            var tare = code.value;
            var paid_weight = total_weight - tare;

            last_order_line.set_quantity(paid_weight)
        },

        show: function(){
            var self = this;
            this._super()
            this.pos.barcode_reader.set_action_callback('weight',  _.bind(self.barcode_weight_action, self))
        },
	});
});
