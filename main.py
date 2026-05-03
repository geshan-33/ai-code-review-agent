# AI 代码评审 + 自动修复 Agent (演示代码)
import openai

openai.api_key = "your-api-key"

SAMPLE_DIFF = """
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -10,6 +10,8 @@
 def get_user(user_id):
+    password = "admin123"
     query = f"SELECT * FROM users WHERE id = {user_id}"
"""

print("=== AI 代码评审 + 自动修复 Agent 演示 ===\n")
print("1. 评审 Agent 分析 diff...")
issues = [
    {"severity": "critical", "category": "安全", "description": "硬编码数据库密码"},
    {"severity": "major", "category": "安全", "description": "SQL 注入漏洞"},
]
for i, iss in enumerate(issues, 1):
    print(f"问题{i}: [{iss['severity']}] {iss['category']} - {iss['description']}")

print("\n2. 修复 Agent 生成 patch...")
print("--- a/app.py\n+++ b/app.py\n-    password = \"admin123\"\n+    password = os.environ.get('DB_PASS')")
print("\n3. 验证 Agent 验证...\n✅ 验证通过，无新问题引入。")
