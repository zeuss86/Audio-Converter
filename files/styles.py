"""
styles.py - all custom CSS and static markup for the interface.

Design tokens
  Mist  #EEF2F1  page background, a cool pale green-grey
  Ink   #14282B  text, a deep blue-green black
  Pine  #17625E  actions and focus
  Brass #A8843A  one classic detail: the double rule under the masthead
  Line  #D5DEDB  hairlines and card borders

Type: Newsreader (serif) for headings, Public Sans for everything else.
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Public+Sans:wght@400;500;600&display=swap');

:root {
  --ink: #14282B;
  --pine: #17625E;
  --brass: #A8843A;
  --mist: #EEF2F1;
  --line: #D5DEDB;
  --muted: #5B6F6D;
}

html, body, .stApp { font-family: 'Public Sans', system-ui, sans-serif; color: var(--ink); }
.stApp { background: var(--mist); }
.block-container { max-width: 1120px; padding-top: 2.5rem; padding-bottom: 4rem; }

h1, h2, h3, h4 {
  font-family: 'Newsreader', Georgia, serif !important;
  color: var(--ink);
  font-weight: 600;
  letter-spacing: -0.01em;
}

/* Masthead: the one classic flourish is the brass double rule */
.masthead h1 { font-size: 2.8rem; line-height: 1.1; margin: 0 0 0.6rem; padding: 0; }
.masthead p { font-size: 1.05rem; line-height: 1.55; color: var(--muted); max-width: 50ch; margin: 0 0 1.4rem; }
.masthead .rule { border-top: 4px double var(--brass); margin-bottom: 0.5rem; }

/* Sidebar */
[data-testid="stSidebar"] { background: #E3EAE8; border-right: 1px solid var(--line); }
[data-testid="stSidebar"] h3 { font-size: 1.15rem; margin-top: 0.4rem; }

/* Cards: containers created with st.container(key="card_...") */
[class*="st-key-card"] {
  background: #FFFFFF;
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 1.5rem 1.6rem 1.7rem;
  box-shadow: 0 1px 2px rgba(20, 40, 43, 0.06), 0 12px 30px rgba(20, 40, 43, 0.07);
}
[class*="st-key-card"] h3 { margin-top: 0; font-size: 1.45rem; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 0.25rem; border-bottom: 1px solid var(--line); margin-bottom: 1.2rem; }
.stTabs [data-baseweb="tab"] { font-weight: 600; font-size: 1rem; padding: 0.7rem 1.3rem; }

/* Drag-and-drop area */
[data-testid="stFileUploaderDropzone"] {
  background: #F7FAF9;
  border: 1.5px dashed #9DB3AF;
  border-radius: 8px;
  transition: border-color 0.15s, background 0.15s;
}
[data-testid="stFileUploaderDropzone"]:hover { border-color: var(--pine); background: #F0F6F5; }

/* Buttons */
.stButton > button, [data-testid="stDownloadButton"] > button {
  border-radius: 6px;
  font-weight: 600;
  padding: 0.55rem 1.4rem;
  box-shadow: 0 1px 2px rgba(20, 40, 43, 0.14);
}

/* Metrics */
[data-testid="stMetricValue"] { font-family: 'Newsreader', Georgia, serif; font-size: 1.75rem; }
[data-testid="stMetricLabel"] p { color: var(--muted); font-size: 0.85rem; }

/* Empty state */
.empty-note {
  border: 1.5px dashed var(--line);
  border-radius: 8px;
  padding: 2.4rem 1.2rem;
  text-align: center;
  color: var(--muted);
  line-height: 1.55;
}

@media (max-width: 640px) {
  .masthead h1 { font-size: 2.1rem; }
}
</style>
"""

MASTHEAD = """
<div class="masthead">
  <h1>Audio and Document Converter</h1>
  <p>Turn a PDF into an MP3 you can listen to, or an MP3 recording into text you can edit.</p>
  <div class="rule"></div>
</div>
"""
