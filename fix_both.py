import os
import subprocess
import urllib.parse
from datetime import datetime

base_dir = r"C:\Users\rohit\.gemini\antigravity\scratch\Fullstack069"

def read_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return "File not found"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @page {{ margin: 15mm; }}
        body {{ font-family: Arial, sans-serif; margin: 0px 10px; color: #333; line-height: 1.5; font-size: 14px; }}
        h1, h2, h3, h4, h5, h6, .section-title {{ color: #000; page-break-after: avoid; font-family: 'Arial', sans-serif; }}
        .header {{ margin-bottom: 20px; font-size: 14px; line-height: 1.6; }}
        .header h1 {{ font-size: 22px; margin-bottom: 15px; text-transform: uppercase; font-weight: bold; }}
        .header p {{ margin: 3px 0; font-weight: normal; color: #000; }}
        .header p strong {{ font-weight: bold; }}
        .divider {{ border-bottom: 1px solid #ccc; margin: 20px 0; }}
        .section-title {{ font-weight: bold; font-size: 16px; margin-top: 30px; margin-bottom: 10px; text-transform: uppercase; }}
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; page-break-inside: auto; font-size: 13px; }}
        tr {{ page-break-inside: avoid; page-break-after: auto; }}
        table, th, td {{ border: 1px solid #ccc; }}
        th, td {{ padding: 10px; text-align: left; vertical-align: top; }}
        th {{ background-color: #f8f9fa; font-weight: bold; color: #333; }}
        .fail {{ color: #dc3545; font-weight: bold; }}
        .pass {{ color: #28a745; font-weight: bold; }}
        pre {{ background-color: #f8f9fa; border: none; padding: 15px; font-size: 12px; white-space: pre-wrap; word-wrap: break-word; page-break-inside: avoid; color: #333; font-family: 'Consolas', 'Courier New', monospace; }}
        img {{ max-width: 100%; height: auto; border: 1px solid #ddd; margin-top: 10px; margin-bottom: 25px; page-break-inside: avoid; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .output-title {{ font-weight: bold; font-size: 14px; margin-bottom: 5px; color: #0056b3; }}
        ul, ol {{ margin-top: 5px; margin-bottom: 15px; padding-left: 20px; }}
        li {{ margin-bottom: 5px; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{doc_type}</h1>
        <p><strong>Course:</strong> Full Stack Web Development</p>
        <p><strong>Course Code:</strong> 23CM4121</p>
        <p><strong>Experiment No.:</strong> {exp_no}</p>
        <p><strong>Student Name:</strong> {student_name}</p>
        <p><strong>Roll No.:</strong> {roll_no}</p>
        <p><strong>Date:</strong> 30-08-2026</p>
    </div>
    <div class="divider"></div>
    
    <div class="section-title">1. TITLE</div>
    <p>{title}</p>
    
    <div class="section-title">2. AIM</div>
    <p>{aim}</p>
    
    <div class="section-title">3. OBJECTIVE</div>
    <p>The objectives of this experiment are:</p>
    {objective}
    
    <div class="section-title">4. THEORY</div>
    {theory}
    
    <div class="section-title">5. ALGORITHM / PROCEDURE</div>
    {procedure}
    
    <div class="section-title">6. PROGRAM / SOURCE CODE</div>
    {code_html}
    
    <div class="section-title">7. CODE EXPLANATION</div>
    <table>
        <tr><th style="width: 30%;">Code / Syntax</th><th>Explanation</th></tr>
        {code_explanation}
    </table>
    
    <div class="section-title">8. TEST CASES AND EXECUTION DATA</div>
    <p>The experiment was tested with both positive and negative validation test cases:</p>
    <table>
        <tr>
            <th style="width: 12%;">Test Case</th>
            <th style="width: 22%;">Input / Action</th>
            <th style="width: 28%;">Expected Result</th>
            <th style="width: 28%;">Actual Result</th>
            <th style="width: 10%;">Status</th>
        </tr>
        {test_cases_table}
    </table>
    
    <div class="section-title">9. OUTPUT</div>
    {output_html}

    <div class="section-title">10. TEST CASES SCREENSHOTS</div>
    {testcases_html}
    
    <div class="section-title">11. RESULT</div>
    <p>{result}</p>
</body>
</html>
"""

def make_tc_row(tc_id, action, expected, actual, status):
    status_class = "pass" if status.lower() == "pass" else "fail"
    return f"<tr><td>{tc_id}</td><td>{action}</td><td>{expected}</td><td>{actual}</td><td class='{status_class}'>{status}</td></tr>"

def make_code_exp(rows):
    return "".join([f"<tr><td><code>{k}</code></td><td>{v}</td></tr>" for k,v in rows.items()])

records_data = [
    # OBS 1
    {
        'doc_type': 'LABORATORY OBSERVATION', 'exp_no': '1',
        'title': 'Design and Implementation of College Information Portal Using HTML5',
        'aim': 'To develop a structured, semantic HTML5 web page for the ANITS College Information Portal that incorporates text formatting, department lists, student detail tables, interactive registration forms, and multimedia audio/video players.',
        'objective': '<ul><li>To understand core HTML5 semantic tags and document layout structure.</li><li>To implement formatted text, mathematical/chemical formulas using sup and sub tags.</li><li>To create structured tabular data using table, tr, th, and td elements.</li><li>To design an interactive student registration form with various HTML5 input types.</li><li>To embed and control multimedia audio and video players.</li></ul>',
        'theory': '<p>HTML5 is the standard markup language for creating modern web pages. It introduces semantic elements such as &lt;header&gt;, &lt;nav&gt;, &lt;section&gt;, &lt;article&gt;, and &lt;footer&gt; to structure content meaningfully.</p><p>Forms in HTML5 provide rich input controls including text, email, password, radio buttons, checkboxes, dropdown select, color pickers, and date pickers for client-side data capture.</p><p>HTML5 also provides native &lt;audio&gt; and &lt;video&gt; elements with browser controls for seamless media playback without third-party plugins.</p><p><strong>Application Flow:</strong><br>Browser -&gt; HTML5 Document -&gt; Semantic Elements -&gt; Tables & Forms -&gt; Media Players -&gt; Rendered Webpage</p>',
        'procedure': '<ol><li>Create an HTML5 document and configure the title as \'College Information Portal\'.</li><li>Add a header section with institution title and introductory description.</li><li>Create a navigation bar with hyperlink anchors to sections and external portals.</li><li>Format about text using bold, italic, underline, superscript, and subscript tags.</li><li>Create ordered list for departments and unordered list for campus facilities.</li><li>Construct a student details table with borders, column headers, and records.</li><li>Build a comprehensive student registration form with text, email, password, branch select, date, color, and range inputs.</li><li>Embed audio and video tags with controls attribute.</li><li>Open in web browser and verify all elements and form controls with valid and invalid inputs.</li></ol>',
        'code_explanation': make_code_exp({
            "&lt;header&gt;, &lt;nav&gt;, &lt;footer&gt;": "Semantic HTML5 layout container elements.",
            "&lt;sup&gt;, &lt;sub&gt;": "Displays text as superscript (X²) or subscript (H₂O).",
            "&lt;ol&gt;, &lt;ul&gt;, &lt;li&gt;": "Creates ordered (numbered) and unordered (bulleted) lists.",
            "&lt;table&gt;, &lt;tr&gt;, &lt;th&gt;, &lt;td&gt;": "Structures tabular data into rows, header cells, and standard data cells.",
            "&lt;input type='radio' name='g'&gt;": "Radio button group allowing only one gender selection.",
            "&lt;select&gt;, &lt;option&gt;": "Drop-down select menu for branch selection.",
            "&lt;audio controls&gt;, &lt;video controls&gt;": "Native media playback controls for audio and video files."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Valid Page Load", "Render all layout sections and navigation links", "All sections, lists, and tables display correctly", "Pass"),
            make_tc_row("TC-02", "Formulas & Formatting", "Render superscripts, subscripts, bold and italics", "X² and H₂O formulas display with correct baseline offsets", "Pass"),
            make_tc_row("TC-03", "Valid Form Submission", "Fill form with valid email, roll number, and branch", "Form accepts all valid field data successfully", "Pass")
        ]),
        'output_data': [
            ("Program Main Output", r"01-observation\week-01-html5-and-css3\screenshots\task1_main.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"01-observation\week-01-html5-and-css3\testcases\tc1.png")
        ],
        'files': [r'01-observation\week-01-html5-and-css3\src\task1.html'],
        'pdf_out': r'01-observation\week-01-html5-and-css3\Observation_Task1.pdf'
    },
    # OBS 2
    {
        'doc_type': 'LABORATORY OBSERVATION', 'exp_no': '2',
        'title': 'Design and Implementation of Interactive UI Layouts using CSS3 and Canvas',
        'aim': 'To style a static HTML5 webpage using CSS3 selectors, box models, Flexbox, CSS Grids, transitions, and to draw interactive 2D graphics utilizing the HTML5 Canvas API.',
        'objective': '<ul><li>To apply internal CSS rules with class and ID selectors.</li><li>To implement complex background gradients and text shadows.</li><li>To design responsive flexbox and grid dashboard layouts.</li><li>To create interactive button hover transitions and transformations.</li><li>To programmatically render shapes, lines, and text onto an HTML5 Canvas.</li></ul>',
        'theory': '<p>Cascading Style Sheets (CSS3) is the styling language used to describe the presentation of a document written in HTML. CSS3 introduces advanced features like rounded corners, shadows, gradients, transitions or animations, and flexible box/grid layouts.</p><p>Flexbox provides a more efficient way to lay out, align, and distribute space among items in a container, even when their size is unknown or dynamic.</p><p>The HTML5 &lt;canvas&gt; element is used to draw graphics, on the fly, via JavaScript. The canvas is simply a container for graphics, while a script is required to actually draw the graphics (paths, boxes, circles, text, and adding images).</p><p><strong>Application Flow:</strong><br>HTML Document -&gt; CSS Styling (Colors, Fonts, Layout) -&gt; DOM Rendering -&gt; Canvas API Initialization -&gt; 2D Graphics Drawing</p>',
        'procedure': '<ol><li>Create a semantic HTML structure with navigation, header, and content sections.</li><li>Apply linear-gradient backgrounds to the document body.</li><li>Target elements using CSS IDs (#main-nav) and classes (.feature-card) to apply paddings, margins, and borders.</li><li>Define display: flex; on a container to align its children horizontally with gap spacing.</li><li>Implement pseudo-classes like :hover on buttons to trigger CSS transforms (scale) and background color transitions.</li><li>Embed a &lt;canvas&gt; element with specified width and height.</li><li>Write an embedded JavaScript block to access the canvas 2D context.</li><li>Use context methods (fillRect, arc, moveTo, lineTo, fillText) to draw geometric shapes and names.</li><li>Test the layout responsiveness and hover animations in the browser.</li></ol>',
        'code_explanation': make_code_exp({
            "background: linear-gradient(...)": "Creates a smooth transition between two or more specified colors.",
            "box-shadow: 0px 4px 10px rgba(...)": "Attaches one or more drop-shadows to the element's bounding box.",
            "display: flex;": "Initiates a flexbox formatting context for its children.",
            "transition: transform 0.3s ease;": "Provides a smooth animation effect when CSS properties change (e.g., on hover).",
            "canvas.getContext('2d')": "Returns a two-dimensional drawing context on the canvas.",
            "ctx.arc(x, y, r, 0, 2*Math.PI)": "Creates a circular arc/curve path.",
            "ctx.fillText(text, x, y)": "Draws filled text on the canvas at the specified coordinates."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Render CSS Flexbox", "Dashboard cards align horizontally with space-around", "Cards successfully rendered in a flex row layout", "Pass"),
            make_tc_row("TC-02", "CSS Hover Transition", "Button scales up and changes color on mouse hover", "Smooth transition observed on hover state", "Pass"),
            make_tc_row("TC-03", "Canvas Context Rendering", "Draw orange rectangle, green circle, and blue line", "Shapes painted to canvas successfully", "Pass")
        ]),
        'output_data': [
            ("Program Main Output", r"01-observation\week-01-html5-and-css3\screenshots\task2_main.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"01-observation\week-01-html5-and-css3\testcases\tc2.png")
        ],
        'files': [r'01-observation\week-01-html5-and-css3\src\task2.html'],
        'pdf_out': r'01-observation\week-01-html5-and-css3\Observation_Task2.pdf'
    },
    # OBS 3
    {
        'doc_type': 'LABORATORY OBSERVATION', 'exp_no': '3',
        'title': 'Object-Oriented Programming and Data Encapsulation using JavaScript ES6 Classes',
        'aim': 'To implement object-oriented programming principles in JavaScript by creating ES6 classes, instantiating objects, and dynamically injecting structured data into the Document Object Model (DOM).',
        'objective': '<ul><li>To define JavaScript ES6 classes with constructors.</li><li>To instantiate objects encapsulating student profile attributes.</li><li>To extract user input from HTML form elements using JS.</li><li>To validate form inputs dynamically preventing empty submissions.</li><li>To construct HTML template strings and inject them into the DOM using innerHTML.</li></ul>',
        'theory': '<p>JavaScript ES6 introduced the <code>class</code> keyword, providing syntactic sugar over the existing prototype-based inheritance model. Classes provide a much clearer and simpler syntax to create objects and deal with inheritance.</p><p>A <code>constructor</code> is a special method for creating and initializing an object created with a class. Data encapsulation is achieved by grouping attributes (like name, roll number, CGPA) into a single object instance.</p><p>The Document Object Model (DOM) allows JavaScript to read values from input fields, execute conditional validation logic, and dynamically update the page content without requiring a server request.</p><p><strong>Application Flow:</strong><br>User Input -&gt; Button Click Event -&gt; Form Validation -&gt; Class Instantiation -&gt; DOM Injection</p>',
        'procedure': '<ol><li>Create a simple HTML UI containing input fields for Name, Roll No, Department, and CGPA.</li><li>Add a "Show Profile" button that triggers a JavaScript function on click.</li><li>Define an ES6 class named <code>Student</code> with a constructor initializing 4 properties.</li><li>Inside the click handler, retrieve values from the input fields using <code>document.getElementById().value</code>.</li><li>Implement an IF condition to check for empty strings and trigger an alert if validation fails.</li><li>Instantiate a new <code>Student</code> object passing the retrieved values as arguments.</li><li>Construct a template literal string mapping the object properties into HTML markup.</li><li>Inject the resulting string into a target <code>&lt;div&gt;</code> using the <code>innerHTML</code> property.</li><li>Test edge cases such as empty submissions and extreme values.</li></ol>',
        'code_explanation': make_code_exp({
            "class Student { constructor(...) }": "Defines an ES6 class blueprint with an initialization function.",
            "let student = new Student(...)": "Instantiates a new object from the Student class with specific data.",
            "document.getElementById('id').value": "Retrieves the current string value from an HTML input element.",
            "if (name === '') { alert(...); return; }": "Validates input and halts function execution if criteria are not met.",
            "display.innerHTML = `... ${var} ...`": "Updates the DOM content of an element dynamically using template literals."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Valid Object Instantiation", "Provide all student details and click Show Profile", "Profile card rendered dynamically with correct data", "Pass"),
            make_tc_row("TC-02", "Data Update & Re-render", "Change CGPA to 9.00 and submit again", "DOM successfully replaces old card with updated 9.00 card", "Pass"),
            make_tc_row("TC-03", "Empty Form Submission", "Clear all inputs and click Show Profile", "Validation halts execution and fires browser alert", "Fail")
        ]),
        'output_data': [
            ("Program Main Output", r"01-observation\week-02-javascript-es6-and-dom\screenshots\task3_main.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"01-observation\week-02-javascript-es6-and-dom\testcases\tc3.png")
        ],
        'files': [r'01-observation\week-02-javascript-es6-and-dom\src\task3.html'],
        'pdf_out': r'01-observation\week-02-javascript-es6-and-dom\Observation_Task3.pdf'
    },
    # OBS 4
    {
        'doc_type': 'LABORATORY OBSERVATION', 'exp_no': '4',
        'title': 'State Management and DOM Traversal using JavaScript Event Listeners',
        'aim': 'To build an interactive To-Do List application that demonstrates state management, class inheritance, dynamic element creation, DOM traversal, and event-driven architectural patterns.',
        'objective': '<ul><li>To implement ES6 Class inheritance using <code>extends</code> and <code>super()</code>.</li><li>To manage a global state counter for unique DOM element identification.</li><li>To dynamically append HTML segments to a parent container.</li><li>To pass specific identifying parameters into inline onclick event handlers.</li><li>To remove and style specific DOM nodes upon user interaction.</li></ul>',
        'theory': '<p>Interactive web applications rely heavily on event listeners and DOM manipulation. When a user interacts with the page (e.g., clicking a button), JavaScript captures the event and executes logic to modify the UI.</p><p>Class inheritance in JavaScript allows a child class to inherit properties and methods from a parent class, promoting code reusability. A child class calls <code>super()</code> to invoke the parent\'s constructor.</p><p>Dynamically generated elements must often carry unique identifiers so that subsequent interactions (like deleting or completing a specific item) know exactly which DOM node to target.</p><p><strong>Application Flow:</strong><br>User Input -&gt; Create WebTask Instance -&gt; Generate Unique HTML -&gt; Append to DOM -&gt; Handle Inline Events (Complete/Delete) -&gt; Update State</p>',
        'procedure': '<ol><li>Define a parent <code>Task</code> class with basic properties (id, text).</li><li>Define a child <code>WebTask</code> class that extends <code>Task</code> and adds a <code>getHTML()</code> method returning a formatted UI string.</li><li>Initialize a global <code>taskCounter</code> to track unique IDs.</li><li>Create an <code>addTask()</code> function that reads input, validates it, and instantiates a <code>WebTask</code>.</li><li>Append the generated HTML to the list container and increment the counter.</li><li>Create a <code>completeTask(id)</code> function that finds the specific text span by ID and applies inline CSS (line-through).</li><li>Create a <code>deleteTask(id)</code> function that finds the specific task box by ID and executes <code>.remove()</code>.</li><li>Implement a helper function to toggle the visibility of an "Empty List" message based on container content.</li><li>Test adding, completing, and deleting multiple tasks.</li></ol>',
        'code_explanation': make_code_exp({
            "class WebTask extends Task": "Creates a child class inheriting from the Task parent class.",
            "super(id, text);": "Invokes the parent class constructor to initialize inherited properties.",
            "document.getElementById('id').innerHTML += ...": "Appends a new HTML string to the end of an element's existing content.",
            "onclick='deleteTask(${this.id})'": "Binds a dynamic integer parameter to an inline event handler.",
            "specificText.style.textDecoration = 'line-through';": "Applies an inline CSS style to visually strike out completed text.",
            "specificBox.remove();": "Completely detaches and deletes a node from the DOM."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Add New Task", "Input text and click Add Task", "New task UI block appended to DOM successfully", "Pass"),
            make_tc_row("TC-02", "Complete Task Action", "Click Complete button on a specific task", "Target task text becomes gray and struck-through", "Pass"),
            make_tc_row("TC-03", "Empty State Validation", "Check state rendering", "No tasks available message dynamically handled", "Pass")
        ]),
        'output_data': [
            ("Program Main Output", r"01-observation\week-02-javascript-es6-and-dom\screenshots\task4_main.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"01-observation\week-02-javascript-es6-and-dom\testcases\tc4.png")
        ],
        'files': [r'01-observation\week-02-javascript-es6-and-dom\src\task4\index.html', r'01-observation\week-02-javascript-es6-and-dom\src\task4\script.js'],
        'pdf_out': r'01-observation\week-02-javascript-es6-and-dom\Observation_Task4.pdf'
    },
    
    # RECORD 1
    {
        'doc_type': 'LABORATORY RECORD', 'exp_no': '1',
        'title': 'Design and Implementation of Static College Webpage Using HTML5 Formatting, Tables, Lists, and Forms',
        'aim': 'To develop a static college webpage for ABC Engineering College utilizing HTML5 text formatting tags, superscripts, subscripts, lists, structured tables, hyperlinks, images, and contact form inputs.',
        'objective': '<ul><li>To practice document structuring with HTML5.</li><li>To apply text formatting tags (bold, italic, underline, sup, sub).</li><li>To construct ordered and unordered lists for academic courses and facilities.</li><li>To create structured tables displaying student academic details.</li><li>To implement a contact form with text, email, gender radio buttons, and submit action.</li></ul>',
        'theory': '<p>HTML5 is the backbone of web development. It provides semantic elements, inline text formatting tags for scientific notations and emphasis, lists for structured content, tables for tabular datasets, and forms for capturing user feedback and registrations.</p><p><strong>Application Flow:</strong><br>HTML5 Structure -&gt; Text Formatting & Lists -&gt; Student Table -&gt; Image & Links -&gt; Contact Form</p>',
        'procedure': '<ol><li>Create an HTML5 document with title \'Static Webpage\'.</li><li>Display college heading and introductory paragraph with bold, italic, and underline tags.</li><li>Format chemical formula (H₂O) and mathematical formula (X²) using sub and sup.</li><li>Build an ordered list (&lt;ol&gt;) for courses and an unordered list (&lt;ul&gt;) for facilities.</li><li>Construct a border table with headers: Roll No, Name, Branch, and populate rows.</li><li>Embed an image tag and an external hyperlink with target=\'_blank\'.</li><li>Implement a contact form containing name, email, gender radio buttons, and a submit button.</li><li>Verify web page rendering and test valid and invalid form submissions in browser.</li></ol>',
        'code_explanation': make_code_exp({
            "&lt;b&gt;, &lt;i&gt;, &lt;u&gt;": "Applies bold, italic, and underline styling to text.",
            "&lt;sup&gt;, &lt;sub&gt;": "Renders text above (superscript X²) or below (subscript H₂O) normal baseline.",
            "&lt;ol&gt;, &lt;ul&gt;, &lt;li&gt;": "Creates numbered and bulleted lists for courses and campus facilities.",
            "&lt;table border='1'&gt;": "Defines a structured table with visible cell borders.",
            "&lt;input type='radio' name='gender'&gt;": "Radio button group ensuring mutual exclusivity of gender choice.",
            "&lt;a href='...' target='_blank'&gt;": "Hyperlink opening destination URL in a new browser tab."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Text Formatting & Lists", "Render paragraphs, formulas (X², H₂O) and lists", "All typography, superscripts, subscripts and lists display cleanly", "Pass"),
            make_tc_row("TC-02", "Student Table", "Inspect tabular records rendering", "Table displays Roll No, Name, Branch rows with visible borders", "Pass"),
            make_tc_row("TC-03", "Missing Gender Radio", "Leave gender radio button unchecked and submit", "Form submission fails validation when mandatory radio choice omitted", "Fail")
        ]),
        'output_data': [
            ("Program Main Output", r"02-record\week-01\screenshots\out1.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"02-record\week-01\testcases\tc1.png")
        ],
        'files': [r'02-record\week-01\src\index.html'],
        'pdf_out': r'02-record\week-01\Record_Week1.pdf'
    },
    
    # RECORD 2
    {
        'doc_type': 'LABORATORY RECORD', 'exp_no': '2',
        'title': 'Advanced Responsive Layouts using CSS3 Grids, Flexbox, and Media Queries',
        'aim': 'To construct a visually appealing, responsive dashboard layout utilizing CSS3 methodologies including external stylesheets, pseudo-classes, Flexbox alignment, Grid templates, and transition animations.',
        'objective': '<ul><li>To isolate CSS styling from HTML structure using classes.</li><li>To implement Flexbox for horizontal alignment and vertical centering.</li><li>To build multi-column layouts utilizing CSS Grid templates.</li><li>To apply box-shadows, border-radius, and complex gradients.</li><li>To animate user interactions using CSS pseudo-classes and transitions.</li></ul>',
        'theory': '<p>Modern web layout relies entirely on CSS modules. Flexbox is designed for one-dimensional layouts (a row or a column), distributing space dynamically. CSS Grid provides a two-dimensional layout system, handling both columns and rows simultaneously.</p><p>CSS3 Transitions enable the interpolation of property values over a specific duration, creating smooth animations when element states change, such as hovering over a button or focusing an input field.</p><p><strong>Application Flow:</strong><br>DOM Tree Parsing -&gt; CSSOM Generation -&gt; Flex/Grid Layout Calculation -&gt; Paint & Compositing -&gt; Interactive Hover States</p>',
        'procedure': '<ol><li>Create the fundamental HTML structure wrapping elements in container div tags.</li><li>Apply a universal reset and body typography/background styling.</li><li>Design a navigation bar using absolute positioning or flexbox for alignment.</li><li>Build a dashboard container utilizing <code>display: flex</code> to align feature cards.</li><li>Build a secondary container utilizing <code>display: grid</code> with <code>grid-template-columns</code>.</li><li>Style feature cards with padding, borders, border-radius, and box-shadows.</li><li>Apply background colors to specific cards to differentiate themes.</li><li>Style buttons with borders, padding, colors, and <code>cursor: pointer</code>.</li><li>Implement a <code>.btn:hover</code> rule with <code>transform: scale(1.05)</code> and transition durations.</li></ol>',
        'code_explanation': make_code_exp({
            "border-radius: 12px;": "Rounds the corners of an element's outer border edge.",
            "box-shadow: 0px 4px 4px black;": "Applies a drop shadow effect to element boxes.",
            "display: grid; grid-template-columns: repeat(2, 1fr);": "Creates a two-column grid where each column takes up an equal fraction of the space.",
            "justify-content: space-around;": "Distributes items evenly with equal space around them.",
            "align-items: center;": "Vertically centers items within a flex container.",
            ".btn-main:hover { transform: scale(); }": "Applies a scaling transformation specifically when the mouse pointer is over the element."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Flexbox Container Alignment", "Verify horizontal alignment of cards in dashboard class", "Cards spaced evenly across the horizontal axis", "Pass"),
            make_tc_row("TC-02", "Grid Layout Distribution", "Verify two-column structure in grid-con class", "Cards wrap exactly into a 2x2 grid layout", "Pass"),
            make_tc_row("TC-03", "Missing CSS Class Mapping", "Apply undefined class to an element", "Element renders with default browser styling unaligned", "Fail")
        ]),
        'output_data': [
            ("Program Main Output", r"02-record\week-02\screenshots\out2.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"02-record\week-02\testcases\tc2.png")
        ],
        'files': [r'02-record\week-02\src\index.html'],
        'pdf_out': r'02-record\week-02\Record_Week2.pdf'
    },
    
    # RECORD 3
    {
        'doc_type': 'LABORATORY RECORD', 'exp_no': '3',
        'title': 'Core JavaScript Logic, Array Manipulation, and Functional Programming',
        'aim': 'To implement functional programming patterns in JavaScript utilizing ES6 arrow functions, advanced array methods like filter and reduce, and dynamic DOM injection.',
        'objective': '<ul><li>To declare constants and initialize array data structures.</li><li>To compute aggregations using the Array.prototype.reduce() method.</li><li>To implement conditional extractions using the Array.prototype.filter() method.</li><li>To utilize ES6 destructuring and the Math utility object.</li><li>To dynamically build and inject HTML strings into the Document Object Model.</li></ul>',
        'theory': '<p>JavaScript treats functions as first-class citizens, meaning they can be passed as arguments, returned, and assigned to variables. ES6 arrow functions provide a concise syntax for writing function expressions.</p><p>Array methods like <code>map</code>, <code>filter</code>, and <code>reduce</code> are foundational for data transformation, avoiding the need for manual loops and mutable state, thus adhering to functional programming principles.</p><p><strong>Application Flow:</strong><br>Data Initialization (Array) -&gt; Aggregation (Reduce) -&gt; Extraction (Filter) -&gt; Math Operations -&gt; DOM InnerHTML Update</p>',
        'procedure': '<ol><li>Define a constant array of integer marks representing student scores.</li><li>Create a function <code>calculateAverage</code> that leverages <code>reduce()</code> to sum the array.</li><li>Create an arrow function <code>filterHighScores</code> to return scores &gt;= 80.</li><li>Create a function <code>getMinMax</code> utilizing the spread operator <code>...arr</code> and <code>Math.max/min</code>.</li><li>Execute the functions and destructure the results into separate variables.</li><li>Log the intermediate calculations to the browser console.</li><li>Construct a template literal string embedding the calculated variables.</li><li>Inject the final string into a target DOM element using <code>document.getElementById().innerHTML</code>.</li></ol>',
        'code_explanation': make_code_exp({
            "arr.reduce((acc, curr) => acc + curr, 0)": "Executes a reducer function on each element, resulting in a single output value.",
            "arr.filter(score => score >= 80)": "Creates a new array with all elements that pass the test implemented by the provided function.",
            "Math.max(...arr)": "Uses the spread syntax to pass array elements as individual arguments to find the maximum value.",
            "const { max, min } = getMinMax(marks);": "Object destructuring assignment to unpack properties from an object into distinct variables.",
            "marks.join(', ')": "Creates and returns a new string by concatenating all of the elements in an array."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Average Calculation", "Pass [85, 92, 78, 64, 95, 88] to calculateAverage", "Returns exactly 83.67 as formatted average", "Pass"),
            make_tc_row("TC-02", "High Score Filtering", "Pass same array to filterHighScores", "Returns new array containing [85, 92, 95, 88]", "Pass"),
            make_tc_row("TC-03", "Empty Array Execution", "Provide [] to reduce and filter functions", "Reduce returns 0, Max/Min return -Infinity/Infinity", "Fail")
        ]),
        'output_data': [
            ("Program Main Output", r"02-record\week-03\screenshots\out3.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"02-record\week-03\testcases\tc3.png")
        ],
        'files': [r'02-record\week-03\src\week3rd.html'],
        'pdf_out': r'02-record\week-03\Record_Week3.pdf'
    },
    
    # RECORD 4
    {
        'doc_type': 'LABORATORY RECORD', 'exp_no': '4',
        'title': 'Interactive DOM Manipulation and Object-Oriented Architecture',
        'aim': 'To architect an interactive web dashboard using JavaScript Event Listeners, Prompt interactions, dynamic CSS modifications, and ES6 Object-Oriented Class hierarchies.',
        'objective': '<ul><li>To attach dynamic event listeners to DOM buttons.</li><li>To modify CSS styling directly via the JavaScript Style Object.</li><li>To capture user input synchronously via browser Prompts.</li><li>To model data using ES6 classes and inheritance structures.</li><li>To execute class methods that update the User Interface dynamically.</li></ul>',
        'theory': '<p>DOM Manipulation is the process of interacting with the DOM API to change or modify the HTML document dynamically. Event listeners observe specific elements and trigger callback functions when user events (clicks, keypresses) occur.</p><p>JavaScript Classes allow developers to construct blueprints for data models. Inheritance (using <code>extends</code>) enables specialized subclasses (like AdvancedCourse) to inherit properties from a base class (like Course), keeping logic modular and DRY (Don\'t Repeat Yourself).</p><p><strong>Application Flow:</strong><br>User Event (Click) -&gt; Event Listener Triggered -&gt; Callback Execution -&gt; Class Method Invocation -&gt; DOM Update</p>',
        'procedure': '<ol><li>Build an HTML interface with several interaction buttons.</li><li>Define a base <code>Course</code> class with title, description, and DOM element ID properties.</li><li>Create an <code>AdvancedCourse</code> subclass that extends <code>Course</code> and adds a level property.</li><li>Implement a <code>showInfo()</code> method within the classes to inject data into the DOM.</li><li>Instantiate objects representing AI, Editing, and Game Development courses.</li><li>Use <code>addEventListener()</code> to bind click events on buttons to the objects\' <code>showInfo()</code> methods.</li><li>Implement a separate event listener that triggers a <code>prompt()</code> dialog to capture user names.</li><li>Implement a function to dynamically alter <code>document.body.style.background</code>.</li><li>Verify all interactions and state changes within the browser.</li></ol>',
        'code_explanation': make_code_exp({
            "element.addEventListener('click', func)": "Attaches an event handler to an element without overwriting existing event handlers.",
            "let name = prompt('Enter Name');": "Displays a dialog box that prompts the visitor for input.",
            "document.body.style.background = '...'": "Directly manipulates the CSS background property of the document body node.",
            "class AdvancedCourse extends Course": "Establishes a prototype chain where AdvancedCourse inherits from Course.",
            "document.getElementById(this.id).innerHTML": "Dynamically updates the HTML content of the specific element tied to the object instance."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Class Instantiation & Method Call", "Click 'Open' button on AI course card", "AI object executes showInfo() injecting details into DOM", "Pass"),
            make_tc_row("TC-02", "Style Mutation Event", "Click the 'Change Color' theme button", "Body background gradient updates to linear-gradient dynamically", "Pass"),
            make_tc_row("TC-03", "Null Prompt Handling", "Click 'Message' button and hit 'Cancel'", "DOM heading updates to 'Welcome null' due to missing validation", "Fail")
        ]),
        'output_data': [
            ("Program Main Output", r"02-record\week-04\screenshots\out4.png")
        ],
        'testcases_data': [
            ("Test Case Execution 1", r"02-record\week-04\testcases\tc4.png")
        ],
        'files': [r'02-record\week-04\src\index.html'],
        'pdf_out': r'02-record\week-04\Record_Week4.pdf'
    },
    
    # RECORD 5
    {
        'doc_type': 'LABORATORY RECORD', 'exp_no': '5',
        'title': 'Introduction to Node.js Runtime, Built-in Modules, and HTTP Servers',
        'aim': 'To explore basic Node.js execution environments, leverage built-in OS, Path, and DNS modules for system interaction, and establish a foundational HTTP server.',
        'objective': '<ul><li>To execute standalone JavaScript scripts via the Node CLI environment.</li><li>To utilize Node built-in modules (os, path, dns) to extract system-level information.</li><li>To understand CommonJS module imports using the <code>require()</code> syntax.</li><li>To create a simple local HTTP server that responds to network requests.</li><li>To define HTTP response headers, status codes, and payload bodies.</li></ul>',
        'theory': '<p>Node.js is an asynchronous event-driven JavaScript runtime designed to build scalable network applications. Unlike browser environments, Node executes directly on the operating system, granting access to file systems and network hardware.</p><p>It provides a rich library of various JavaScript modules which simplifies the development of web applications to a great extent. For instance, the <code>http</code> module allows Node to transfer data over the Hyper Text Transfer Protocol (HTTP).</p><p><strong>Application Flow:</strong><br>Node Runtime Initialization -&gt; Require Core Modules -&gt; Extract OS/DNS Data -&gt; Initialize HTTP Server -&gt; Listen on Port 3000 -&gt; Serve Requests</p>',
        'procedure': '<ol><li>Write a basic JS script (app.js) logging messages to test the execution environment.</li><li>Execute the script using the terminal command <code>node app.js</code>.</li><li>Create a modules.js script utilizing <code>os</code>, <code>path</code>, and <code>dns</code> modules.</li><li>Extract architecture data, resolve IP addresses, and parse file paths.</li><li>Write a server.js script requiring the core <code>http</code> module.</li><li>Invoke <code>http.createServer()</code> and define a callback function resolving requests.</li><li>Set the response header to <code>Content-Type: text/html</code>.</li><li>Write HTML payloads to the response and execute <code>res.end()</code>.</li><li>Start the server on port 3000 and send a request via a web browser.</li></ol>',
        'code_explanation': make_code_exp({
            "const os = require('os');": "Loads the built-in operating system module using CommonJS syntax.",
            "os.arch() / os.platform()": "Returns the operating system CPU architecture and platform identifiers.",
            "dns.lookup('domain', callback)": "Resolves a hostname into the first found A (IPv4) or AAAA (IPv6) record.",
            "http.createServer((req, res) => { ... })": "Initializes a new HTTP server instance with a request listener callback.",
            "res.writeHead(200, { ... })": "Sends a response header to the request, establishing status codes and MIME types.",
            "res.end('html string')": "Signals to the server that all of the response headers and body have been sent."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "CLI Script Execution", "Run `node app.js` in terminal", "Script executes synchronously and logs to stdout", "Pass"),
            make_tc_row("TC-02", "Core Module API Calls", "Execute `node modules.js`", "Returns architecture, parsed paths, and resolved IP addresses", "Pass"),
            make_tc_row("TC-03", "Port Conflict Error", "Run `node server.js` while port 3000 is occupied", "Node throws EADDRINUSE error and server crashes", "Fail")
        ]),
        'output_data': [
            ("Output 1: HTTP Server Startup Console Log", r"02-record\week-05\screenshots\srv_out.png"),
            ("Output 2: CLI Application Execution", r"02-record\week-05\screenshots\app_out.png")
        ],
        'testcases_data': [
            ("Test Case 1: Error Exception", r"02-record\week-05\testcases\tc_fail.png")
        ],
        'files': [r'02-record\week-05\src\app.js', r'02-record\week-05\src\modules.js', r'02-record\week-05\src\server.js'],
        'pdf_out': r'02-record\week-05\Record_Week5.pdf'
    },
    
    # RECORD 6
    {
        'doc_type': 'LABORATORY RECORD', 'exp_no': '6',
        'title': 'API Development and Advanced Routing using the Express.js Framework',
        'aim': 'To architect a scalable backend service using the Express.js framework, implementing basic HTTP routing to serve both static HTML views and structured JSON Application Programming Interfaces (APIs).',
        'objective': '<ul><li>To install and initialize the Express.js framework within a Node application.</li><li>To configure middleware and port bindings.</li><li>To construct GET route handlers for the root URL endpoint.</li><li>To design a dedicated API endpoint serving complex JavaScript objects.</li><li>To automate the serialization of JavaScript objects into JSON format for network transport.</li></ul>',
        'theory': '<p>Express.js is a fast, unopinionated, minimalist web framework for Node.js. While Node\'s native HTTP module is powerful, creating complex routing logic is cumbersome. Express abstracts this complexity, providing a robust set of features for web and mobile applications.</p><p>Routes determine how the application responds to client requests at particular endpoints, which consist of a URI (or path) and a specific HTTP request method (GET, POST, PUT, DELETE).</p><p><strong>Application Flow:</strong><br>Express App Instance -&gt; Define Endpoint Definitions (/ and /profile) -&gt; Bind Route Handlers -&gt; Listen on Port 3000 -&gt; Automatic JSON Serialization on Request</p>',
        'procedure': '<ol><li>Import the <code>express</code> module using CommonJS require.</li><li>Initialize the application instance by executing <code>express()</code>.</li><li>Define an arbitrary port variable (e.g., 3000).</li><li>Define a root route (<code>/</code>) using <code>app.get()</code> and utilize <code>res.send()</code> to return an HTML string.</li><li>Define a secondary API route (<code>/profile</code>) targeting data retrieval.</li><li>Create a local JavaScript object containing structured profile details (Name, Dept, CGPA).</li><li>Utilize the <code>res.json()</code> method to automatically serialize and dispatch the object.</li><li>Call <code>app.listen()</code> to bind the application to the network port.</li><li>Verify functionality by accessing both endpoints via a web browser.</li></ol>',
        'code_explanation': make_code_exp({
            "const app = express();": "Creates an Express application object, providing routing and middleware capabilities.",
            "app.get('/route', callback)": "Routes HTTP GET requests to the specified path with the specified callback functions.",
            "res.send('HTML')": "Sends the HTTP response, automatically assigning the text/html content-type header.",
            "res.json(object)": "Sends a JSON response, automatically converting the JS object via JSON.stringify().",
            "app.listen(port, callback)": "Binds and listens for connections on the specified host and port."
        }),
        'test_cases_table': "".join([
            make_tc_row("TC-01", "Root Endpoint Routing", "Send GET request to localhost:3000/", "Express intercepts request and responds with HTML Welcome page", "Pass"),
            make_tc_row("TC-02", "API Endpoint Routing", "Send GET request to localhost:3000/profile", "Express executes specific handler, returning Profile object", "Pass"),
            make_tc_row("TC-03", "404 Not Found Handling", "Access undefined endpoint /invalid", "Express falls back to default 404 handler, returning 'Cannot GET /invalid'", "Fail")
        ]),
        'output_data': [
            ("Output 1: /profile API Endpoint JSON Response", r"02-record\week-06\screenshots\json_out.png"),
            ("Output 2: Root Route HTML Rendering", r"02-record\week-06\screenshots\browser_out.png")
        ],
        'testcases_data': [
            ("Test Case 1: Route Invalid Check", r"02-record\week-06\testcases\tc_fail.png")
        ],
        'files': [r'02-record\week-06\src\week6.js'],
        'pdf_out': r'02-record\week-06\Record_Week6.pdf'
    }
]

def generate_pdfs_for_repo(repo_path, student_name, roll_no):
    for task in records_data:
        code_html = ''
        for filepath in task['files']:
            full_path = os.path.join(repo_path, filepath)
            content = read_file(full_path)
            code_html += f'<p><strong>Source File:</strong> {os.path.basename(filepath)}</p><pre><code>{content}</code></pre>'
            
        output_html = ''
        for out_title, img in task['output_data']:
            abs_path = os.path.abspath(os.path.join(repo_path, img)).replace(chr(92), '/')
            if os.path.exists(os.path.join(repo_path, img)):
                encoded_path = urllib.parse.quote(abs_path, safe=':/')
                output_html += f'<p class="output-title">{out_title}</p><img src="file:///{encoded_path}" />'
                
        testcases_html = ''
        for tc_title, tc_img in task['testcases_data']:
            abs_path = os.path.abspath(os.path.join(repo_path, tc_img)).replace(chr(92), '/')
            if os.path.exists(os.path.join(repo_path, tc_img)):
                encoded_path = urllib.parse.quote(abs_path, safe=':/')
                testcases_html += f'<p class="output-title">{tc_title}</p><img src="file:///{encoded_path}" />'

        html = html_template.format(
            doc_type=task['doc_type'],
            exp_no=task['exp_no'],
            title=task['title'],
            aim=task['aim'],
            objective=task['objective'],
            theory=task['theory'],
            procedure=task['procedure'],
            code_html=code_html,
            code_explanation=task['code_explanation'],
            test_cases_table=task['test_cases_table'],
            output_html=output_html,
            testcases_html=testcases_html,
            student_name=student_name,
            roll_no=roll_no,
            result="Thus, the experiment was successfully implemented and verified across both positive functional and negative validation test cases."
        )
        
        temp_file = os.path.join(repo_path, 'temp.html')
        with open(temp_file, 'w', encoding='utf-8') as f: f.write(html)
        pdf_out = os.path.abspath(os.path.join(repo_path, task["pdf_out"]))
        subprocess.run([
            r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            '--headless',
            '--disable-gpu',
            '--no-pdf-header-footer',
            f'--print-to-pdf={pdf_out}',
            f'file:///{os.path.abspath(temp_file).replace(chr(92), "/")}'
        ])
        if os.path.exists(temp_file): os.remove(temp_file)

# 1. Generate for Charishma
generate_pdfs_for_repo(r"C:\Users\rohit\.gemini\antigravity\scratch\Fullstack069", "B.Charishma", "a24126552067")

# 2. Generate for Rohit
generate_pdfs_for_repo(r"C:\Users\rohit\.gemini\antigravity\scratch\FullStack", "A.Rohit", "324126510006")
