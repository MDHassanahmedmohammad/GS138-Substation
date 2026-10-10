# PowerWorld Files

The supplied files in this project use the `.pwd` extension. In PowerWorld, `.pwd` files are one-line/display files; they are not a substitute for the complete solved `.pwb` case database.

Files supplied for this portfolio:

- `GS138_BASE_30MW.pwd`
- `GS138_BaseCase.pwd`
- `GS138_LoadGrowth.pwd`
- `GS138_LoadGrowth_+15.pwd`
- `GS138_LoadGrowth_13.pwd`
- `GS138_T1_Out_30MW.pwd`
- `GS138_T1_Out_40MW.pwd`
- `GS138_T2_Out_40MW.pwd`

For a fully reproducible PowerWorld study, also add the matching `.pwb` case file(s) if available and shareable.

## Binary upload note

The GitHub connector used in this chat can create and edit repository text files, but the remaining binary assets are not being accepted through this connector path. Add the `.pwd`, `.pwb`, PDF, PNG, and DOCX assets through GitHub's **Add file > Upload files** interface while preserving the folder structure.

## Integrity check

SHA-256 checking of the supplied files found two byte-identical pairs:

- `GS138_LoadGrowth_+15.pwd` and `GS138_LoadGrowth_13.pwd`
- `GS138_T1_Out_30MW.pwd` and `GS138_T2_Out_40MW.pwd`

If these are intended to represent different solved conditions, open them in PowerWorld and verify/save the intended display files before publishing.

See `SHA256SUMS.txt` for all supplied `.pwd` checksums.
