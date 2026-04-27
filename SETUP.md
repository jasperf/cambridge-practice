# Setting Up cambridge-practice on GitHub Pages

A step-by-step guide to get the site live at `jasperf.github.io/cambridge-practice`.

---

## Step 1 — Create the repo on GitHub

1. Go to **github.com/new** (make sure you're logged in as `jasperf`)
2. Fill in:
   - **Repository name:** `cambridge-practice`
   - **Description:** `Interactive self-marking exercise sheets for Cambridge Secondary & IGCSE`
   - **Visibility:** Public *(required for free GitHub Pages)*
   - Leave "Initialize with README" **unchecked** — we'll push our own
3. Click **Create repository**
4. Keep the page open — you'll need the remote URL in Step 3

---

## Step 2 — Set up the local directory

Open Terminal and run these commands one by one:

```bash
# 1. Go to your code directory (create it if it doesn't exist)
mkdir -p ~/code
cd ~/code

# 2. Create the project folder
mkdir cambridge-practice
cd cambridge-practice

# 3. Initialise git
git init

# 4. Set your identity (if not already set globally)
git config user.name "jasperf"
git config user.email "your@email.com"
```

---

## Step 3 — Add the files

Copy the three files from Claude's output into `~/code/cambridge-practice/`:

```
~/code/cambridge-practice/
├── index.html                              ← home page
├── README.md                               ← repo description
└── s1/
    └── term4-week1-maths-science.html      ← Week 1 exercises
```

You can do this in Finder (drag and drop) or Terminal:

```bash
# Example if files are in ~/Downloads:
cp ~/Downloads/index.html ~/code/cambridge-practice/
cp ~/Downloads/README.md ~/code/cambridge-practice/
mkdir -p ~/code/cambridge-practice/s1
cp ~/Downloads/term4-week1-maths-science.html ~/code/cambridge-practice/s1/
```

---

## Step 4 — First commit and push

```bash
cd ~/code/cambridge-practice

# Stage everything
git add .

# First commit
git commit -m "Initial commit: Week 1 Maths & Science exercises"

# Connect to GitHub (paste the URL from Step 1)
git remote add origin https://github.com/jasperf/cambridge-practice.git

# Push
git branch -M main
git push -u origin main
```

If prompted for credentials, use your GitHub username and a **Personal Access Token**
(not your password). Generate one at: github.com/settings/tokens → New classic token → scope: `repo`.

---

## Step 5 — Enable GitHub Pages

1. Go to your repo: **github.com/jasperf/cambridge-practice**
2. Click **Settings** (top tab)
3. Scroll to **Pages** in the left sidebar
4. Under **Source**, set:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait ~60 seconds, then visit:

   👉 **https://jasperf.github.io/cambridge-practice**

---

## Step 6 — Adding new exercise sheets (your weekly workflow)

```bash
cd ~/code/cambridge-practice

# Create next week's file (copy from last week as template)
cp s1/t4/w1/term4-week1-maths-science.html s1/term4-week2-english-maths.html

# Edit the new file in VS Code
code s1/term4-week2-english-maths.html

# When ready, push it live:
git add .
git commit -m "Add Week 2: English & Maths exercises"
git push
```

GitHub Pages auto-deploys within ~30 seconds of every push. No build step needed.

---

## Optional: Custom domain

If you buy a domain (e.g. `cambridgepractice.com` on Namecheap, ~$12/yr):

```bash
# 1. Create a CNAME file in the repo root
echo "cambridgepractice.com" > CNAME
git add CNAME
git commit -m "Add custom domain"
git push
```

2. In your domain registrar's DNS settings, add:
   - Type: `CNAME`
   - Host: `www`
   - Value: `jasperf.github.io`

3. Back in GitHub Settings → Pages, enter your domain and tick **Enforce HTTPS**.

Takes 10–30 minutes to propagate.

---

## Folder structure to maintain

```
cambridge-practice/
├── index.html              ← update this when adding new sheets
├── README.md
├── CNAME                   ← only if using custom domain
├── s1/                     ← Secondary 1
│   ├── term4-week1-maths-science.html
│   ├── term4-week2-english.html
│   └── ...
├── s2/                     ← Secondary 2 (future)
└── igcse/                  ← IGCSE (future)
```

---

## Quick reference commands

| Task | Command |
|------|---------|
| Check status | `git status` |
| See what changed | `git diff` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push live | `git push` |
| Pull latest | `git pull` |
| Open in VS Code | `code .` |
