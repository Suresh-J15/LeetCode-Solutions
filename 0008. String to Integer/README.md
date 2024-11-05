<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0008. String to Integer</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium">
        <div><table type="1"><th>String</th></table></div><br><br>
        <div><p style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif" >
            Implement the <strong>myAtoi(string s)</strong> function, which converts a string to a 32-bit signed integer. <br><br>
            The algorithm for <strong>myAtoi(string s)</strong> is as follows: <br>
            <strong>Whitespace:</strong> Ignore any leading whitespace <strong>(" ")</strong>. <br>
            <strong>Signedness:</strong> Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present. <br>
            <strong>Conversion:</strong> Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0. <br>
            <strong>Rounding:</strong> If the integer is out of the 32-bit signed integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then round the integer to remain in the range. Specifically, integers less than -2<sup>31</sup> should be rounded to -2<sup>31</sup>, and integers greater than 2<sup>31</sup> - 1 should be rounded to 2<sup>31</sup> - 1. <br>
            Return the integer as the final result. <br> 
        </p></div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> s = "42" <br>
                <strong>Output:</strong> 42 <br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> s = " -042"<br>
                <strong>Output:</strong> -42 <br>
            </p></div>
            <div><p>
                <strong><u>Example 3:</u></strong><br>
                <strong>Input:</strong> s = "1337c0d3" <br>
                <strong>Output:</strong> 1337 <br>
            </p></div>
            <div><p>
                <strong><u>Example 4:</u></strong><br>
                <strong>Input:</strong> "0-1" <br>
                <strong>Output:</strong> 0 <br>
            </p></div>
            <div><p>
                <strong><u>Example 5:</u></strong><br>
                <strong>Input:</strong> s = "words and 987" <br>
                <strong>Output:</strong> 0 <br>
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>0 <= s.length <= 200</li>
                <li>s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.</li>
            </ul>
        </div>
    </body>
</html>
