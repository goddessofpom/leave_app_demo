define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./apidoc/main.js",
    "group": "E:\\leave_app\\apidoc\\main.js",
    "groupTitle": "E:\\leave_app\\apidoc\\main.js",
    "name": ""
  },
  {
    "type": "post",
    "url": "/api/create_ticket/",
    "title": "创建工单",
    "version": "1.0.0",
    "group": "app",
    "name": "创建工单",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "transition_id",
            "description": "<p>新建工单流转id</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"code\": 0,\n    \"msg\": \"\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "post",
    "url": "/api/handle_ticket/",
    "title": "处理工单",
    "version": "1.0.0",
    "group": "app",
    "name": "处理工单",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ticket_id",
            "description": "<p>工单id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "transition_id",
            "description": "<p>流转id</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"code\": 0,\n    \"msg\": \"\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "post",
    "url": "/api/user_logout/",
    "title": "用户登出",
    "version": "1.0.0",
    "group": "app",
    "name": "用户登出",
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"logout success!\"\n}",
          "type": "text"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "post",
    "url": "/api/user_login/",
    "title": "用户登录",
    "version": "1.0.0",
    "group": "app",
    "name": "用户登录",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>用户名</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"login success!\"\n}",
          "type": "text"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "get",
    "url": "/api/get_workflow_init_state/",
    "title": "获取工作流初始状态",
    "version": "1.0.0",
    "group": "app",
    "name": "获取工作流初始状态",
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"code\": 0,\n    \"msg\": \"\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "get",
    "url": "/api/ticket_list/",
    "title": "获取工单列表",
    "version": "1.0.0",
    "group": "app",
    "name": "获取工单列表",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>页码</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"code\": 0,\n    \"msg\": \"\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "get",
    "url": "/api/ticket_transition/",
    "title": "获取工单可以做的操作",
    "version": "1.0.0",
    "group": "app",
    "name": "获取工单可以做的操作",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ticket_id",
            "description": "<p>工单id</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"code\": 0,\n    \"msg\": \"\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  },
  {
    "type": "get",
    "url": "/api/ticket_detail/",
    "title": "获取工单详情",
    "version": "1.0.0",
    "group": "app",
    "name": "获取工单详情",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ticket_id",
            "description": "<p>工单id</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response-Example",
          "content": "{\n    \"code\": 0,\n    \"msg\": \"\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./app/views.py",
    "groupTitle": "app"
  }
] });
