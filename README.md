# BS-Notify

Program I made to notify me to measure my blood sugar every two hours. Writen in bash, for Mac OSX requiring no external libraries.

## Usage

Create or edit your crontab file to allow the script to be run every two hours

```bash
crontab -e
```

In the crontab file add this line, where you replace the path with the notify script you just cloned

```bash
0 */2 * * * <path/to/script>
```

Save the file and your done!
