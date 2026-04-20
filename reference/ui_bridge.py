import http.server
import json
import os
import urllib.parse

class UIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 路由 1: 获取合并后的 mental_map 和当前 settings
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # 合并所有 mental_map 供前端渲染
            combined_map = []
            import glob
            for f in glob.glob("mental_map_*.json"):
                with open(f, 'r', encoding='utf-8') as j:
                    combined_map.append(json.load(j))
            
            with open("settings.json", 'r', encoding='utf-8') as s:
                current_settings = json.load(s)
            
            self.wfile.write(json.dumps({
                "maps": combined_map,
                "settings": current_settings
            }).encode())
        else:
            return super().do_GET()

    def do_POST(self):
        # 路由 2: 修改配置
        if self.path == '/api/update':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            update_req = json.loads(post_data)
            
            with open("settings.json", 'r+', encoding='utf-8') as f:
                data = json.load(f)
                data[update_req['var_id']] = update_req['value']
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
            
            self.send_response(200)
            self.end_headers()

def run_ui():
    port = 8000
    print(f"[Code2Config] UI 控制台已启动: http://localhost:{port}")
    http.server.HTTPServer(('', port), UIHandler).serve_forever()

if __name__ == "__main__":
    run_ui()