odoo.define('pos_accented_search', function (require) {

    "use strict";
     var db = require("point_of_sale.DB");
     db.include({

        init: function(options){
            this._super(options);
            this.accented_replacement =
                {"œ": "oe", "á":"a", "á":"a", "ç":"c", "é": "e", "è":"e", "ê": "e", "ë": "e",
                 "Œ": "OE", "Á":"A", "Á":"A", "Ç":"C", "É": "E", "È":"E", "Ê": "E", "Ë": "E"};
        },

        remove_accented_characters: function(product, replacement=this.accented_replacement){
            return product.replace(/[^\w ]/g, function(char) {
                return replacement[char] || char;
                });
        },

        _product_search_string: function(product){
            return this.remove_accented_characters(this._super(product));
        },

        search_product_in_category: function(category_id, query){
            return this._super(category_id, this.remove_accented_characters(query))
        }
     });

     return db;

});