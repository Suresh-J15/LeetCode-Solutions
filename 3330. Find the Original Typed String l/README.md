<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>3330. Find the Original Typed String l</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table type="1"><th>String</th></table></div><br><br>
        <div><p style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif" >
            Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and <strong>may</strong> press a key for too long, resulting in a character being typed <strong>multiple</strong> times. <br><br>
            Although Alice tried to focus on her typing, she is aware that she may still have done this <strong>at most</strong> once. <br><br>
            You are given a string word, which represents the <strong>final</strong> output displayed on Alice's screen.<br><br>
            Return the total number of possible original strings that Alice might have intended to type. <br>
        </p></div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> word = "abbcccc" <br>
                <strong>Output:</strong> 5 <br>
                <strong>Explanation:</strong><br>The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".<br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> word = "abcd" <br>
                <strong>Output:</strong> 1 <br>
            </p></div>
            <div><p>
                <strong><u>Example 3:</u></strong><br>
                <strong>Input:</strong> word = "aaaa" <br>
                <strong>Output:</strong> 4
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>1 <= word.length <= 100</li>
                <li>word consists only of lowercase English letters.</li>
            </ul>
        </div>
    </body>
</html>
