<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0001. Two Sum</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table type="1"><th>Array</th><th>Hash-Table</th></table></div><br>
        <div><p style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif" >
            Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. <br><br>
            You may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. <br><br>
            You can return the answer in any order. <br>
        </p></div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> nums = [2,7,11,15], target = 9 <br>
                <strong>Output:</strong> [0,1] <br>
                <strong>Explanation:</strong><br> Because nums[0] + nums[1] == 9, we return [0, 1]. <br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> nums = [3,2,4], target = 6<br>
                <strong>Output:</strong> [1,2]<br>
            </p></div>
            <div><p>
                <strong><u>Example 3:</u></strong><br>
                <strong>Input:</strong> nums = [3,3], target = 6<br>
                <strong>Output:</strong> [0,1]
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>2 <= nums.length <= 10<sup>4</sup></li>
                <li>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></li>
                <li>-10<sup>9</sup> <= target <= 10<sup>9</sup></li>
                <li><strong>Only one valid answer exists.</strong></li>
            </ul>
        </div>
    </body>
</html>
