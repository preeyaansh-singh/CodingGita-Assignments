### Assignment 1: Understanding Concepts

**Objective:** Check basic understanding of branching.

**Tasks:**
1. What is a **branch** in Git? Explain in your own words.
2. Why should we **not** work directly on the `main` branch?
3. Explain the road analogy of branching (main road vs side road).
4. What is the difference between `git branch` and `git switch`?

**Submission:** Written answers in your notebook.

**Answers :**

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/691605f2-4e5f-423b-92f2-1a740babde5a" />
<img width="1600" height="1025" alt="image" src="https://github.com/user-attachments/assets/fa12bcb5-c5af-405d-8a32-1634e4cf8af5" />

---

### Assignment 2: Commands Identification

**Objective:** Identify the correct commands.

**Tasks:**
1. Write the command for the following actions:

| Action                              | Command |
|-------------------------------------|---------|
| List all branches                   |         |
| Create a new branch named `feature-home` |    |
| Switch to `feature-home`            |         |
| Create + Switch in one command      |         |
| Merge `feature-home` into main      |         |
| Delete `feature-home` after merge   |         |

2. Write both the **modern** and **older** command for:
   - Switching to a branch
   - Creating + switching to a new branch

**Submission:** Filled table + answers


**Answers :**

<img width="1600" height="1508" alt="image" src="https://github.com/user-attachments/assets/d38d2b5f-8dc5-497e-8791-914c518c020b" />
<img width="1600" height="807" alt="image" src="https://github.com/user-attachments/assets/fbef37a5-471a-4040-bdfe-59417093da96" />

---

### Assignment 3: Practical Branching Workflow

**Objective:** Perform the complete branching cycle.

**Tasks:**
1. Make sure you are on the `main` branch.
2. Create a new branch named `feature-contact`.
3. Create a file `contact.txt` and write your name + any message.
4. Stage and commit the file with a meaningful message.
5. Switch back to `main`.
6. Merge `feature-contact` into `main`.
7. Delete the `feature-contact` branch.
8. Verify using:
   - `git branch`
   - `git log --oneline`

**Submission:**  
- Screenshot of `git branch` (before and after)  
- Screenshot of `git log --oneline`  
- Screenshot showing `contact.txt` is present on `main`

**Answers :**

<img width="2163" height="727" alt="image" src="https://github.com/user-attachments/assets/28206374-01bb-4a7a-89b5-b990086353b3" />
<img width="491" height="47" alt="image" src="https://github.com/user-attachments/assets/6d1d191d-e88f-4399-a7d9-af1fe0e38233" />
<img width="2167" height="726" alt="image" src="https://github.com/user-attachments/assets/a08b2950-36b2-44ec-b52f-f6ffe9905839" />
<img width="2161" height="728" alt="image" src="https://github.com/user-attachments/assets/574337c4-38b1-4b44-a7ba-09293a68eda1" />

---

### Assignment 4: Conceptual + Error Handling

**Objective:** Understand rules and common mistakes.

**Tasks:**
1. What will happen if you try to delete a branch that is not yet merged?  
   Write the error and how to fix it.
2. Why should you always **commit** before switching branches?
3. Fill in the correct flow:

```
______ → Work → ______ → ______ → Switch to main → ______ → Delete branch
```

4. Explain the difference between:
   - `git branch -d branch-name`
   - `git branch -D branch-name`

**Submission:** Written answers

**Answers :**

<img width="1565" height="1600" alt="image" src="https://github.com/user-attachments/assets/2facc4d4-6d0c-4d28-b5bb-1d65c14f0156" />
<img width="1600" height="824" alt="image" src="https://github.com/user-attachments/assets/146fd93c-4293-4189-b7f9-a3fee597521b" />

---

### Assignment 5: Complete Real Scenario

**Objective:** Apply branching in a realistic situation.

**Scenario:**  
You are working on a website project. Currently you are on the `main` branch. You need to add two new pages: **About** and **Services**.

**Tasks:**
1. Create a branch `feature-about`, add a file `about.txt`, commit it, merge it into `main`, and delete the branch.
2. Create another branch `feature-services`, add a file `services.txt`, commit it, merge it into `main`, and delete the branch.
3. After completing both, show:
   - Final list of branches (`git branch`)
   - Final commit history (`git log --oneline`)
4. Answer:
   - Why did we create two separate branches instead of doing both features on one branch?
   - What is the advantage of merging only after the feature is complete?

**Submission:**  
- Screenshots of both merges  
- Final `git branch` and `git log --oneline`  
- Written answers for the two questions

 **Answers :**

<img width="2161" height="728" alt="image" src="https://github.com/user-attachments/assets/9d67cc8a-4a3d-4124-8bae-1f329b93b10d" />
<img width="2070" height="760" alt="image" src="https://github.com/user-attachments/assets/9bc1cc94-9abc-449e-b4f1-dceb80171c1a" />
<img width="462" height="135" alt="image" src="https://github.com/user-attachments/assets/60c6e6b3-a37e-4f10-bfd3-5c7f28000d5d" />
<img width="591" height="161" alt="image" src="https://github.com/user-attachments/assets/d7101d6f-094e-4307-a507-8c62306256e6" />

Thank Youu
