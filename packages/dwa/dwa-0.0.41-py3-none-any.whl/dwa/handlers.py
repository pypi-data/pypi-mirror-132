from concurrent.futures import ThreadPoolExecutor
from http.client import responses as http_status
import tornado.concurrent
import tornado.web
import tornado.gen
import email.utils
import mimetypes
import traceback
import datetime
import utils
import time
import json
import os
import re


class BaseResponse(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(2**4)
    org_app_root = None
    app_root = None
    sql = None
    writer = None
    cookies_domain = None
    cookies_expires_day = None
    extra_headers = None
    test_server = False
    server = None
    api_key = None
    decrypted_params = None
    export_functions = None
    under_maintenance = False
    internal_error = False
    internal_error_header = None
    internal_error_reason = None
    remote_ip = None
    is_local_ip = False
    is_localhost = False
    is_server_local = False
    admin_contact = ""
    grr_secret = ""
    free_var = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.org_app_root = self.app_root
        if self.server is not None:
            self.app_root = os.path.join(self.app_root, self.server)
        self.cookies_macros = {
            "get": self.get_cookie,
            "set": self.set_cookie,
            "get_secure": self.get_secure_cookie,
            "set_secure": self.set_secure_cookie,
        }
        try:
            self.request.path = bytes([ord(c) for c in self.request.path]).decode()
        except (UnicodeDecodeError, ValueError):
            pass
        if self.request.headers["Host"].startswith("test."):
            self.test_server = True
        self.prepare_request_summary()
        self.is_local_ip = re.search(r"192\.168\.", self.remote_ip) is not None
        self.is_localhost = re.search(r"127\.0\.0\.1", self.remote_ip) is not None

    def prepare_request_summary(self):
        try:
            if not tornado.web._has_stream_request_body(self.__class__):
                _body = self.request.body.decode()
            else:
                _body = "not_available_due_to_stream_request_body"
        except:
            _body = ""
            for _ in self.request.body:
                _body += "\\x{:02x}".format(_)
        headers = dict(self.request.headers)
        self.request_summary = {
            "timestamp": int(time.time())
        }
        if "Host" in headers:
            self.request_summary.update({
                "Host": headers["Host"]
            })
            host = headers.pop("Host")
            self.is_server_local = re.search(r"192\.168\.", host) is not None
        if "X-Forwarded-For" in headers:
            proxied_ip = headers["X-Forwarded-For"].split(",")
            x_real_ip = headers["X-Real-Ip"]
            if proxied_ip:
                self.remote_ip = proxied_ip[0].strip() or x_real_ip
            else:
                self.remote_ip = x_real_ip
            headers.pop("X-Real-Ip")
        else:
            self.remote_ip = self.request.remote_ip
        self.request_summary.update({
            "remote_ip": self.remote_ip
        })
        self.request_summary.update({
            "method": self.request.method,
            "uri": self.request.path+("?"+self.request.query if self.request.query else ""),
            "body": _body,
        })
        self.request_summary.update(headers)

    def prepare(self):
        if self._finished:
            return
        if self.internal_error:
            self.set_status(500)
            try:
                content = '''<html>
<head>
    <meta charset="UTF-8">
    <title>500 Internal Server Error </title>
</head>
<body>
    <h2>{}</h2>
    <div><pre>{}</pre></div>
    <div>Please try again later.</div>{}
</body>
</html>
'''
                content = content.format(
                    (self.internal_error_header or ""),
                    self.format_exc(self.internal_error_reason or ""),
                    self.admin_contact,
                ).encode()
            except:
                traceback.print_exc()
                content = "<title>{msg}</title><body>{msg}{admin_contact}</body>".format(
                    msg="500 Internal Server Error",
                    admin_contact=self.admin_contact
                )
            self.write(content)
            self.finish()
            return
        if self.test_server and not self.is_local_ip:
            self.write_error(403)
            return
        if not self.is_localhost:
            try:
                self.prepare_username()
                self.prepare_xsrf()
                self.prepare_session_key()
            except:
                if not self._finished or not self.get_status():
                    self.write_error(500, msg=traceback.format_exc())
                return
            if self.request.headers["Host"] == "127.0.0.1":
                self.write_error(403)
                return
            if self.under_maintenance:
                self.set_status(503)
                content = "<title>503 Service Unavailable</title><body><h2>Server Maintenance</h2><div>Please try again later.</div>{}</body>"
                content = content.format(self.admin_contact)
                self.write(content)
                self.finish()
                return
            for k, v in self.extra_headers.items():
                if self.test_server and k == "Content-Security-Policy":
                    continue
                self.set_header(k, v)

    def set_cookie(self, k, v, expires_day=None, **kwargs) -> None:
        if expires_day is None:
            expires_day = self.cookies_expires_day
        if "expires_days" in kwargs:
            kwargs.pop("expires_days")
        if "domain" in kwargs:
            kwargs.pop("domain")
        super().set_cookie(k, v, domain=self.cookies_domain, expires_days=expires_day, **kwargs)

    def _set_cookie(self, *args, **kwargs) -> None:
        return super().set_cookie(*args, **kwargs)

    def prepare_username(self):
        pass

    def prepare_xsrf(self):
        pass

    def prepare_session_key(self):
        pass

    def decrpyt_params(self, v):
        return v

    def encrpyt_params(self, v):
        return v

    def check_xsrf_cookie(self):
        raise NotImplementedError()

    def _check_xsrf_cookie(self):
        return super().check_xsrf_cookie()

    def dump_request_summary(self, fn):
        self.writer(
            os.path.join(self.app_root, "log", fn+".log"),
            "ab",
            (json.dumps(self.request_summary, ensure_ascii=False)+"\n").encode()
        )

    def check_etag_header(self):
        return False

    def _check_etag_header(self):
        return super().check_etag_header()

    def compute_etag(self):
        return None

    def _compute_etag(self):
        return super().compute_etag()

    def format_exc(self, exc):
        exc = re.sub(r"File.*?site-packages.", "File \"", exc)
        regex = re.compile("File.*?{}.".format(re.escape(self.org_app_root)))
        exc = regex.sub("File \"app_root\\\\", exc)
        return exc

    def write_error(self, status_code, **kwargs):
        self.dump_request_summary("error")
        msg = {
            "status_code": status_code,
            "msg": (http_status[status_code] if status_code in http_status else "unknown error") if "msg" not in kwargs else self.format_exc(kwargs["msg"])
        }
        self.set_header("Content-Type", "text/plain")
        if status_code == 406:
            na_406_html = "<html><title>406 Not Acceptable</title><body><h1>{}</h1><script>setTimeout(function(){{window.location.reload(true)}}, 5000);</script></body></html>"
            self.set_status(200)
            self.set_header("Content-Type", "text/html")
            self.write(na_406_html.format("IP Error\n(Please do not use company network or public wi-fi)\nRefresh to retry."))
        else:
            self.set_status(status_code)
            self.write(json.dumps(msg))
        self.finish()

    def _write_error(self, *args, **kwargs) -> None:
        return super().write_error(*args, **kwargs)


class StaticFileHandler(BaseResponse, tornado.web.StaticFileHandler):
    pass


class ErrorHandler(BaseResponse):
    def check_xsrf_cookie(self):
        return


class NotFound(ErrorHandler):
    def prepare(self):
        self.write_error(404)


class SuccessHandler(BaseResponse):
    rh = []

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     import time
    #     # self.ts = self.request.remote_ip+"/"+str(time.time())+"/"+self.request.path
    #     # SuccessHandler.rh.append(self.ts)
    #     p = threading.Thread(target=self._monitor_count)
    #     p.daemon = True
    #     p.start()

    def on_finish(self) -> None:
        self._monitor_count()

    def on_connection_close(self) -> None:
        self._monitor_count()
        super().on_connection_close()

    def _monitor_count(self):
        # while True:
        #     if self._finished:
        #         # SuccessHandler.rh.remove(self.ts)
        #         break
        #     import time
        #     # time.sleep(1/1000)
        #     time.sleep(1)
        self.dump_request_summary("success")


class BaseFile(SuccessHandler):
    _args = None
    file_name = None
    file_path = None
    file_modified = None

    def get_file_stat(self):
        return os.stat(self.file_path)

    def get_file_modified(self):
        return datetime.datetime.utcfromtimestamp(int(self.get_file_stat().st_mtime))

    def should_return_304(self) -> bool:
        ims_value = self.request.headers.get("If-Modified-Since")
        if ims_value is not None:
            date_tuple = email.utils.parsedate(ims_value)
            if date_tuple is not None:
                if_since = datetime.datetime(*date_tuple[:6])
                if if_since >= self.file_modified:
                    return True
        return False

    def set_modified_header(self):
        self.set_header("Last-Modified", self.file_modified)

    def set_304_header(self):
        self.set_status(304)

    def get_what(self, og_title=None, og_description=None):
        return None

    @tornado.concurrent.run_on_executor
    def _get(self):
        self.set_modified_header()
        if self.should_return_304():
            return self.set_304_header()
        what = self.get_what() or open(self.file_path, "rb").read()
        if "Content-Security-Policy" in self._headers:
            self._headers["Content-Security-Policy"] = self._headers["Content-Security-Policy"].replace(" 'nonce-foxe6'", "")
        return what

    @tornado.gen.coroutine
    def get(self, *args):
        self._args = args
        a = yield self._get()
        if a:
            self.write(a)
            self.finish()


class File(BaseFile):
    def prepare(self) -> None:
        super().prepare()
        self.file_path = os.path.join(self.app_root, self.path_args[0])
        content_type = mimetypes.guess_type(self.file_path)[0]
        self.set_header("Content-Type", content_type or "application/octet-stream")
        self.file_modified = self.get_file_modified()


class HTML(BaseFile):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.file_path = os.path.join(self.app_root, self.file_name+".html")
        self.file_modified = self.get_file_modified()


class AJAX(SuccessHandler):
    api_name = None

    @tornado.concurrent.run_on_executor
    def _run(self, method: str):
        params = self.decrypted_params if self.decrypted_params else utils.parse_params(self.request.arguments.items())
        exec(open(os.path.join(self.app_root, self.api_name + "_api.py"), "rb").read().decode())
        return locals()["api_"+method](
            params=params,
            cookies=self.cookies_macros,
            app_root=self.app_root,
            sql=self.sql,
            writer=self.writer,
            export_functions=self.export_functions,
            x_real_ip=self.remote_ip,
            test_server=self.test_server,
            domain=self.cookies_domain[1:],
            server_name=self.server,
            free_var=self.free_var
        )

    @tornado.gen.coroutine
    def get(self, *args):
        raw_params = yield self._run("get")
        self.write(raw_params)
        self.finish()

    @tornado.gen.coroutine
    def post(self, *args):
        raw_params = yield self._run("post")
        is_exc = isinstance(raw_params, Exception)
        is_traceback = False
        if not is_exc:
            is_traceback = "Traceback (most recent call last):" in raw_params
        if is_exc or is_traceback:
            if is_traceback:
                raw_params = json.loads(raw_params)
            if is_exc:
                raw_params = "{}: {}".format(type(raw_params).__name__, raw_params)
            return self.write_error(400, msg=raw_params)
        raw_params = raw_params.encode()
        if self.decrypted_params:
            self.write(self.encrpyt_params(raw_params))
        else:
            self.set_header("Content-Type", "application/json")
            self.write(raw_params)
        self.finish()


