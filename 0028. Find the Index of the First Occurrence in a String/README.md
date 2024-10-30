<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0028. Find the index of the First Occurrence in the String</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table type="1"><th>Two Pointers</th><th>String</th><th>String Matching</th></table></div><br>
        <div style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif">
          <p> Given two strings <i>needle</i> and <i>haystack</i>, return the index of the first occurrence of <i>needle</i> in <i>haystack</i>, or -1 if <i>needle</i> is not part of <i>haystack</i>. </p>
        </div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> haystack = "sadbutsad", needle = "sad" <br>
                <strong>Output:</strong> 0 <br>
                <strong>Explanation:</strong> <br>
                "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> haystack = "leetcode", needle = "leeto" <br>
                <strong>Output:</strong> -1 <br>
                <strong>Explanation:</strong> <br>
                "leeto" did not occur in "leetcode", so we return -1.
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>1 <= haystack.length, needle.length <= 10<sup>4</sup>.</li>
                <li><i>haystack</i> and <i>needle</i> consist of only lowercase English characters.</li>
            </ul>
        </div>
    </body>
</html>
