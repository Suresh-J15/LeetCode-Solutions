<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0020. Valid Parentheses</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table type="1"><th>String</th><th>Stack</th></table></div><br>
        <div style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif"><p>
            Given a string s containing just the characters '(' , ')' , '{' , '}' , '[' and ']' , determine if the input string is valid. <br><br>
            An input string is valid if:<br>
            </p>
            <ol type="1">
                <li>Open brackets must be closed by the same type of brackets.</li>
                <li>Open brackets must be closed in the correct order.</li>
                <li>Every close bracket has a corresponding open bracket of the same type.</li>
            </ol> 
        </div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> s = "()" <br>
                <strong>Output:</strong> true <br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> s = "()[]{}" <br>
                <strong>Output:</strong> true <br>
            </p></div>
            <div><p>
                <strong><u>Example 3:</u></strong><br>
                <strong>Input:</strong> s = "(]" <br>
                <strong>Output:</strong> false <br>
            </p></div>
            <div><p>
                <strong><u>Example 4:</u></strong><br>
                <strong>Input:</strong> s = "([])" <br>
                <strong>Output:</strong> true
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>1 <= s.length <= 10<sup>4</sup></li>
                <li>s consists of parentheses only '()[]{}'.</li>
            </ul>
        </div> 
    </body>
</html>
