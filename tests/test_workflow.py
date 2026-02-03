"""
Lab 03: n8n LINE Gold Price Bot - Auto-grading Tests
ตรวจสอบจากไฟล์ workflow.json โดยไม่ต้องรัน n8n
"""

import pytest
import json
import os

WORKFLOW_FILE = 'workflow.json'


class TestWorkflowFile:
    """ตรวจสอบไฟล์ workflow.json (20 คะแนน)"""

    @pytest.fixture(autouse=True)
    def load_workflow(self):
        if os.path.exists(WORKFLOW_FILE):
            with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
                self.nodes = self.workflow.get('nodes', [])
        else:
            self.workflow = None
            self.nodes = []

    def test_01_workflow_file_exists(self):
        """Test 1: มีไฟล์ workflow.json (10 คะแนน)"""
        assert os.path.exists(WORKFLOW_FILE), \
            "workflow.json not found - กรุณา export workflow จาก n8n"

    def test_02_workflow_valid_json(self):
        """Test 2: เป็น valid JSON (10 คะแนน)"""
        assert self.workflow is not None, "workflow.json is not valid JSON"
        assert 'nodes' in self.workflow, "workflow.json missing 'nodes' key"


class TestWebhookNode:
    """ตรวจสอบ Webhook Node (20 คะแนน)"""

    @pytest.fixture(autouse=True)
    def load_workflow(self):
        if os.path.exists(WORKFLOW_FILE):
            with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
                self.nodes = self.workflow.get('nodes', [])
                self.webhook_node = None
                for node in self.nodes:
                    if 'webhook' in node.get('type', '').lower():
                        self.webhook_node = node
                        break
        else:
            self.workflow = None
            self.nodes = []
            self.webhook_node = None

    def test_03_has_webhook_node(self):
        """Test 3: มี Webhook Node (10 คะแนน)"""
        webhook_nodes = [n for n in self.nodes if 'webhook' in n.get('type', '').lower()]
        assert len(webhook_nodes) > 0, "Workflow ต้องมี Webhook Node เพื่อรับข้อมูลจาก LINE"

    def test_04_webhook_method_post(self):
        """Test 4: Webhook ใช้ POST method (10 คะแนน)"""
        if self.webhook_node is None:
            pytest.skip("No webhook node found")
        params = self.webhook_node.get('parameters', {})
        http_method = params.get('httpMethod', '').upper()
        assert http_method == 'POST', \
            f"Webhook ต้องใช้ POST method สำหรับ LINE, got '{http_method}'"


class TestGoldAPINode:
    """ตรวจสอบ HTTP Request Node สำหรับ Gold API (20 คะแนน)"""

    @pytest.fixture(autouse=True)
    def load_workflow(self):
        if os.path.exists(WORKFLOW_FILE):
            with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
                self.nodes = self.workflow.get('nodes', [])
                self.http_nodes = [n for n in self.nodes if 'httprequest' in n.get('type', '').lower()]
        else:
            self.workflow = None
            self.nodes = []
            self.http_nodes = []

    def test_05_has_gold_api_node(self):
        """Test 5: มี HTTP Request Node สำหรับ Gold API (10 คะแนน)"""
        gold_api_found = False
        for node in self.http_nodes:
            params = node.get('parameters', {})
            url = params.get('url', '').lower()
            if 'gold' in url or 'chnwt' in url:
                gold_api_found = True
                break
        assert gold_api_found, \
            "ต้องมี HTTP Request Node ที่เรียก Thai Gold API"

    def test_06_gold_api_url_correct(self):
        """Test 6: Gold API URL ถูกต้อง (10 คะแนน)"""
        correct_url = 'api.chnwt.dev/thai-gold-api/latest'
        url_found = False
        for node in self.http_nodes:
            params = node.get('parameters', {})
            url = params.get('url', '').lower()
            if correct_url in url:
                url_found = True
                break
        assert url_found, \
            f"Gold API URL ต้องเป็น https://{correct_url}"


