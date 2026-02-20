from playwright.sync_api import sync_playwright
import time

def run_scroller():
    with sync_playwright() as p:
        # 1. 启动浏览器（headless=False 让你亲眼看它怎么滚）
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 2. 访问一个动态加载示例（这里以一个简单的新闻列表为例）
        print("🚀 正在开启浏览器...")
        page.goto("https://news.ycombinator.com/") # 这里用 Hacker News 演示，它虽简单但很稳

        # 3. 模拟滚动逻辑
        for i in range(1, 4):
            print(f"滚动第 {i} 次...")
            # 使用 JavaScript 指令让页面滚到底部
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # 等待 2 秒，给网络一点“变魔术”加载数据的时间
            time.sleep(2) 

        # 4. 抓取渲染后的数据
        # 此时页面已经加载了更多内容，我们直接获取所有标题
        titles = page.locator(".titleline > a").all_inner_texts()
        
        print(f"✅ 滚动完成！一共抓取了 {len(titles)} 个标题：")
        for idx, title in enumerate(titles[:10], 1):
            print(f"{idx}. {title}")

        browser.close()

if __name__ == "__main__":
    run_scroller()