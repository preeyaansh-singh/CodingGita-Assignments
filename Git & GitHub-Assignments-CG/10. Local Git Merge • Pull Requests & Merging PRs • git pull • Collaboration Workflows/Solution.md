### Instructions
Complete all mandatory assignments in order. Use your existing practice repo (recommended name: CodingGita_Assignments) for submission.  
Take clear screenshots where asked. Submit the **GitHub repository link** or required screenshots or both as per the submission guidelines of each assignment.

**Before you start:** Make sure your local `main` is clean and up to date (`git status` and `git pull`).

---

### Assignment 1 – Local Merge (Mandatory)

**Goal:** Practice merging a feature branch into `main` locally.

1. Create a new branch:  
   `git checkout -b feature-local-merge`
2. Create a file named `local-merge.txt` and write 3–4 lines about what you learned today about local merge.
3. Stage and commit:  
   `git add .`  
   `git commit -m "Add local-merge notes"`
4. Switch back to main:  
   `git checkout main`
5. Merge the feature branch:  
   `git merge feature-local-merge`
6. Push main:  
   `git push origin main`
7. Run `git log --oneline -5` and take a screenshot of the history.

**Submit:** Screenshot of `git log --oneline` after the merge + confirmation that the file is on GitHub `main`.

**Answer :**

<img width="852" height="167" alt="image" src="https://github.com/user-attachments/assets/abfac510-f4b3-4ea6-850e-2eeba59380ad" />
<img width="927" height="557" alt="image" src="https://github.com/user-attachments/assets/b60a6557-2ea4-44d7-9184-63ccee4277b6" />

---

### Assignment 2 – Pull Request Workflow (Mandatory)

**Goal:** Create a Pull Request, merge it on GitHub, then update local main with `git pull`.

1. Create a new branch:  
   `git checkout -b feature-pr-practice`
2. Create a file named `pr-practice.txt`. Write what a Pull Request is and why teams use it (4–5 lines).
3. Commit:  
   `git add .`  
   `git commit -m "Add PR practice notes"`
4. Push the branch:  
   `git push -u origin feature-pr-practice`
5. On GitHub: Open a Pull Request from `feature-pr-practice` into `main`. Write a clear PR title and description.
6. Merge the Pull Request on GitHub (use **“Create a merge commit”** option).
7. Delete the feature branch on GitHub (optional but recommended).
8. Locally:  
   `git checkout main`  
   `git pull origin main`
9. Confirm `pr-practice.txt` is now present on local main. Take a screenshot of the terminal after pull and of the merged PR on GitHub.

**Submit:** Link to the merged PR + screenshot of successful `git pull` + screenshot of GitHub PR (merged state).

**Answer :**

<img width="860" height="105" alt="image" src="https://github.com/user-attachments/assets/261473dc-78f5-43e0-87ca-25cf526e0fb1" />
<img width="912" height="177" alt="image" src="https://github.com/user-attachments/assets/7b6de1f6-ea72-4ed3-bb06-0473fd72ad25" />
<img width="652" height="315" alt="image" src="https://github.com/user-attachments/assets/10223695-7b7a-4d20-83e1-6dca794ec339" />

---

### Assignment 3 – Compare Both Workflows (Mandatory)

**Goal:** Experience both methods side-by-side and write a short comparison.

1. You already did one local merge (Assignment 1) and one PR merge (Assignment 2).
2. Create a short file named `comparison.txt` (on a new branch or directly on main).
3. In that file answer these questions **in your own words**:
   - What is the main difference between local merge and PR merge?
   - When would you prefer a local merge?
   - When is a Pull Request better?
   - After merging a PR on GitHub, which command brings the changes to your computer?
   - What does `git pull` actually do (two steps)?
4. Commit and push `comparison.txt` (either via local merge or via a new PR).

**Submit:** Content of `comparison.txt` (or screenshot) + link to the commit/PR.

**Answer :**

<img width="551" height="117" alt="image" src="https://github.com/user-attachments/assets/eafbf3a5-37ae-4a4e-beee-b9e5e62021a1" />
<img width="1117" height="460" alt="image" src="https://github.com/user-attachments/assets/f9da6ffc-5b0a-455b-a8b0-aa1cd1eb6333" />

### Assignment 4 – git pull Practice (Mandatory)

**Goal:** Practice updating local branches safely with `git pull`.

1. Make sure you are on `main`:  
   `git checkout main`
2. Run `git pull origin main` and observe the output.
3. Create a small change on GitHub itself (edit any file using the GitHub web editor on `main` and commit).
4. Back in your terminal, run `git pull origin main` again.
5. Confirm the web change is now in your local files.
6. Take a screenshot of the terminal showing the pull that brought the web change.

**Submit:** Screenshot of the successful `git pull` that received the GitHub web edit.

**Answer :**

<img width="652" height="321" alt="image" src="https://github.com/user-attachments/assets/50e748b0-ceb1-478f-9fc4-22baf8acc5b0" />

