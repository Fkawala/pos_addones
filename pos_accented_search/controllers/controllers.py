# -*- coding: utf-8 -*-
from openerp import http

# class PosAccentedSearch(http.Controller):
#     @http.route('/pos_accented_search/pos_accented_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_accented_search/pos_accented_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_accented_search.listing', {
#             'root': '/pos_accented_search/pos_accented_search',
#             'objects': http.request.env['pos_accented_search.pos_accented_search'].search([]),
#         })

#     @http.route('/pos_accented_search/pos_accented_search/objects/<model("pos_accented_search.pos_accented_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_accented_search.object', {
#             'object': obj
#         })