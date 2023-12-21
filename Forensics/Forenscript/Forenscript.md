# Forenscript
## Basic idea of the problem
So basically in this challenge you were given a file. The file had `.bin` extension and wasnt opening. 
## Initial Approach
Like any forensic challenge, i first tried to understand what the file was...fo i used `file` command on my terminal to know abt it but it was a waste. I t showed that it was a data file.
Then i tried using `binwalk` but it showed nothing. So finally i thought abt seeing it in a hex editor. I opened it on Hex Fiend.
## Something weird in the Hex Dump
now when u see the Hex Dump. You will find that the header of this file has strings like GNP and RDHIF. 

<img width="1398" alt="Screenshot 2023-12-22 at 00 53 19" src="https://github.com/LU1F3R/BackdoorCTF_23/assets/45719646/26b1ba9d-4e54-4122-bcc8-8bcb4ecec848">

You might know that for the PNG files the header contains strings like PNG and IHDR. Bingo!
This Hex Dump is having reverse hex bytes in the group of 4. Now all i needed to do was to reverse the batch of 4 hex bytes of the complete hex dump which was a pretty easy task. I made a script for the same.
```
#!/usr/bin/python

with open('a.bin', 'rb') as file:
    with open('a.png', 'wb') as out:
        while mbytes := file.read(4):
             out.write(bytes(reversed(mbytes)))
```
This will leave you with a png file.


![a](https://github.com/LU1F3R/BackdoorCTF_23/assets/45719646/01b0d3e7-569a-43df-9278-fd38555c261a)



But like all annoying challenges, this one also had a fake flag.

## Analysing the Fake flag
Now when you analyse this image using binwalk, you will notice that it has another png file in it. Now that's interesting so basically you have to extract an image from this image.
i tried using `binwalk -e` to extract but it didn't work. I didnt have any other idea of any tool for extracting. So i thought of analysing its hex dump.
Now since we know that there is another png file somewhere in this png file. That means that the hex dump of this png file should contain more than one header of a png file. So in my hex editor i just searched for hex bytes of the header of a png file
`04 67 41 4D 41 00 00 B1 8F 0B FC 61 05 00 00`.

<img width="1382" alt="Screenshot 2023-12-22 at 01 08 26" src="https://github.com/LU1F3R/BackdoorCTF_23/assets/45719646/42a30523-5e45-4d85-879b-1d879270dd0d">

And Bingo!!! I was correct. There is another png header in this file.
So now just erase all the bytes above this png header. And you will get the flag.

![a](https://github.com/LU1F3R/BackdoorCTF_23/assets/45719646/b7a077a3-7b91-46d0-8804-e7d4e1581c7d)

## Flag

`flag{scr1pt1ng_r34lly_t0ugh_a4n't_1t??}`