class TestCodeNode:
    """ตรวจสอบ Code Node (10 คะแนน)"""

    @pytest.fixture(autouse=True)
    def load_workflow(self):
        if os.path.exists(WORKFLOW_FILE):
            with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
                self.nodes = self.workflow.get('nodes', [])
                self.code_node = None
                self.js_code = ""
                for node in self.nodes:
                    if 'code' in node.get('type', '').lower():
                        self.code_node = node
                        self.js_code = node.get('parameters', {}).get('jsCode', '')
                        break
        else:
            self.workflow = None
            self.nodes = []
            self.code_node = None
            self.js_code = ""

    def test_07_has_code_node(self):
        """Test 7: มี Code Node (10 คะแนน)"""
        code_nodes = [n for n in self.nodes if 'code' in n.get('type', '').lower()]
        assert len(code_nodes) > 0, \
            "ต้องมี Code Node เพื่อจัดรูปแบบข้อความ"


class TestLineReplyNode:
    """ตรวจสอบ HTTP Request Node สำหรับ LINE Reply (20 คะแนน)"""

    @pytest.fixture(autouse=True)
    def load_workflow(self):
        if os.path.exists(WORKFLOW_FILE):
            with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
                self.nodes = self.workflow.get('nodes', [])
                self.http_nodes = [n for n in self.nodes if 'httprequest' in n.get('type', '').lower()]
        else:
            self.workflow = None
            self.nodes = []
            self.http_nodes = []

    def test_08_has_line_reply_node(self):
        """Test 8: มี HTTP Request Node สำหรับ LINE Reply (10 คะแนน)"""
        line_api_found = False
        for node in self.http_nodes:
            params = node.get('parameters', {})
            url = params.get('url', '').lower()
            if 'api.line.me' in url or 'line' in node.get('name', '').lower():
                line_api_found = True
                break
        assert line_api_found, \
            "ต้องมี HTTP Request Node ที่เรียก LINE Reply API"

    def test_09_line_reply_url_correct(self):
        """Test 9: LINE Reply URL ถูกต้อง (10 คะแนน)"""
        correct_url = 'api.line.me/v2/bot/message/reply'
        url_found = False
        for node in self.http_nodes:
            params = node.get('parameters', {})
            url = params.get('url', '').lower()
            if correct_url in url:
                url_found = True
                break
        assert url_found, \
            f"LINE Reply API URL ต้องเป็น https://{correct_url}"


class TestMessageFormatting:
    """ตรวจสอบการจัดรูปแบบข้อความ (10 คะแนน)"""

    @pytest.fixture(autouse=True)
    def load_workflow(self):
        if os.path.exists(WORKFLOW_FILE):
            with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
                self.nodes = self.workflow.get('nodes', [])
                self.js_code = ""
                for node in self.nodes:
                    if 'code' in node.get('type', '').lower():
                        self.js_code = node.get('parameters', {}).get('jsCode', '')
                        break
        else:
            self.workflow = None
            self.nodes = []
            self.js_code = ""

    def test_10_message_has_price_formatting(self):
        """Test 10: มีการจัดรูปแบบข้อความราคาทอง (10 คะแนน)"""
        if not self.js_code:
            pytest.skip("No code node found")
        
        # ตรวจสอบว่ามีการอ้างอิงถึงราคาทอง
        has_price_ref = any([
            'price' in self.js_code.lower(),
            'gold_bar' in self.js_code.lower(),
            'gold' in self.js_code.lower(),
            'buy' in self.js_code.lower(),
            'sell' in self.js_code.lower()
        ])
        
        # ตรวจสอบว่ามีการสร้างข้อความ
        has_message = any([
            'message' in self.js_code.lower(),
            'text' in self.js_code.lower(),
            'replytoken' in self.js_code.lower()
        ])
        
        assert has_price_ref and has_message, \
            "Code Node ต้องมีการจัดรูปแบบข้อความที่แสดงราคาทอง (buy/sell price)"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
