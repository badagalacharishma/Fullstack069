import os
import subprocess
import urllib.parse

# PART 1: Generate missing testcase images into testcases/ folder
base_dir = r"C:\Users\rohit\.gemini\antigravity\scratch\Fullstack069"

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f: f.write(content)

def capture(html_path, out_png):
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    abs_html = os.path.abspath(html_path).replace(chr(92), '/')
    subprocess.run([
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless', '--disable-gpu',
        f'--screenshot={os.path.abspath(out_png)}',
        '--window-size=1280,1024', f'file:///{abs_html}'
    ])

# Generate Test Case Screenshots
t1_src = os.path.join(base_dir, r'01-observation\week-01-html5-and-css3\src\task1.html')
with open(t1_src, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('<body>', '<body style="background: #f0e6ff;">'))
capture('t.html', os.path.join(base_dir, r'01-observation\week-01-html5-and-css3\testcases\tc1.png'))

t2_src = os.path.join(base_dir, r'01-observation\week-01-html5-and-css3\src\task2.html')
with open(t2_src, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('linear-gradient(to right, #d9eaff, #ffffff)', 'linear-gradient(to right, #ffecd9, #ffffff)'))
capture('t.html', os.path.join(base_dir, r'01-observation\week-01-html5-and-css3\testcases\tc2.png'))

t3_src = os.path.join(base_dir, r'01-observation\week-02-javascript-es6-and-dom\src\task3.html')
with open(t3_src, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('value="8.42"', 'value="9.00"').replace('</script>', 'showProfile();</script>'))
capture('t.html', os.path.join(base_dir, r'01-observation\week-02-javascript-es6-and-dom\testcases\tc3.png'))

t4_html = os.path.join(base_dir, r'01-observation\week-02-javascript-es6-and-dom\src\task4\index.html')
script4 = os.path.join(base_dir, r'01-observation\week-02-javascript-es6-and-dom\src\task4\script.js')
style4 = os.path.join(base_dir, r'01-observation\week-02-javascript-es6-and-dom\src\task4\style.css')
with open(t4_html, 'r', encoding='utf-8') as f: h4 = f.read()
with open(script4, 'r', encoding='utf-8') as f: s4 = f.read()
with open(style4, 'r', encoding='utf-8') as f: st4 = f.read()
h4_comb = h4.replace('</head>', f'<style>{st4}</style></head>').replace('</body>', f'<script>{s4}</script></body>')
write_file('t.html', h4_comb.replace('</body>', '<script>document.getElementById("taskInput").value = "Invalid State Check"; addTask();</script></body>'))
capture('t.html', os.path.join(base_dir, r'01-observation\week-02-javascript-es6-and-dom\testcases\tc4.png'))

r1 = os.path.join(base_dir, r'02-record\week-01\src\index.html')
with open(r1, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('<body>', '<body style="background: #fafafa;">'))
capture('t.html', os.path.join(base_dir, r'02-record\week-01\testcases\tc1.png'))

r2 = os.path.join(base_dir, r'02-record\week-02\src\index.html')
with open(r2, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('flex-direction', 'flex-direction-removed'))
capture('t.html', os.path.join(base_dir, r'02-record\week-02\testcases\tc2.png'))

r3 = os.path.join(base_dir, r'02-record\week-03\src\week3rd.html')
with open(r3, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('[85, 92, 78, 64, 95, 88]', '[10, 20, 30]'))
capture('t.html', os.path.join(base_dir, r'02-record\week-03\testcases\tc3.png'))

r4 = os.path.join(base_dir, r'02-record\week-04\src\index.html')
with open(r4, 'r', encoding='utf-8') as f: write_file('t.html', f.read().replace('<h3>AI</h3>', '<h3>Google Cloud</h3>'))
capture('t.html', os.path.join(base_dir, r'02-record\week-04\testcases\tc4.png'))

def capture_term(out_png, text):
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    write_file('t.html', f'<html><body style="background: black; color: white; font-family: Consolas, monospace; padding: 20px;">{text}</body></html>')
    capture('t.html', out_png)

capture_term(os.path.join(base_dir, r'02-record\week-05\testcases\tc_fail.png'), r"C:\Users\charishma\FullStack&gt; node server.js<br>Error: EADDRINUSE :::3000")
capture_term(os.path.join(base_dir, r'02-record\week-06\testcases\tc_fail.png'), r"Cannot GET /invalid")

if os.path.exists('t.html'): os.remove('t.html')
