# Daily Job Openings Tracker

Automatically fetches job postings every morning and saves them as a dated Excel file in the `reports/` folder.

## Setup (one time, ~10 minutes)

1. **Get a free API key**
   - Go to https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch
   - Sign up (free) and subscribe to the **Basic (free) plan**
   - Copy your API key (X-RapidAPI-Key)

2. **Create a GitHub repo**
   - Upload all these files, keeping the folder structure
     (`.github/workflows/daily_jobs.yml` must stay in that path)

3. **Add the API key as a secret**
   - Repo → Settings → Secrets and variables → Actions → New repository secret
   - Name: `RAPIDAPI_KEY`  |  Value: your key

4. **Customize your searches**
   - Edit `SEARCH_QUERIES` at the top of `fetch_jobs.py`

5. **Test it**
   - Repo → Actions → "Daily Job Openings" → Run workflow

Every day at 8:00 AM UAE time a new file appears:
`reports/jobs_2026-07-21.xlsx`

## Notes
- Free JSearch plan allows ~200 requests/month → keep queries × pages small (3 queries × 1 page daily is fine).
- Change the schedule in `daily_jobs.yml` (cron is in UTC).

## Email delivery setup

The report is emailed daily to srikanthpatel5141@gmail.com. To make this work:

1. **Create a Gmail App Password** (for the Gmail account that will SEND the mail — can be the same address):
   - Turn on 2-Step Verification: https://myaccount.google.com/security
   - Then go to https://myaccount.google.com/apppasswords
   - Create an app password named "job-tracker" and copy the 16-character code

2. **Add two more repo secrets** (Settings → Secrets and variables → Actions):
   - `GMAIL_USER` = your Gmail address (e.g. srikanthpatel5141@gmail.com)
   - `GMAIL_APP_PASSWORD` = the 16-character app password

3. To change the recipient later, edit `TO_EMAIL` at the top of `send_email.py`.

## Web app (dashboard)

A phone-friendly dashboard lives in `docs/index.html`. It shows every day's openings with search, source filters, salaries, and one-tap Apply buttons.

**Enable it once:**
1. Repo → Settings → Pages
2. Source: "Deploy from a branch" → Branch: `main` → Folder: `/docs` → Save
3. After the next workflow run, open: `https://<your-username>.github.io/<repo-name>/`

The dashboard reads `docs/jobs_data.json`, which the daily workflow refreshes automatically — so the page always shows the latest day's jobs. Bookmark it on your phone's home screen for one-tap access.
