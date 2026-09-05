# Publish the prepared repository

The repository is initialized locally on `main`. Public GitHub publication was
requested, but the browser's administrator-policy check was unavailable during
setup. No GitHub repository was created, and no remote was configured. GitHub
access must be restored before publishing.

The initial commit uses the neutral author `Repository setup <noreply@localhost>`
so preparing the repository does not expose a personal email address. Later
commits can use the owner's preferred Git identity.

## When GitHub access is available

### Publish through the website

A clean export is supplied alongside the working repository as
`polynomial-image-compression-public.zip`. It contains the committed files and
GitHub workflow, without the local `.git` directory, caches, or private paths.

1. Open [GitHub's new repository page](https://github.com/new) in your own browser.
2. Select your account, enter `polynomial-image-compression`, and choose **Public**.
   Leave README, gitignore, and license initialization off, then create the repository.
3. Extract `polynomial-image-compression-public.zip`. On the empty repository page,
   choose **uploading an existing file**.
4. Drag the extracted folder's **contents** into the upload page, including
   `.github`, `.gitattributes`, and `.gitignore`. On macOS, press
   **Command–Shift–Period** in Finder to reveal those hidden items. Upload the
   contents, not the ZIP file or an extra enclosing folder.
5. Commit the upload to `main`. Check the rendered README, the four-track history,
   and the **Research checks** workflow under **Actions**.

The website upload creates a new GitHub commit. It does not preserve the prepared
local Git commit history. Use the following route if preserving that history is
preferred.

### Publish with the GitHub CLI

From a machine with the GitHub CLI installed and signed in to the intended account,
run this from the repository root:

```bash
gh repo create polynomial-image-compression --public --source=. --remote=origin --push --description "Research notes and exact experiments on polynomial image compression, unit-distance and sum-product methods."
```

Alternatively, create an empty public repository named
`polynomial-image-compression` on GitHub, leaving the README, license, and
gitignore initialization options off. Then use the remote address displayed by
GitHub:

```bash
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

`YOUR_REPOSITORY_URL` is a placeholder for that repository's actual HTTPS or SSH
address. Use the account's existing authorized authentication flow. If a
repository with this name already exists, inspect it before choosing whether to
reuse it; do not force-push this archive over existing work.

After publication, verify that the README, four track records, and 39 archived sources appear on
`main`, and inspect the **Research checks** workflow. The local tests have run;
GitHub's Python-version matrix has not run until a remote workflow executes.
