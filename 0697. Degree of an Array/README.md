<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0697. Degree of an Array</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table type="1"><th>Array</th><th>Hash-Table</th></table></div><br>
        <div><p style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif" >
            Given a non-empty array of non-negative integers nums, the <strong>degree</strong> of this array is defined as the maximum frequency of any one of its elements.<br><br>
            Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.<br>
        </p></div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> nums = [1,2,2,3,1] <br>
                <strong>Output:</strong> [0,1] <br>
                <strong>Explanation:</strong><br> 
                The input array has a degree of 2 because both elements 1 and 2 appear twice.
                Of the subarrays that have the same degree:<br>
                [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]<br>
                The shortest length is 2. So return 2. <br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> nums = [1,2,2,3,1,4,2]<br>
                <strong>Output:</strong> 6<br>
                <strong>Explanation:</strong><br> 
                The degree is 3 because the element 2 is repeated 3 times.<br>
                So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6. <br>
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>nums.length will be between 1 and 50,000.</li>
                <li>nums[i] will be an integer between 0 and 49,999.</li>
            </ul>
        </div>
    </body>
</html>
