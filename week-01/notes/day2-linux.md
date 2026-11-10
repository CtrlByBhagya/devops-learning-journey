# Day 2 – Linux Basics

Today I learned how to create, copy, move, delete and read files and directories in Linux.

## 1. mkdir – Make a Directory

The `mkdir` command is used to create a new directory (folder).

**Syntax:**
```bash
mkdir folder_name
```

**Example:**
```bash
mkdir backup
```

This creates a new folder called `backup`.

## 2. touch – Create a File

The `touch` command is used to create an empty file.

**Syntax:**
```bash
touch filename
```

**Example:**
```bash
touch linux.txt
```

This creates an empty file called `linux.txt`.

## 3. cp – Copy a File

The `cp` command is used to make a copy of a file.

**Syntax:**
```bash
cp source destination
```

**Example:**
```bash
cp linux.txt linux-backup.txt
```

This creates a copy of `linux.txt` named `linux-backup.txt`.

The original file remains unchanged.

## 4. mv – Move or Rename a File

The `mv` command is used to move a file from one location to another or change its name.

**Example 1: Rename a file**
```bash
mv linux.txt linux-notes.txt
```

Changes the filename from `linux.txt` to `linux-notes.txt`.

**Example 2: Move a file into a folder**
```bash
mv linux-backup.txt backup/
```

Moves `linux-backup.txt` into the `backup` folder.

## 5. rm – Remove a File

The `rm` command is used to delete a file.

**Syntax:**
```bash
rm filename
```

**Example:**
```bash
rm linux-notes.txt
```

This deletes the file `linux-notes.txt`.

**Useful option:**
```bash
rm -i filename
```

The `-i` option asks for confirmation before deleting the file.

Be careful while using `rm` because deleted files are not normally sent to a recycle bin.

## 6. cat – Read and Write Files

The `cat` command is used to display the contents of a file.

**Example:**
```bash
cat linux-backup.txt
```

This displays everything written inside the file.

We can also use `cat` to write content into a file.

**Using `>` (overwrite):**
```bash
cat > notes.txt
```

This creates a file and lets us type content into it. If the file already contains something, its old content gets replaced.

Press `Ctrl + D` when finished.

**Using `>>` (append):**
```bash
cat >> notes.txt
```

This adds new content at the end of the file without deleting the existing content.

Press `Ctrl + D` when finished.

## 7. less – Read Large Files

The `less` command is used to read a file one screen at a time.

It is especially useful when a file contains many lines.

**Example:**
```bash
less application.log
```

Some useful keys while using `less`:

- `Space` – Move to the next page.
- `b` – Go to the previous page.
- `↑` and `↓` – Move up and down.
- `/ERROR` – Search for the word ERROR.
- `n` – Find the next matching result.
- `q` – Exit `less`.

**Difference between `cat` and `less`:**

- `cat` displays the complete file at once.
- `less` allows us to move through the file page by page.

## 8. head – Read the Beginning of a File

The `head` command displays the first 10 lines of a file by default.

**Example:**
```bash
head linux-backup.txt
```

To display only the first 3 lines:

```bash
head -n 3 linux-backup.txt
```

Here, `-n 3` means display 3 lines.

## 9. tail – Read the End of a File

The `tail` command displays the last 10 lines of a file by default.

**Example:**
```bash
tail linux-backup.txt
```

To display only the last 2 lines:

```bash
tail -n 2 linux-backup.txt
```

### Monitoring a File Continuously

```bash
tail -f application.log
```

The `-f` option keeps displaying new lines whenever they are added to the file.

This is useful when monitoring application logs to see new errors or updates.

Press `Ctrl + C` to stop.

---

## What I Learned Today

I practised all nine commands and understood how to:

1. Create directories and files.
2. Copy, move, rename and delete files.
3. Read and write file contents.
4. View large files page by page.
5. Read the beginning and end of files.
6. Monitor new entries in log files.

These commands are useful when working with Linux servers and managing files in DevOps.