import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CouponCode(Model):

    fields = ["code", "coupon_id", "coupon_set_name"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', '/coupon_codes', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/coupon_codes/%s' % id, None, env)
