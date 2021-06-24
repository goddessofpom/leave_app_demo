from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, Http404
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
import json
from .utils import workflow_request

# Create your views here.
@csrf_exempt
def user_login(request):
    """
    @api {post} /api/user_login/ 用户登录
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 用户登录

    @apiParam {String} username 用户名
    @apiParam {String} password 密码

    @apiSuccessExample {text} Response-Example
    {
        "login success!"
    }
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login success!")
        else:
            return HttpResponse("login failed!")
    raise Http404

@csrf_exempt
def user_logout(request):
    """
    @api {post} /api/user_logout/ 用户登出
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 用户登出

    @apiSuccessExample {text} Response-Example
    {
        "logout success!"
    }
    """
    if request.method == "POST":
        logout(request)
        return HttpResponse("logout success!")
    raise Http404

def get_workflow_init_state(request):
    """
    @api {get} /api/get_workflow_init_state/ 获取工作流初始状态
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 获取工作流初始状态

    @apiSuccessExample {json} Response-Example
    {
        "code": 0,
        "msg": "",
        "data": {}
    }
    """
    if request.method == "GET":
        workflow_id = settings.LOONFLOW_ID
        url = f"/api/v1.0/workflows/{workflow_id}/init_state"
        data =  workflow_request("get", url, request.user.username)
        return JsonResponse(data)
    raise Http404

def ticket_list(request):
    """
    @api {get} /api/ticket_list/ 获取工单列表
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 获取工单列表

    @apiParam {Number} [page=1] 页码

    @apiSuccessExample {json} Response-Example
    {
        "code": 0,
        "msg": "",
        "data": {}
    }
    """
    if request.method == "GET":
        url = "/api/v1.0/tickets"
        request_data = json.loads(request.body)
        data = workflow_request("get", url, request.user.username, request_data)
        return JsonResponse(data)
    raise Http404

def ticket_detail(request):
    """
    @api {get} /api/ticket_detail/ 获取工单详情
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 获取工单详情

    @apiParam {Number} ticket_id 工单id

    @apiSuccessExample {json} Response-Example
    {
        "code": 0,
        "msg": "",
        "data": {}
    }
    """
    if request.method == "GET":
        ticket_id = request.GET["ticket_id"]
        url = f"/api/v1.0/tickets/{ticket_id}"
        data = workflow_request("get", url, request.user.username)
        return JsonResponse(data)
    raise Http404

def ticket_transition(request):
    """
    @api {get} /api/ticket_transition/ 获取工单可以做的操作
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 获取工单可以做的操作

    @apiParam {Number} ticket_id 工单id

    @apiSuccessExample {json} Response-Example
    {
        "code": 0,
        "msg": "",
        "data": {}
    }
    """
    if request.method == "GET":
        ticket_id = request.GET["ticket_id"]
        url = f'/api/v1.0/tickets/{ticket_id}/transitions'
        data = workflow_request("get", url, request.user.username)
        return JsonResponse(data)
    raise Http404

@csrf_exempt
@permission_required("app.student_perm")
def create_ticket(request):
    """
    @api {post} /api/create_ticket/ 创建工单
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 创建工单

    @apiParam {Number} transition_id 新建工单流转id

    @apiSuccessExample {json} Response-Example
    {
        "code": 0,
        "msg": "",
        "data": {}
    }
    """
    if request.method == "POST":
        url = "/api/v1.0/tickets"
        request_data = json.loads(request.body)
        workflow_id = settings.LOONFLOW_ID
        request_data["workflow_id"] = workflow_id
        data = workflow_request("post", url, request.user.username, request_data)
        return JsonResponse(data)
    raise Http404

@csrf_exempt
@permission_required("app.teacher_perm")
def handle_ticket(request):
    """
    @api {post} /api/handle_ticket/ 处理工单
    @apiVersion 1.0.0
    @apiGroup app
    @apiName 处理工单

    @apiParam {Number} ticket_id 工单id
    @apiParam {Number} transition_id 流转id

    @apiSuccessExample {json} Response-Example
    {
        "code": 0,
        "msg": "",
        "data": {}
    }
    """
    if request.method == "POST":
        request_data = json.loads(request.body)
        ticket_id = request_data.pop("ticket_id")
        url = f'api/v1.0/tickets/{ticket_id}'
        data = workflow_request("patch", url, request.user.username, request_data)
        return JsonResponse(data)
    raise Http404