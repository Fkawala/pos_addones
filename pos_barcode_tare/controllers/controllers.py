# -*- coding: utf-8 -*-
from openerp import http

# class BarecodeTare(http.Controller):
#     @http.route('/barecode_tare/barecode_tare/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barecode_tare/barecode_tare/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('barecode_tare.listing', {
#             'root': '/barecode_tare/barecode_tare',
#             'objects': http.request.env['barecode_tare.barecode_tare'].search([]),
#         })

#     @http.route('/barecode_tare/barecode_tare/objects/<model("barecode_tare.barecode_tare"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barecode_tare.object', {
#             'object': obj
#         })