### Instructions
Complete all mandatory assignments in order. Use your existing practice repo (recommended name: CodingGita_Assignments) for submission.  
Take clear screenshots where asked. Submit the **GitHub repository link** or required screenshots or both as per the submission guidelines of each assignment.

**Before you start:** Make sure local `main` is clean and up to date (`git status` + `git pull origin main`).

---

### Assignment 1 – Complete PR Lifecycle with `feature/contact-form` (Mandatory)

**Goal:** Practice the full cycle: branch → file → commit → push → PR → merge → cleanup.

1. Update main:  
   `git checkout main && git pull origin main`
2. Create branch:  
   `git checkout -b feature/contact-form`
3. Create file `contact.html` with a simple heading and a short paragraph about a contact form.
4. Stage, commit and push:  
   ```bash
   git add contact.html
   git commit -m "Add contact form page"
   git push -u origin feature/contact-form
   ```
5. On GitHub: Open a Pull Request (base = `main`, compare = `feature/contact-form`). Write a clear title and description.
6. Merge the Pull Request using **“Create a merge commit”**.
7. Delete the remote branch (GitHub “Delete branch” button or `git push origin --delete feature/contact-form`).
8. Update local main using the two-command method:  
   ```bash
   git checkout main
   git fetch origin main
   git merge origin/main
   ```
9. Delete local branch:  
   `git branch -d feature/contact-form`
10. Take screenshots of:  
    (a) the merged PR  
    (b) terminal after fetch + merge  
    (c) `git branch` showing the branch is gone

**Submit:** Merged PR link + the 3 screenshots listed above.

**Answers :**

<img width="686" height="90" alt="image" src="https://github.com/user-attachments/assets/02db33ed-69fa-4b5b-b459-92b4c88eda1a" />
<img width="1024" height="601" alt="image" src="https://github.com/user-attachments/assets/55922738-c18d-41fc-9a60-ac44551b719b" />
<img width="1024" height="169" alt="image" src="https://github.com/user-attachments/assets/5c9a03ac-494c-4fac-8dae-296d62bcf5dc" />

---

### Assignment 2 – `feature/about-page` with Review & Rework (Mandatory)

**Goal:** Practice receiving a review comment, reworking the **same** branch, and updating the PR.

1. Create branch:  
   `git checkout -b feature/about-page`
2. Create `about.html` with only a basic heading (intentionally incomplete).
3. Commit and push:  
   ```bash
   git add .
   git commit -m "Add about page skeleton"
   git push -u origin feature/about-page
   ```
4. Open a Pull Request on GitHub.
5. **Simulate review:** Add a comment on the PR yourself (or ask a classmate/mentor) requesting:  
   *“Please add a short paragraph about the purpose of the about page and a simple team section placeholder.”*
6. Rework on the **same branch**:  
   ```bash
   git checkout feature/about-page
   # edit about.html as requested
   git add .
   git commit -m "Address review: add description and team section"
   git push origin feature/about-page
   ```
7. Confirm the PR on GitHub now shows the new commit.
8. Merge the PR, delete remote branch, update local main (`git fetch` + `git merge` or `git pull`), delete local branch.
9. Screenshot:  
   (a) PR conversation showing the review comment + your new commit  
   (b) merged PR

**Submit:** PR link showing review comment + rework commit, plus merged PR screenshot.

**Answers :**


<img width="530" height="76" alt="image" src="https://github.com/user-attachments/assets/6a0d9385-d54b-4990-9a58-adc18f71eb44" />
<img width="1292" height="110" alt="image" src="https://github.com/user-attachments/assets/62bf4f4b-a4a4-4255-9977-f2b66142a178" />
<img width="1024" height="137" alt="image" src="https://github.com/user-attachments/assets/c3bce891-421c-4de8-821f-7d102f818639" />

---

### Assignment 3 – `feature/navbar` Independent Full Cycle (Mandatory)

**Goal:** Independently complete one more full PR lifecycle.

1. Create `feature/navbar` branch from updated main.
2. Create `navbar.html` with a heading and 3–4 lines describing what a navigation bar contains (Home, About, Contact, etc.).
3. Commit, push, open PR with a clear title and description.
4. Merge the PR on GitHub.
5. Delete remote branch.
6. Update local main using:  
   ```bash
   git fetch origin main
   git merge origin/main
   ```
7. Delete local branch with `git branch -d feature/navbar`.
8. Run `git log --oneline -10` and take a screenshot showing the merge commits from the features you completed.

**Submit:** Merged PR link + screenshot of `git log --oneline`.

**Answers :**









