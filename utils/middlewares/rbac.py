from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re
from django.http import JsonResponse
from utils.base_response import BaseResponse


class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ret = BaseResponse()
        try:
            # 对权限进行校验
            # 1.当前访问的URL
            current_url = request.path_info
            # 白名单的判断
            for i in settings.WHITE_URL_LIST:
                if re.match(i, current_url):
                    return
            # 如果是超级管理员，不做任何处理，这一部分可以省略，偷懒代码
            role = request.session.get('role')
            if role == '超级管理员':
                return
            # 2.获取当前用户的所有权限信息
            permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
            # 3.权限的校验
            if permission_list is not None:
                for item in permission_list:
                    url = item[0]
                    if re.match('^{}$'.format(url), current_url):
                        return

            ret.code = 108
            ret.data = '当前身份没有权限'
            return JsonResponse(ret.dict)
        except Exception as e:
            ret.code = 109
            ret.data = '出现一点小问题'
            return JsonResponse(ret.dict)