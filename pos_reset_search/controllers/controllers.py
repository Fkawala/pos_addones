# -*- coding: utf-8 -*-
from openerp import http

# class PosResetSearch(http.Controller):
#     @http.route('/pos_reset_search/pos_reset_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_reset_search/pos_reset_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_reset_search.listing', {
#             'root': '/pos_reset_search/pos_reset_search',
#             'objects': http.request.env['pos_reset_search.pos_reset_search'].search([]),
#         })

#     @http.route('/pos_reset_search/pos_reset_search/objects/<model("pos_reset_search.pos_reset_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_reset_search.object', {
#             'object': obj
#         })