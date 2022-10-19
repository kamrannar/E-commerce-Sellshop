from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from blog.models import BlockedIP

class BlockIPMiddleware(MiddlewareMixin):
    def process_request(self,request):
        bloked_ips_qs = BlockedIP.objects.all()
        blocked_ips = [ip.ip_addr for ip in bloked_ips_qs]   
        # print(request.META['REMOTE_ADDR'])
        if request.META['REMOTE_ADDR'] in blocked_ips:
            
            return HttpResponseForbidden('<h1> Forbidden!</h1>')
