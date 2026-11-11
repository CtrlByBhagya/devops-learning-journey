# Day 3 – Linux Practice

## 1. Getting help in Linux

Linux provides documentation to help us understand commands and their options.

### `man` command

`man` stands for manual. It displays detailed information about a Linux command.

```bash
man ls
```

This opens the manual page for the `ls` command.

Useful keys inside the manual:

- `Space` – Move one page down.
- `b` – Move one page up.
- `↑` and `↓` – Move line by line.
- `/word` – Search for a word.
- `n` – Find the next occurrence.
- `q` – Quit the manual.

### `--help` option

We can also use `--help` to get a quick explanation of a command.

```bash
ls --help
```

Difference:

- `man ls` gives detailed documentation in an interactive viewer.
- `ls --help` displays a shorter help summary in the terminal.

## 2. Useful options of `ls`

| Option | Meaning |
|---|---|
| `ls -l` | Shows detailed information about files. |
| `ls -a` | Shows hidden files too. |
| `ls -h` | Shows file sizes in a human-readable format. |
| `ls -R` | Lists files inside subdirectories recursively. |

We can combine options:

```bash
ls -lh
```

This shows detailed information with readable file sizes.

## 3. Linux Wildcards

Wildcards help us match multiple filenames without typing every filename separately.

### Asterisk (`*`)

`*` matches zero or more characters.

Example:

```bash
ls *.txt
```

This lists all files ending in `.txt`.

In my practice directory, it displayed:

```text
a1.txt
a2.txt
b1.txt
```

### Question mark (`?`)

`?` matches exactly one character.

Example:

```bash
ls a?.txt
```

This matches filenames such as:

```text
a1.txt
a2.txt
```

Another example:

```bash
ls b?.txt
```

This matches `b1.txt`.

If no filename matches a wildcard pattern, Linux displays an error saying it cannot access that pattern.

## 4. Copying multiple files using wildcards

We can use wildcards with the `cp` command.

Instead of copying each file separately:

```bash
cp a1.txt backup/
cp a2.txt backup/
cp b1.txt backup/
```

We can write:

```bash
cp *.txt backup/
```

This copies all matching `.txt` files into the `backup` directory.

To check the copied files:

```bash
ls backup/
```

I verified that `a1.txt`, `a2.txt` and `b1.txt` were copied successfully.

**Important difference:**

- `cp` copies files. The original files remain in their location.
- `mv` moves files. They are removed from their previous location.

## What I learned today

- How to use manual pages to understand Linux commands.
- How to search and navigate inside `man`.
- How to use `--help` for quick command information.
- The difference between `*` and `?` wildcards.
- How to select multiple files using filename patterns.
- How to copy multiple matching files into a directory using `cp`.