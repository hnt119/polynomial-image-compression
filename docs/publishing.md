# Publishing reviewed research evidence

The existing public repository is [hnt119/polynomial-image-compression](https://github.com/hnt119/polynomial-image-compression). Its default branch is `main`. **Do not create another repository for this archive.** The older setup instructions described a local checkout before GitHub publication and have been superseded.

For the 5 November 2026 export, GitHub main was verified at `38567c5faa1355e55f90596bd1043163df22dda8`. The historical local main at `484df0c4c615e05e1912f9f41f9e501c07fce001` had a different root commit. The 73 shared tree entries matched exactly; the local history also carried six project dotfiles absent from the upload. The release was prepared on a dedicated branch **from upstream main**, not by rewriting or merging the histories. The original working checkout remains available locally.

For future releases, fetch upstream, compare both history and content, review each added path and the complete staged diff, run the documented checks on the public tree, and push the reviewed branch normally. Use a PR when histories, protections, or pending work make a direct main update inappropriate. Verify the remote head matches the intended commit; report Actions separately from local checks. A PR is not a merge.

Do not publish the private migration bundle, administrative records, correspondence, machine paths, credentials or third-party reference PDFs. Preserve those locally. Use a documented portable copy when an otherwise publishable result embeds a private locator. Keep archived hashes and the existing license notice unchanged. See the [release inventory](release/2026-11-05/README.md) and [reproduction guide](reproducibility.md).
