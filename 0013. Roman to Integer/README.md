<!DOCTYPE html>
<html>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0013. Roman to Integer</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table><th>Hash-Table</th><th>String</th><th>Math</th></table></div><br>
        <div style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif;"><p>
            Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 
            For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.<br><br>
            Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
            <ul>
                <li>I can be placed before V (5) and X (10) to make 4 and 9. </li>
                <li>X can be placed before L (50) and C (100) to make 40 and 90. </li>
                <li>C can be placed before D (500) and M (1000) to make 400 and 900.</li>
                <li>Given a roman numeral, convert it to an integer.</li>
            </ul>  
        </p></div><br>
        <div style="background-color: papayawhip;">
            <table border="1", type="1" style="width: 25%; border-collapse: collapse; margin: 20px 0; margin-left: 20px;">
                <strong> 
                    <th style="border:1px solid black;">Symbol</th>
                    <th style="border:1px solid black;">Value</th>
                </strong>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">I</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">1</td></tr>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">V</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">5</td></tr>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">X</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">10</td></tr>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">L</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">50</td></tr>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">C</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">100</td></tr>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">D</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">500</td></tr>
                <tr><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">M</td><td style="padding: 12px; text-align: center; border: 2px solid #ddd;">1000</td></tr>
            </table> 
        </div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> x = 121 <br>
                <strong>Output:</strong> true <br>
                <strong>Explanation:</strong><br> 121 reads as 121 from left to right and from right to left. <br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> x = -121<br>
                <strong>Output:</strong> false <br>
                <strong>Explanation:</strong><br> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. <br>
            </p></div>
            <div><p>
                <strong><u>Example 3:</u></strong><br>
                <strong>Input:</strong> x = 10 <br>
                <strong>Output:</strong> false <br>
                <strong>Explanation:</strong><br> Reads 01 from right to left. Therefore it is not a palindrome. <br>
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>1 <= s.length <= 15</li>
                <li>s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').</li>
                <li>It is <strong>guaranteed</strong> that s is a valid roman numeral in the range [1, 3999].</li>
            </ul>
        </div>
    </body>
</html>
